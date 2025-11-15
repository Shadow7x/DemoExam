from PySide6.QtWidgets import QMainWindow, QMessageBox, QFrame,QDialog, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate
from ..Pages.MainWindow import Ui_MainWindow
from ..Pages.Home import Ui_HomeWindow
from ..Pages.ProductFrame import Ui_ProductFrame
from ..Pages.Product import Ui_Product
from ..Pages.Order import Ui_OrderFrame
from ..Pages.OrdersList import Ui_OrderWindow
from ..Pages.OrderDialog import Ui_OrderDialog
from ..models import *
from django.db.models import Q
from django.core.files import File
import os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.enter)
        self.ui.Guest.clicked.connect(self.open_main)
        
    def enter(self):
        login = self.ui.Login.toPlainText()
        password = self.ui.Password.toPlainText()
        if User.objects.filter(email=login, password=password).exists():
            self.open_main(User.objects.filter(email=login, password=password).first())
        else:
            QMessageBox.warning(None, "Ошибка", "Такого пользователя не существует")
        
    def open_main(self, user = None):
        self.home = HomeWindow(user)
        self.home.show()
        self.close()


class ProductFrame(QFrame):
    def __init__(self,product:Product, parent: "HomeWindow") -> None:
        super(ProductFrame, self).__init__()
        self.ui = Ui_ProductFrame()
        self.product = product
        self.ui.setupUi(self)
        self.parents = parent
        
        self.ui.Name.setText(self.ui.Name.text() + f" {product.type} | {product.name}")
        self.ui.Description.setText(self.ui.Description.text() +product.description)
        self.ui.Creator.setText(self.ui.Creator.text() +product.creator)
        self.ui.Seller.setText(self.ui.Seller.text() +product.seller)
        self.ui.Price.setText(self.ui.Price.text() +str(product.price))
        self.ui.Counter.setText(self.ui.Counter.text() +product.counter)
        self.ui.Count.setText(self.ui.Count.text() +str(product.count))
        self.ui.Discount.setText(self.ui.Discount.text()+ " " +str(product.discount) +"%")
        
        if product.image:
            image = QPixmap(product.image.path)
            self.ui.Image.setPixmap(image)
        
        if product.discount >=15:
            self.ui.Discount.setStyleSheet("color:#2E8B57")
        
        if not parent.user or parent.user.role !="Администратор":
            self.ui.Update.setEnabled(False)
            self.ui.Delete.setEnabled(False)
        
        self.ui.Update.clicked.connect(self.open_update)
        self.ui.Delete.clicked.connect(self.delete)
        
    def open_update(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.parents.initialize()
    
    def delete(self):
        self.product.image.delete()
        self.product.delete()
        self.parents.initialize()

class OrderFrame(QFrame):
    def __init__(self, order:NewOrder, parent: "OrderWindow") -> None:
        super(OrderFrame, self).__init__()
        self.ui = Ui_OrderFrame()
        self.order = order
        self.ui.setupUi(self)
        self.parents = parent
        

        ui = self.ui
        ui.Article.setText(self.ui.Article.text() + f"{order.article.article}")
        ui.Status.setText(self.ui.Status.text() + f"{order.status}")
        ui.Address.setText(self.ui.Address.text() + f"{order.location.address}")
        ui.Date.setText(self.ui.Date.text() + f"{order.date}")
        ui.DateDelivery.setText(self.ui.DateDelivery.text() + f"{order.dateDelivery}")
        

        
        if not parent.user or parent.user.role !="Администратор":
            self.ui.Update.setEnabled(False)
            self.ui.Delete.setEnabled(False)
        
        self.ui.Update.clicked.connect(self.open_update)
        self.ui.Delete.clicked.connect(self.delete)
        
    def open_update(self):
        dialog = OrderDialog(self.order)
        dialog.exec()
        self.parents.initialize()
    
    def delete(self):
        self.order.delete()
        self.parents.initialize()
        
        
class OrderWindow(QMainWindow):        
    def __init__(self, user: User | None = None):
        super(OrderWindow, self).__init__()
        self.ui = Ui_OrderWindow()
        self.ui.setupUi(self)
        self.user = user
        
        if user:
            self.ui.User.setText(f"{user.surname} {user.name} {user.patronymic}")
        else:
            self.ui.User.setText("Гость")
            
        self.ui.Exit.clicked.connect(self.exit)
        self.orders = NewOrder.objects.all()
        
        self.ui.CreateOrder.clicked.connect(self.createOrder)
        self.ui.Orders.clicked.connect(self.openProducts)

        self.initialize()
    
        self.ui.CreateOrder.setEnabled(False)
        self.ui.Orders.setEnabled(False)
    
        if  user and user.role == "Администратор":
            self.ui.CreateOrder.setEnabled(True)
            self.ui.Orders.setEnabled(True)

        if  user and user.role == "Менеджер":

            self.ui.Orders.setEnabled(True)
        
        
    def initialize(self):
        self.orders = NewOrder.objects.all()
        layout = self.ui.scrollAreaWidgetContents.layout()
        while layout.count():
            item = layout.takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
        for i in self.orders:
            p_card = OrderFrame(i, self)
            self.ui.scrollAreaWidgetContents.layout().addWidget(p_card)
    
    def openProducts(self):
        self.Products= HomeWindow(self.user)
        self.Products.show()
        
        self.close()
    
    def createOrder(self):
        dialog = OrderDialog()
        dialog.exec()
        self.initialize()
    
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        
        self.close()

class HomeWindow(QMainWindow):
    def __init__(self, user: User | None = None):
        super(HomeWindow, self).__init__()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.user = user
        
        if user:
            self.ui.User.setText(f"{user.surname} {user.name} {user.patronymic}")
        else:
            self.ui.User.setText("Гость")
            
        self.ui.Exit.clicked.connect(self.exit)
        self.products = Product.objects.all()
        
        self.sort = ["По возрастанию","По убыванию"]
        self.ui.comboBoxSort.addItems(self.sort)
        self.ui.comboBoxSort.currentIndexChanged.connect(self.initialize)
        
        self.sellers = ["Все поставщики"]
        for i in self.products:
            if i.seller not in self.sellers:
                self.sellers.append(i.seller)
        self.ui.comboBoxFilter.addItems(self.sellers)
        self.ui.comboBoxFilter.currentIndexChanged.connect(self.initialize)
        self.ui.Search.textChanged.connect(self.initialize)
        
        self.ui.CreateProduct.clicked.connect(self.createProduct)
        self.ui.Orders.clicked.connect(self.openOrders)

        self.initialize()
        
        self.ui.CreateProduct.setEnabled(False)
        self.ui.Orders.setEnabled(False)
    
        if  user and user.role == "Администратор":
            self.ui.CreateProduct.setEnabled(True)
            self.ui.Orders.setEnabled(True)

        if  user and user.role == "Менеджер":

            self.ui.Orders.setEnabled(True)
            
    def initialize(self):
        self.products = Product.objects.all()
        layout = self.ui.scrollAreaWidgetContents.layout()
        while layout.count():
            item = layout.takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
                


        search = self.ui.Search.text().lower()
        if search !="":
            self.products = self.products.filter(Q(type__icontains =search) | Q(name__icontains =search) | Q(description__icontains =search) |Q(seller__icontains =search) | Q(creator__icontains =search) |Q(counter__icontains =search))
        
        sort = self.ui.comboBoxSort.currentText()

        
        
        filter = self.ui.comboBoxFilter.currentText()
        if filter != "Все поставщики":
            self.products = self.products.filter(seller = filter)
        
        if sort == "По возрастанию":
            self.products = self.products.order_by("count")
        else:
            self.products = self.products.order_by("-count")
        
        for i in self.products:
            p_card = ProductFrame(i, self)
            self.ui.scrollAreaWidgetContents.layout().addWidget(p_card)
            
        
    def openOrders(self):
        self.Orders= OrderWindow(self.user)
        self.Orders.show()
        
        self.close()
    
    def createProduct(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()
    
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        
        self.close()

class ProductDialog(QDialog):
        def __init__(self, product: Product | None = None):
            super(ProductDialog, self).__init__()
            self.ui = Ui_Product()
            self.ui.setupUi(self)
            ui =self.ui
            self.product = product
            self.ui.ChooseFile.clicked.connect(self.choose_file)
            if product:
                ui.Name.setText(product.name)
                ui.Type.setText(product.type)
                ui.Article.setText(product.article)
                ui.Price.setText(str(product.price))
                ui.Counter.setText(product.counter)
                ui.Seller.setText(product.seller)
                ui.Creator.setText(product.creator)
                ui.Discount.setText(str(product.discount))
                ui.Count.setText(str(product.count))
                ui.Description.setText(product.description)
                
                if product.image:
                    print(product.image.path)
                    img = QPixmap(product.image.path)
                    ui.Image.setPixmap(img)
                    ui.Path.setText(product.image.path)
            
            ui.Button.clicked.connect(self.updateDB)
        
        def choose_file(self):
            file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Images *.png *.jpg *.jpeg")
            self.ui.Path.setText(file_path)
            new_img = QPixmap(file_path)
            
            self.ui.Image.setPixmap(new_img)
            
        def updateDB(self):
            ui = self.ui
            name = ui.Name.text()
            type = ui.Type.text()
            article = ui.Article.text()
            price = ui.Price.text()
            counter = ui.Counter.text()
            seller = ui.Seller.text()
            creator = ui.Creator.text()
            discount = ui.Discount.text()
            count = ui.Count.text()
            description = ui.Description.text()
            file = ui.Path.text()
            
            if any([i.replace(" ","") == "" for i in [name, type, article, price,counter,seller,creator,discount,count,description]]) :
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
            else:
                try:
                    price = int(price)
                    discount = int(discount)
                    count = int(count)
                    if all([i>=0 for i in [price, discount, count]]):
                        if self.product:
                            if self.product.image:
                                self.product.image.delete()
                                
                            if file:
                                filename = os.path.basename(file)
                                with open(file, 'rb') as f:
                                    self.product.image.save(filename, File(f), save=True)
                            else:
                                self.product.image = None
                            self.product.name = name
                            self.product.type = type
                            self.product.article = article
                            self.product.price = price
                            self.product.counter = counter
                            self.product.seller = seller
                            self.product.creator = creator
                            self.product.discount = discount
                            self.product.count = count
                            self.product.description = description
                            
                            self.product.save()
                            self.close()
                        else:
                            self.product = Product.objects.create(name = name, type = type, article = article, price = price, counter = counter, seller = seller, creator = creator, discount = discount, count = count,description = description) 
                            if file:
                                filename = os.path.basename(file)
                                with open(file, 'rb') as f:
                                    self.product.image.save(filename, File(f), save=True)
                            else:
                                self.product.image = None
                            self.product.save()
                            self.close()
                            
                    else:
                        QMessageBox.warning(self, "Ошибка", "Значения должны быть больше или ровны 0")
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "Ошибка", "Неправльный тип данных")


class OrderDialog(QDialog):
    def __init__(self, order: NewOrder | None = None):
        super(OrderDialog, self).__init__()
        self.ui = Ui_OrderDialog()
        self.ui.setupUi(self)
        ui = self.ui
        self.order = order
        
        products = Product.objects.all()
        for i in products:
            ui.comboBoxProducts.addItem(i.article)
        statuses = ["Завершен","Новый"]
        ui.comboBoxStatus.addItems(statuses)
        locations = OrderLocation.objects.all()
        for i in locations:
            ui.comboBoxAddress.addItem(i.address)
            
        if order:
            ui.comboBoxProducts.setCurrentText(order.article.article)
            ui.comboBoxStatus.setCurrentText(order.status)
            ui.comboBoxAddress.setCurrentText(order.location.address)
            ui.Date.setSelectedDate(QDate(*list(map(int,str(order.date).split("-")))))
            ui.DateDelivery.setSelectedDate(QDate(*list(map(int,str(order.dateDelivery).split("-")))))
            

        
        ui.Button.clicked.connect(self.updateDB)
    

        
    def updateDB(self):
        ui = self.ui
        product = Product.objects.filter(article = ui.comboBoxProducts.currentText()).first()
        status = ui.comboBoxStatus.currentText()
        address = OrderLocation.objects.filter(address = ui.comboBoxAddress.currentText()).first()
        date = ui.Date.selectedDate().toPython()
        dateDelivery = ui.DateDelivery.selectedDate().toPython()
        print(date)
        

        try:
            if self.order:

              
                self.order.article = product
                self.order.status = status
                self.order.location = address
                self.order.date = date
                self.order.dateDelivery = dateDelivery
                
                
                self.order.save()
                self.close()
            else:
                self.order = NewOrder.objects.create(article = product, status = status, location = address, date = date, dateDelivery = dateDelivery) 

                self.close()
                    
            
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Ошибка", f"{e}")
            