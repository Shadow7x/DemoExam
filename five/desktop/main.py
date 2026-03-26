from django.db.models import Q
from django.core.files import File

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame, QDialog, QFileDialog, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate

from .models import *

from .pages.MainWindow import Ui_MainWindow
from .pages.Product import Ui_Product
from .pages.ProductsWindow import Ui_ProductsWindow
from .pages.ProductDialog import Ui_ProductDialog
from .pages.Order import Ui_Frame
from .pages.OrderDeteilsFrame import Ui_OrderDetailsFrame
from .pages.OrderDialog import Ui_OrderDialog
from .pages.OrdersWindow import Ui_OrdersWindow


import os

class Role:
    ADMIN = ("Администратор")
    MANAGER = ("Администратор", "Менеджер")
    
    @staticmethod
    def check_lvl(user:User |None):
        if user:
            if user.role in Role.ADMIN:
                return 2
            elif user.role in Role.MANAGER:
                return 1
        return 0 

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        
        self.ui = Ui_MainWindow()
        ui = self.ui
        
        ui.setupUi(self)
        
        ui.Login.setText("starka78@mail.ru")
        ui.Password.setText("9SdkLp012")
        
        ui.Guest.clicked.connect(self.open_products)
        ui.Enter.clicked.connect(self.enter)
        
    def enter(self):
        ui = self.ui
        login = ui.Login.text()
        password = ui.Password.text()
        
        if User.objects.filter(login = login, password = password).exists():
            self.open_products(User.objects.filter(login = login, password = password).first())
        else:
            QMessageBox.warning(self, "Ошибка","Такого пользователя не существует")
        
    def open_products(self, user : User | None = None):
        self.windows = ProductsWindow(user)
        self.windows.show()
        self.close()


class ProductFrame(QFrame):
    def __init__(self, product : Product, parents: "ProductsWindow") -> None:
        super(ProductFrame,self).__init__()
        
        self.ui = Ui_Product()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.product = product
        self.parents = parents
        
        ui.Type.setText(f"{product.type} | {product.name}")
        ui.Description.setText(ui.Description.text() + product.description)
        ui.Creator.setText(ui.Creator.text() + product.creator)
        ui.Seller.setText(ui.Seller.text() + product.seller)
        ui.Count.setText(ui.Count.text() + str(product.count))
        
        ui.Discount.setText(str(product.discount) + ui.Discount.text() )
        if product.discount > 0:
            ui.OldPrice.setText(str(product.price))
        else:
            ui.OldPrice.hide()
        ui.NewPrice.setText(str(product.price - (product.price * product.discount*0.01)))
        
        if product.discount > 15:
            ui.Discount.setStyleSheet("background-color:#2E8B57")
        else:
            ui.Discount.setStyleSheet("background-color:red")
        
        if product.count <=0:
            ui.Count.setStyleSheet("color:#aaa ")
        
        if product.image:
            pixmap = QPixmap(product.image.path)
            ui.image.setPixmap(pixmap)
            
        ui.Update.clicked.connect(self.update_product)
        ui.Delete.clicked.connect(self.delete_product)
        
        if Role.check_lvl(parents.user)< 2:
            ui.Update.hide()
            ui.Delete.hide()
        
    def delete_product(self):
        if QMessageBox.question(self, "Удаление", "Вы точно хотите удалить этот обьект?") == QMessageBox.Yes:
            if self.product.image:
                self.product.image.delete()
            self.product.delete()
        self.parents.initialize()
    
    def update_product(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.parents.initialize()

class ProductsWindow(QMainWindow):
    def __init__(self, user : User | None) -> None:
        super(ProductsWindow,self).__init__()
        
        self.ui = Ui_ProductsWindow()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.user = user
        
        if user:
            ui.FIO.setText(user.__str__())
        else:
            ui.FIO.setText("Гость")

        filters = ["Все поставщики", *list(set(i.seller for i in Product.objects.all()))]
        sort = ["По возрастанию", "По убыванию"]
        
        ui.comboBoxFilter.addItems(filters)
        ui.comboBoxSort.addItems(sort)
        
        
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.Search.textChanged.connect(self.initialize)
        
        ui.Exit.clicked.connect(self.exit)
        ui.CreateProduct.clicked.connect(self.create_product)
        ui.Orders.clicked.connect(self.open_orders)
        
        self.initialize()
        
        if Role.check_lvl(user)<2:
            ui.CreateProduct.hide()
        if Role.check_lvl(user)<1:
            ui.Orders.hide()
            while ui.horizontalLayout.layout().count():
                item = ui.horizontalLayout.layout().takeAt(0)
                try:
                    item.widget().deleteLater()
                except:
                    pass
                
        
    def initialize(self):
        ui = self.ui
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
            
        products = Product.objects.all()
            
        search = ui.Search.text().lower()
        sort = ui.comboBoxSort.currentText()
        filters = ui.comboBoxFilter.currentText()
        
        if filters != "Все поставщики":
            products =  products.filter(seller = filters)
            
        if sort == "По возрастанию":
            products = products.order_by("count")
        else:
            products = products.order_by("-count")
            
            
        if search.replace(" ","")!= "":
            products = products.filter(Q(type__icontains = search) 
                                       | Q(name__icontains =search)
                                       | Q(description__icontains =search)
                                       | Q(creator__icontains =search)
                                       | Q(seller__icontains =search)
                                       | Q(price__icontains =search)
                                       | Q(count__icontains =search)
                                       | Q(discount__icontains =search))
        
        
        
        
        
        for p in products:
            frame = ProductFrame(p,self)
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
            
    def create_product(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()
        
    def open_orders(self):
        self.windows = OrdersWindow(self.user)
        self.windows.show()
        self.close()
    
    def exit(self):
        self.windows = MainWindow()
        self.windows.show()
        self.close()


class OrderFrame(QFrame):
    def __init__(self, order : Order, parents: "OrdersWindow") -> None:
        super(OrderFrame,self).__init__()
        
        self.ui = Ui_Frame()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.order = order
        self.parents = parents
        
        ui.FIO.setText(order.user.__str__())
        ui.Status.setText(order.status)
        ui.Address.setText(order.order_location.address)
        ui.Date.setText(str(order.date))
        ui.DateDelivery.setText(str(order.date_delivery))
        
        for i in OrderDetails.objects.filter(order = order):
            ui.scrollAreaWidgetContents.layout().addWidget(QLabel(f"{i.product.article} | {i.product.name} | {i.count}"))
        ui.Status.setText(order.status)
        
        
        ui.Update.clicked.connect(self.update_order)
        ui.Delete.clicked.connect(self.delete_order)
        
        if Role.check_lvl(parents.user)< 2:
            ui.Update.hide()
            ui.Delete.hide()
        
    def delete_order(self):
        if QMessageBox.question(self, "Удаление", "Вы точно хотите удалить этот обьект?") == QMessageBox.Yes:
           
            self.order.delete()
        self.parents.initialize()
    
    def update_order(self):
        dialog = OrderDialog(self.order)
        dialog.exec()
        self.parents.initialize()

class OrdersWindow(QMainWindow):
    def __init__(self, user : User | None) -> None:
        super(OrdersWindow,self).__init__()
        
        self.ui = Ui_OrdersWindow()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.user = user
        
        if user:
            ui.FIO.setText(user.__str__())
        else:
            ui.FIO.setText("Гость")

        ui.Exit.clicked.connect(self.exit)
        ui.CreateOrder.clicked.connect(self.create_order)
        ui.Products.clicked.connect(self.open_products)
        if Role.check_lvl(user)<2:
            ui.CreateOrder.hide()
        self.initialize()
        
    def initialize(self):
        ui = self.ui
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
            
        orders = Order.objects.all()
            
        
        for o in orders:
            frame = OrderFrame(o,self)
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
            
    def create_order(self):
        dialog = OrderDialog()
        dialog.exec()
        self.initialize()
        
    def open_products(self):
        self.windows = ProductsWindow(self.user)
        self.windows.show()
        self.close()
    
    
    def exit(self):
        self.windows = MainWindow()
        self.windows.show()
        self.close()




class ProductDialog(QDialog):
    def __init__(self, product : Product| None = None) -> None:
        super(ProductDialog,self).__init__()
        
        self.ui = Ui_ProductDialog()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.product = product
        
        ui.comboBoxType.addItems(list(set(i.type for i in Product.objects.all())))
        ui.comboBoxCreator.addItems(list(set(i.creator for i in Product.objects.all())))
        ui.comboBoxSeller.addItems(list(set(i.seller for i in Product.objects.all())))
        
        if product:
            ui.Article.setText(product.article)
            ui.Name.setText(product.name)
            ui.Description.setText(product.description)
            
            ui.Price.setValue(product.price)
            ui.Count.setValue(product.count)
            ui.Discount.setValue(product.discount)
            
            ui.comboBoxType.setCurrentText(product.type)
            ui.comboBoxCreator.setCurrentText(product.creator)
            ui.comboBoxSeller.setCurrentText(product.seller)

            if product.image:
                ui.Path.setText(product.image.path)
                pixmap = QPixmap(product.image.path)
                ui.Image.setPixmap(pixmap)
        
        ui.OpenFile.clicked.connect(self.open_file)
        ui.Save.clicked.connect(self.save)
        
    def open_file(self):
        name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images *.jpeg *.jpg *.png")
        if name !="":
            
            self.ui.Path.setText(name)
            pixmap = QPixmap(name)
            self.ui.Image.setPixmap(pixmap)
        else:
            name = "./picture.png"
            self.ui.Path.setText("")
            pixmap = QPixmap(name)
            self.ui.Image.setPixmap(pixmap)
    
    def save(self):
        ui = self.ui
        article = ui.Article.text()
        name = ui.Name.text()
        type = ui.comboBoxType.currentText()
        description = ui.Description.text()
        creator = ui.comboBoxCreator.currentText()
        seller = ui.comboBoxSeller.currentText()
        price = ui.Price.value()
        count = ui.Count.value()
        discount = ui.Discount.value()
        
        path = ui.Path.text()
        
        if all([i.replace(" ", "") != "" for i in [article,name,type,description,creator,seller]]):
            if price != 0:
                if self.product:
                    p = self.product
                    p.article = article
                    p.name = name
                    p.type = type
                    p.description = description
                    p.creator = creator
                    p.seller = seller
                    p.price = price
                    p.count = count
                    p.discount = discount
                    
                    if path != "" and (not p.image or path != p.image.path) :
                        filename = os.path.basename(path)
                        
                        if filename.endswith((".png", ".jpg", ".jpeg")):
                            with open(path, 'rb') as f:
                                if p.image:
                                    p.image.delete()
                                p.image.save(filename,File(f), save=True)
                        else:
                            QMessageBox.warning(self, "Ошибка","Не верный формат изображения")
                    elif path == "" and p.image:
                        p.image.delete()
                    p.save()
                else:
                    p = Product()
                    p.article = article
                    p.name = name
                    p.type = type
                    p.description = description
                    p.creator = creator
                    p.seller = seller
                    p.price = price
                    p.count = count
                    p.discount = discount
                    
                    p.save_base()

                    if path != "" :
                        filename = os.path.basename(path)

                        if filename.endswith((".png", ".jpg", ".jpeg")):
                            with open(path, 'rb') as f:
                                p.image.save(filename,File(f), save=True)
                        else:
                            QMessageBox.warning(self, "Ошибка","Не верный формат изображения")
                    p.save()
                QMessageBox.information(self, "Успешно","Сохранено")
                self.close()
                
            else:
                QMessageBox.warning(self, "Ошибка","Цена не может быть ровна 0")
        else:
            QMessageBox.warning(self, "Ошибка","Не все поля заполнены")
            

class OrderDetailsFrame(QFrame):
    def __init__(self, product: Product, count: int, is_check:bool = False) -> None:
        super(OrderDetailsFrame,self).__init__()
        
        self.ui = Ui_OrderDetailsFrame()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.product = product
        ui.CheckBox.setText(product.article)
        ui.CheckBox.setChecked(is_check)
        ui.Num.setValue(count)
    
    def get_data(self):
        ui = self.ui
        return {"product": self.product, "status": ui.CheckBox.isChecked(), "count": ui.Num.value()}
        
        
        

class OrderDialog(QDialog):
    def __init__(self, order : Order| None = None) -> None:
        super(OrderDialog,self).__init__()
        
        self.ui = Ui_OrderDialog()
        ui = self.ui
        
        ui.setupUi(self)
        
        self.order = order
        
        ui.comboBoxFIO.addItems([i.__str__() for i in User.objects.all()])
        ui.comboBoxStatus.addItems(list(set([i.status for i in Order.objects.all()])))
        ui.comboBoxAddress.addItems([i.address for i in OrderLocation.objects.all()])
        
        active_cart = []
        products = Product.objects.all()
        
        if order:
            
            ui.comboBoxFIO.setCurrentText(order.user.__str__())
            ui.comboBoxStatus.setCurrentText(order.status)
            ui.comboBoxAddress.setCurrentText(order.order_location.address)
            
            ui.Date.setSelectedDate(QDate(*list(map(int, str(order.date).split("-")))))
            ui.DateDelivery.setSelectedDate(QDate(*list(map(int, str(order.date_delivery).split("-")))))
            
            active_cart = OrderDetails.objects.filter(order = order)
            
            
            
        for i in active_cart:
            ui.scrollAreaWidgetContents.layout().addWidget(OrderDetailsFrame(i.product, i.count, True))

        for p in products:
            if p not in [i.product for i in active_cart]:
                ui.scrollAreaWidgetContents.layout().addWidget(OrderDetailsFrame(p, 0))
        
        ui.Save.clicked.connect(self.save)
        

    def save(self):
        ui = self.ui
        FIO = ui.comboBoxFIO.currentText()
        status = ui.comboBoxStatus.currentText()
        address = ui.comboBoxAddress.currentText()
        
        date = ui.Date.selectedDate().toPython()
        dateDelivery = ui.DateDelivery.selectedDate().toPython()
        
        active_cart = []
        print(ui.scrollAreaWidgetContents.layout().count())
        for i in range(ui.scrollAreaWidgetContents.layout().count()):
            data = ui.scrollAreaWidgetContents.layout().itemAt(i).widget().get_data()
            if data["status"] == True:
                active_cart.append(data)
        if len(active_cart) == 0:
            if QMessageBox.question(self,"Внимание", "Если не выбран хотябы 1 продукт то заказ будет удален, вы хотите этого ?") == QMessageBox.Yes:
                if self.order:
                    self.order.delete()
                self.close()
        else:
            if self.order:
                o = self.order
                surname, name, patronymic = FIO.split(" ")
                o.user = User.objects.filter(surname = surname, name = name, patronymic = patronymic).first()
                o.status = status
                o.order_location = OrderLocation.objects.filter(address= address).first()
                o.date = date
                o.date_delivery = dateDelivery
                
                o.cart.clear()
                for i in active_cart:
                    if i["count"] > 0:
                        OrderDetails.objects.create(order = o, product = i["product"], count = i["count"])
                    
                
                o.save()
            else:
                o = Order()
                surname, name, patronymic = FIO.split(" ")
                o.user = User.objects.filter(surname = surname, name = name, patronymic = patronymic).first()
                o.status = status
                o.order_location = OrderLocation.objects.filter(address= address).first()
                o.date = date
                o.date_delivery = dateDelivery
                last = Order.objects.last()
                o.num = last.id + 1
                o.code = last.id +1 +100
                
                o.save_base()
                for i in active_cart:
                    if i["count"] > 0:
                        OrderDetails.objects.create(order = o, product = i["product"], count = i["count"])
                    
                
                o.save_base()
            QMessageBox.information(self, "Успешно","Сохранено")
            self.close()

