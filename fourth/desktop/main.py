from PySide6.QtCore import QEvent, QRect, QSize, Qt,QDate
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QMessageBox, QFrame, QDialog, QFileDialog, QLabel
from PySide6.QtGui import QPixmap
from .pages.MainWindow import Ui_MainWindow
from .pages.Product import Ui_Product
from .pages.ProductWindow import Ui_ProductWindow
from .pages.ProductDialog import Ui_ProductDialog
from .pages.Order import Ui_Order
from .pages.OrderWindow import Ui_OrderWindow
from .pages.OrderDialog import Ui_OrderDialog
from .pages.FrameOrderCount import Ui_FrameOrderCount
from .models import *
from django.db.models import Q
from django.core.files import File
import uuid
import os


class Rules:
    hight = ("Администратор")
    mid = ('Администратор', 'Менеджер')
    
    @staticmethod
    def check_lvl(user:User | None):
        if not user:
            return 0
        
        if user.role in Rules.hight:
            return 2
        elif user.role in Rules.mid:
            return 1
        else: return 0


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.Login.setText("94d5ous@gmail.com")
        ui.Password.setText("uzWC67")
        
        ui.Enter.clicked.connect(self.enter)
        ui.Guest.clicked.connect(self.open_products)
        
    def enter(self):
        ui = self.ui
        login = ui.Login.text()
        password = ui.Password.text()
        print(login,password)
        if User.objects.filter(email = login, password = password).exists():
            self.open_products(User.objects.filter(email = login, password = password).first())
        else:
            QMessageBox.warning(self, "Ошибка", "Такого пользовтаеля не существует")
            
    def open_products(self, user : User | None = None):
        self.products = ProductWindow(user)
        self.products.show()
        self.close()


class ProductFrame(QFrame):
    def __init__(self, product : Product, parents: "ProductWindow") -> None:
        super(ProductFrame,self).__init__()
        
        self.ui = Ui_Product()
        ui = self.ui
        ui.setupUi(self)
        
        self.product = product
        self.parents = parents
        
        ui.Type.setText(f"{product.type} | {product.name}")
        ui.Description.setText(ui.Description.text()+ product.description)
        ui.Creator.setText(ui.Creator.text()+ product.creator)
        ui.Seller.setText(ui.Seller.text()+ product.seller)
        
        ui.Counter.setText(ui.Counter.text()+ product.counter)
        ui.Count.setText(ui.Count.text()+ str(product.count))
        ui.Discount.setText( str(product.discount)+ui.Discount.text())


        if product.discount >0:
            ui.OldPrice.setText(str(product.price))
            ui.NewPrice.setText(str(product.price - (product.price * product.discount *0.01)))
        else :
            ui.NewPrice.setText(str(product.price))
            ui.OldPrice.deleteLater()

        if product.image:
            pixmap = QPixmap(product.image.path)
            ui.Image.setPixmap(pixmap)
            
        if Rules.check_lvl(parents.user) < 2:
            ui.Update.setHidden(True)
            ui.Delete.setHidden(True)
            
            
        ui.Update.clicked.connect(self.update_product)
        ui.Delete.clicked.connect(self.delete_product)
    
    def update_product(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.parents.initialize()

    def delete_product(self):
        if QMessageBox.question(self,"Удаление", "Вы действительно хотите удалить этот объект?") == QMessageBox.Yes:
            
            self.product.image.delete()
            self.product.delete()
            self.parents.initialize()

        

class ProductWindow(QMainWindow):
    def __init__(self, user : User | None) -> None:
        super(ProductWindow,self).__init__()
        
        self.ui = Ui_ProductWindow()
        ui = self.ui
        ui.setupUi(self)
        self.user = user
        if user:
            
            ui.FIO.setText(user.__str__())
        else: 

            ui.FIO.setText("Гость")
        
        ui.comboBoxSort.addItems(["По убыванию","По возрастанию"])
        ui.comboBoxFilter.addItems(["Все поставщики" , *list(set([ i.seller for i in Product.objects.all()]))])
        
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        ui.Search.textChanged.connect(self.initialize)
        
        self.initialize()
        
        ui.Exit.clicked.connect(self.exit)
        ui.CreateProduct.clicked.connect(self.create_product)
        ui.OpenOrders.clicked.connect(self.open_orders)
        
        if Rules.check_lvl(user) <2:
            ui.CreateProduct.setHidden(True)
        if Rules.check_lvl(user) <1:
            ui.OpenOrders.setHidden(True)
            while ui.horizontalLayout.layout().count():
                try:
                    ui.horizontalLayout.layout().takeAt(0).widget().deleteLater()
                except:
                    pass
        
    def initialize(self):
        ui = self.ui
        products = Product.objects.all()
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
        search = ui.Search.text().lower()
        sort = ui.comboBoxSort.currentText()
        filter = ui.comboBoxFilter.currentText()
        
        if search.replace(" ","") !="":
            products = products.filter(Q(article__icontains = search) | Q(name__icontains = search) | Q(price__icontains = search) | Q(seller__icontains = search) | Q(creator__icontains = search) | Q(type__icontains = search) | Q(discount__icontains = search) | Q(count__icontains = search) | Q(description__icontains = search))
        
        if sort == "По убыванию":
            products = products.order_by("-count")
        else:
            products = products.order_by("count")
            
        if filter != "Все поставщики":
            products = products.filter(seller = filter)
        
        for p in products:
            frame = ProductFrame(p, self)
            
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
        
    def create_product(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()
    
    def open_orders(self):
        self.main = OrderWindow(self.user)
        self.main.show()
        self.close()
    
    def exit(self):
        
        self.main = MainWindow()
        self.main.show()
        self.close()
      

class OrderFrame(QFrame):
    def __init__(self, order : Order, parents: "OrderWindow") -> None:
        super(OrderFrame,self).__init__()
        
        self.ui = Ui_Order()
        ui = self.ui
        ui.setupUi(self)
        
        self.order = order
        self.parents = parents
        
        ui.Article.setText(" ".join([f"{i.product} x{i.count}" for i in OrderDetails.objects.filter(order = order)]))
        ui.Status.setText(order.status)
        ui.Address.setText(order.location.address)
        ui.Date.setText(str(order.date))
        ui.DateDelivery.setText(str(order.dateDelivery))
        
        if Rules.check_lvl(parents.user) < 2:
            ui.Update.setHidden(True)
            ui.Delete.setHidden(True)
            
        ui.Update.clicked.connect(self.update_product)
        ui.Delete.clicked.connect(self.delete_product)
    
    def update_product(self):
        dialog = OrderDialog(self.parents.user,self.order)
        dialog.exec()
        self.parents.initialize()

    def delete_product(self):
        if QMessageBox.question(self,"Удаление", "Вы действительно хотите удалить этот объект?") == QMessageBox.Yes:

            self.order.delete()
            self.parents.initialize()

class OrderWindow(QMainWindow):
    def __init__(self, user : User | None) -> None:
        super(OrderWindow,self).__init__()
        
        self.ui = Ui_OrderWindow()
        ui = self.ui
        ui.setupUi(self)
        
        if user:
            self.user = user
            ui.FIO.setText(user.__str__())
        else: 
            ui.FIO.setText("Гость")
        
        
        
        self.initialize()
        
        ui.Exit.clicked.connect(self.exit)
        ui.AddOrder.clicked.connect(self.create_order)
        ui.Products.clicked.connect(self.open_products)
        if Rules.check_lvl(user) <2:
            ui.AddOrder.setHidden(True)
        
    def initialize(self):
        ui = self.ui
        products = Order.objects.all()
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
       
        
        for p in products:
            frame = OrderFrame(p, self)
            
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
        
    def create_order(self):
        dialog = OrderDialog(self.user)
        dialog.exec()
        self.initialize()
        
    
    def open_products(self):
        self.main = ProductWindow(self.user)
        self.main.show()
        self.close()
    
    def exit(self):
        
        self.main = MainWindow()
        self.main.show()
        self.close()

  
class ProductDialog(QDialog):
    
    def __init__(self, product : Product | None = None) -> None:
        super(ProductDialog,self).__init__()
        
        self.ui = Ui_ProductDialog()
        ui = self.ui
        ui.setupUi(self)
        
        ui.comboBoxType.addItems(list(set([i.type for i in Product.objects.all()])))
        ui.comboBoxCreator.addItems(list(set([i.creator for i in Product.objects.all()])))
        
        self.product = product
        if product:
            ui.Article.setText(product.article)
            ui.Name.setText(product.name)
            ui.Description.setText(product.description)
            ui.Seller.setText(product.seller)
            ui.Price.setText(str(product.price))
            ui.Counter.setText(product.counter)
            ui.Count.setText(str(product.count))
            ui.Discount.setText(str(product.discount))
            
            ui.comboBoxCreator.setCurrentText(product.creator)
            ui.comboBoxType.setCurrentText(product.type)
            
            
            if product.image:
                ui.Path.setText(product.image.path)
                ui.Image.setPixmap(QPixmap(product.image.path))
        
        ui.Save.clicked.connect(self.save)
        ui.OpenFile.clicked.connect(self.open_file)
    
    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Images *.png *.jpg *.jpeg")
        ui = self.ui
        if file != "":
            ui.Path.setText(file)
            ui.Image.setPixmap(QPixmap(file))
        else:
            ui.Path.setText("")
            ui.Image.setPixmap(QPixmap("./picture.png"))
    
    def save(self):
        ui = self.ui
        article = ui.Article.text()
        name = ui.Name.text()
        type = ui.comboBoxType.currentText()
        description = ui.Description.text()
        creator = ui.comboBoxCreator.currentText()
        price = ui.Price.text()
        counter = ui.Counter.text()
        count = ui.Count.text()
        discount = ui.Discount.text()
        path = ui.Path.text()
        
        if all([i.replace(" ","") !="" for i in [article,name,type,description,creator,price,count,counter,discount]]):
            try:
                count = int(count)
                price = int(price)
                discount = int(discount)
                
                if self.product:
                    p = self.product
                    p.article = article
                    p.name = name
                    p.type = type
                    p.description = description
                    p.creator = creator
                    p.price = price
                    p.counter = counter
                    p.count = count
                    p.discount = discount
                    
                    if not p.image or path != p.image.path:
                        filename = os.path.basename(path)
                        #Оптимально мало ли будут проверять
                        if filename.endswith((".png",".jpg",".jpeg")):

                            if p.image:
                                p.image.delete()
                            with open(path, 'rb') as f:
                                p.image.save(filename, File(f), save=True)
                        elif path.replace(" ", "") =="":
                            if p.image:
                                p.image.delete()
                                
                                
                    p.save()
                else:
                    p = Product()
                    p.article = article
                    p.name = name
                    p.type = type
                    p.description = description
                    p.creator = creator
                    p.price = price
                    p.counter = counter
                    p.count = count
                    p.discount = discount
                    
                    
                    p.save_base()
                    if path != "":
                        filename = os.path.basename(path)
                        #Оптимально мало ли будут проверять
                        if filename.endswith((".png",".jpg",".jpeg")):

                            with open(path, 'rb') as f:
                                p.image.save(filename, File(f), save=True)
                            p.save()
                self.close()
                
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Ошибка", "Не правильные типы данных")
        else:
            QMessageBox.warning(self, "Ошибка", "Не все поля заполнены")

class CartFrame(QFrame):
    def __init__(self, order : OrderDetails, parent_dialog: "OrderDialog") -> None:
        super(CartFrame,self).__init__()
        
        self.ui = Ui_FrameOrderCount()
        ui = self.ui
        ui.setupUi(self)
        
        self.order = order
        self.parent_dialog = parent_dialog
        
        ui.Article.setText(order.product.article)
        ui.Count.setValue(order.count)

        

        
    def get_data(self):
        return self.order.product.article, self.ui.Count.value()
    
    def mouseDoubleClickEvent(self, event):
        print("double click")
        self.parent_dialog.add_to_article(self)
    

class CustomLabel(QLabel):
    def __init__(self, product: Product, parent_dialog : "OrderDialog"):
        super().__init__(product.article)
        self.product = product
        self.parent_dialog = parent_dialog
        

    def mouseDoubleClickEvent(self, event):
        print("double click")
        self.parent_dialog.add_to_cart(self)

        
class OrderDialog(QDialog):
    def __init__(self, user : User , order : Order | None = None ) -> None:
        super(OrderDialog,self).__init__()
        
        self.ui = Ui_OrderDialog()
        ui = self.ui
        ui.setupUi(self)
        
        self.user = user
        
        
        ui.comboBoxStatus.addItems(["Готов", "Не готов"])
        ui.comboBoxAddress.addItems([i.address for i in OrderLocation.objects.all()])
        self.order = order
        
        products = Product.objects.all()
        cart = OrderDetails.objects.filter(order = order)
        
        if order:
            ui.comboBoxAddress.setCurrentText(order.location.address)
            ui.comboBoxStatus.setCurrentText(order.status)
            
            ui.Date.setSelectedDate(QDate(*list(map(int,str(order.date).split("-")))))
            ui.DateDelivery.setSelectedDate(QDate(*list(map(int,str(order.dateDelivery).split("-")))))
            
            products = products.exclude(article__in =[i.product.article for i in cart])

            for i in cart:
                ui.Cart.layout().addWidget(CartFrame(i, self))
        

        for i in products:
            ui.Articles.layout().addWidget(CustomLabel(i, self))   
            
            
        
        ui.Save.clicked.connect(self.save)
    
    def add_to_cart(self, label: CustomLabel):
        
        self.ui.Articles.layout().removeWidget(label)
        label.deleteLater()



        self.ui.Cart.layout().addWidget(
                CartFrame(OrderDetails(product = label.product, order = None, count = 1),self)
            )
    
    def add_to_article(self, label: CartFrame):
        
        self.ui.Cart.layout().removeWidget(label)
        label.deleteLater()



        self.ui.Articles.layout().addWidget(
                CustomLabel(label.order.product,self)
            )

    
    def save(self):
        ui = self.ui
        status = ui.comboBoxStatus.currentText()
        address = ui.comboBoxAddress.currentText()
        
        date = ui.Date.selectedDate().toPython()
        dateDelivery = ui.DateDelivery.selectedDate().toPython()

        o = None
        
        try:

            
            if self.order:
                o = self.order
                o.status = status
                o.location = OrderLocation.objects.filter(address = address).first()
                o.date = date
                o.dateDelivery = dateDelivery

                o.save()
            else:
                o = Order()
                o.status = status
                o.num = Order.objects.last().num + 1 if Order.objects.last() else 1
                o.location = OrderLocation.objects.filter(address = address).first()
                o.date = date
                o.dateDelivery = dateDelivery
                o.user = self.user
                o.code = Order.objects.last().code + 1 if Order.objects.last() else 1
                
                
                o.save_base()
                
            
            o.orders.clear()
            for i in range(ui.Cart.layout().count()):
                frame = ui.Cart.layout().itemAt(i).widget()
                product, count = frame.get_data()
                print(product)
                
                detail = OrderDetails.objects.get_or_create(order = o, product=Product.objects.get(article = product))[0]
                detail.count = count
                detail.save()
            
            if o.orders.count() ==0:
                o.delete()
            self.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Ошибка", "Ошибка, попробуйте позже")
