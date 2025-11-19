from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QMessageBox, QFrame, QDialog, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate
from .pages.MainWindow import Ui_MainWindow
from .pages.HomeWindow import Ui_HomeWindow
from .pages.Product import Ui_Product
from .pages.ProductDialog import Ui_ProductDialog
from .pages.Order import Ui_Order
from .pages.OrderWindow import Ui_OrderWindow
from .pages.OrderDialog import Ui_OrderDialog
from django.db.models import Q
from django.core.files import File
from desktop.models import *
import os


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ui = self.ui
        
        ui.Email.setText("94d5ous@gmail.com")
        ui.Password.setText("uzWC67")
        
        ui.Enter.clicked.connect(self.enter)
        ui.Guest.clicked.connect(self.openHome)
    
    def enter(self):
        ui = self.ui
        email = ui.Email.text()
        password = ui.Password.text()
        
        if User.objects.filter(email = email, password = password).exists():
            self.openHome(User.objects.filter(email = email, password = password).first())
        else:
            QMessageBox.warning(self, "Ошибка", "Такого пользователя не существет")
    
    
    def openHome(self, user:User| None = None):
        self.home = HomeWindow(user)
        self.home.show()
        
        self.close()
        

class ProductFrame(QFrame):
    def __init__(self, product:  Product, parent: "HomeWindow") -> None:
        super(ProductFrame, self).__init__()
        self.ui = Ui_Product()
        self.ui.setupUi(self)
        ui = self.ui
        self.main = parent
        self.product = product
        
        ui.Name.setText(f"{product.type} | {product.name}")
        ui.Description.setText(ui.Description.text()+str(product.description))
        ui.Creator.setText(ui.Creator.text()+product.creator)
        ui.Seller.setText(ui.Seller.text()+product.seller)
        ui.Price.setText(ui.Price.text()+str(product.price))
        ui.Counter.setText(ui.Counter.text()+product.counter)
        ui.Count.setText(ui.Count.text()+str(product.count))
        ui.Discount.setText(str(product.discount)+ui.Discount.text())
        if product.count ==0:
            ui.Name.setStyleSheet("color:blue")
        
        elif product.discount>15:
            ui.Name.setStyleSheet("color:#2E8B57")
        
        if product.image:
            image = QPixmap(product.image.path)
            ui.label.setPixmap(image)
            
        ui.Update.clicked.connect(self.updateProduct)
        ui.Delete.clicked.connect(self.delete)
        
    def updateProduct(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.main.initialize()
        
    def delete(self):
        self.product.delete()
        self.main.initialize()
        
        



class HomeWindow(QMainWindow):
    def __init__(self, user : None | User = None) -> None:
        super(HomeWindow, self).__init__()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        ui = self.ui
        
        self.user = user
        
        ui.FIO.setText(f"{user.surname} {user.name} {user.patronymic}" if user else "Гость")
        
        ui.Exit.clicked.connect(self.exit)
        
        ui.Search.textChanged.connect(self.initialize)
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        
        sorts = ["По возрастанию", "По убыванию"]
        filters = ["Все поставщики", *list(set( [i.seller for i in Product.objects.all()]))]
        
        ui.comboBoxSort.addItems(sorts)
        ui.comboBoxFilter.addItems(filters)
        
        ui.AddProduct.clicked.connect(self.addProduct)
        
        ui.Orders.clicked.connect(self.openOrders)
        
        self.initialize()
        
        
    def initialize(self):
        products = Product.objects.all()
        ui = self.ui
        
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
        search = ui.Search.text().lower()
        sort = ui.comboBoxSort.currentText()
        filter = ui.comboBoxFilter.currentText()
        
        if search!= "":
            products =products.filter(Q(type__icontains=search) | Q(name__icontains=search) | Q(description__icontains=search) | Q(seller__icontains=search) | Q(creator__icontains=search) | Q(price__icontains=search) | Q(counter__icontains=search) | Q(count__icontains=search) | Q(discount__icontains=search))
        
        if sort == "По возрастанию":
            products = products.order_by("count")
        else:
            products = products.order_by("-count")
        
        if filter!= "Все поставщики":
            products = products.filter(seller =filter)
        
        for i in products:
            frame = ProductFrame(i,self)
            self.ui.scrollAreaWidgetContents.layout().addWidget(frame)
    
    def addProduct(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()
        
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
    
    def openOrders(self):
        self.orders = OrderWindow(self.user)
        self.orders.show()
        self.close()


class OrderFrame(QFrame):
    def __init__(self, order:  NewOrder, parent: "OrderWindow") -> None:
        super(OrderFrame, self).__init__()
        self.ui = Ui_Order()
        self.ui.setupUi(self)
        ui = self.ui
        self.main = parent
        self.order = order
        
        ui.Article.setText(ui.Article.text()+ order.article.article)
        ui.Status.setText(ui.Status.text()+ order.status)
        ui.Location.setText(ui.Location.text()+ order.location.address)
        ui.date.setText(ui.date.text()+ str(order.date))
        ui.DateDelivery.setText(ui.DateDelivery.text()+ str(order.dateDelivery))
        

            
        ui.Update.clicked.connect(self.updateProduct)
        ui.Delete.clicked.connect(self.delete)
        
    def updateProduct(self):
        dialog = OrderDialog(self.order)
        dialog.exec()
        self.main.initialize()
        
    def delete(self):
        self.order.delete()
        self.main.initialize()

class OrderWindow(QMainWindow):
    def __init__(self, user : None | User = None) -> None:
        super(OrderWindow, self).__init__()
        self.ui = Ui_OrderWindow()
        self.ui.setupUi(self)
        ui = self.ui
        
        self.user = user
        
        ui.FIO.setText(f"{user.surname} {user.name} {user.patronymic}" if user else "Гость")
        
        ui.Exit.clicked.connect(self.exit)
       
       
        ui.AddOrder.clicked.connect(self.addOrder)
        
        ui.Products.clicked.connect(self.openProducts)
        
        self.initialize()
        
        
    def initialize(self):
        orders = NewOrder.objects.all()
        ui = self.ui
        
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
        
        for i in orders:
            frame = OrderFrame(i,self)
            self.ui.scrollAreaWidgetContents.layout().addWidget(frame)
    
    def addOrder(self):
        dialog = OrderDialog()
        dialog.exec()
        self.initialize()
        
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
    
    def openProducts(self):
        self.orders = HomeWindow(self.user)
        self.orders.show()
        self.close()




class ProductDialog(QDialog):
    def __init__(self, product : None | Product = None) -> None:
        super(ProductDialog, self).__init__()
        self.ui = Ui_ProductDialog()
        self.ui.setupUi(self)
        ui = self.ui
        self.product =product
        p = product
        products = Product.objects.all()
        types = set([i.type for i in products])
        creators = set([i.creator for i in products])
        
        ui.comboBoxType.addItems(types)
        ui.comboBoxCreator.addItems(creators)
        
        if product:
            ui.Article.setText(p.article)
            ui.Name.setText(p.name)

            ui.Description.setText(p.description)
            
            ui.Seller.setText(p.seller)
            ui.Price.setText(str(p.price))
            ui.Counter.setText(p.counter)
            ui.Count.setText(str(p.count))
            ui.Discount.setText(str(p.discount))
            if p.image:
                ui.Path.setText(p.image.path)
            
            
            
            ui.comboBoxCreator.setCurrentText(p.creator)
            ui.comboBoxType.setCurrentText(p.type)
        
        ui.Save.clicked.connect(self.saveProduct)
        
        ui.OpenImage.clicked.connect(self.choose_file)
        
    def choose_file(self):
        file, _ = QFileDialog.getOpenFileName(self,"Выберите изображение", "", "Images *.png *jpg *.jpeg")
        newImage = QPixmap(file)
        self.ui.Path.setText(file)
        self.ui.Image.setPixmap(newImage)
        
    
    def saveProduct(self):
        ui = self.ui
        
        article = ui.Article.text()
        name = ui.Name.text()
        type = ui.comboBoxType.currentText()
        description = ui.Description.text()
        creator = ui.comboBoxCreator.currentText()
        seller = ui.Seller.text()
        price = ui.Price.text()
        counter = ui.Counter.text()
        count = ui.Count.text()
        discount = ui.Discount.text()
        path = ui.Path.text()
        
        if not all([i.replace(" ", "")=="" for i in [article,name,type,creator,seller,price,count,counter,discount]]):
            
            try:
                price = int(price)
                discount = int(discount)
                count = int(count)
                if self.product:
                    p =self.product
                    
                    p.article = article
                    p.name = name
                    p.type = type
                    p.description = description
                    p.creator = creator
                    p.seller = seller
                    p.price = price
                    p.counter = counter
                    p.count = count
                    p.discount= discount
                    if path !="":
                        fileName= os.path.basename(path)
                        with open(path, 'rb') as f:
                            p.image.delete()
                            p.image.save(fileName, File(f, fileName),save=True)
                
                    p.save()
                    
                else:
                    new =Product.objects.create(article = article, name = name, type = type,description = description,creator = creator,seller = seller,price = price,counter = counter,count = count,discount= discount)
                    if path !="":
                        fileName= os.path.basename(path)
                        with open(path, 'rb') as f:

                            new.image.save(fileName, File(f, fileName),save=True)
                        new.save()
                    
                self.close()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Ошибка", "Неверный тип данных")
        else:
            QMessageBox.warning(self, "Ошибка", "Не все поля заполнены")
            

class OrderDialog(QDialog):
    def __init__(self, order : None | NewOrder = None) -> None:
        super(OrderDialog, self).__init__()
        self.ui = Ui_OrderDialog()
        self.ui.setupUi(self)
        ui = self.ui
        self.order =order

        products = Product.objects.all()
        articles = [i.article for i in products]
        statuses = ["Завершен", "Новый"]
        locations = [i.address for i in OrderLocation.objects.all()]
        
        ui.comboBoxLocation.addItems(locations)
        ui.comboBoxArticle.addItems(articles)
        ui.comboBoxStatus.addItems(statuses)
        
        
        if order:
            ui.comboBoxArticle.setCurrentText(order.article.article)
            ui.comboBoxStatus.setCurrentText(order.status)
            ui.comboBoxLocation.setCurrentText(order.location.address)
            
            ui.Date.setSelectedDate(QDate(*list(map(int,str(order.date).split("-")))))
            ui.Date.setSelectedDate(QDate(*list(map(int,str(order.dateDelivery).split("-")))))
        
        ui.Save.clicked.connect(self.saveOrder)

    def saveOrder(self):
        ui = self.ui
        
        article = ui.comboBoxArticle.currentText()
        status =  ui.comboBoxStatus.currentText()
        location = ui.comboBoxLocation.currentText()
        date = ui.Date.selectedDate().toPython()
        dateDelivery = ui.DateDelivery.selectedDate().toPython()

            
        try:
            if self.order:
                o =self.order
                
                o.article = Product.objects.filter(article = article).first()
                o.status = status
                o.location = OrderLocation.objects.filter(address = location).first()
                o.date = date
                o.dateDelivery = dateDelivery
                o.save()
                
            else:
                new =NewOrder.objects.create(article = Product.objects.filter(article = article).first(), status = status, location = OrderLocation.objects.filter(address = location).first(), date = date,dateDelivery = dateDelivery)
                
            self.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Ошибка", "Ошибка при создании")

        
            