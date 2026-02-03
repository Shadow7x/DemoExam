from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QMessageBox, QFrame, QDialog, QFileDialog
from PySide6.QtGui import QPixmap
from .pages.MainWindow import Ui_MainWindow
from .pages.HomeWindow import Ui_HomeWindow
from .pages.Product import Ui_Product
from .pages.ProductDialog import Ui_ProductDialog
from .models import *
from django.db.models import Q
from django.core.files import File
import os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.Login.setText("94d5ous@gmail.com")
        ui.Password.setText("uzWC67")
        
        ui.Enter.clicked.connect(self.enter)
        
        ui.Guest.clicked.connect(self.openHome)
    
    def enter(self):
        ui = self.ui
        login = ui.Login.text()
        password = ui.Password.text()
        
        if User.objects.filter(email = login,password = password).exists():
            self.openHome(User.objects.filter(email = login,password = password).first())
        else:
            QMessageBox.warning(self, "Ошибка", "Такого пользователя не существует")
    
    def openHome(self, user: User| None = None):
        self.home = HomeWindow(user)
        self.home.show()
        self.close()

class ProductFrame(QFrame):
    def __init__(self,product:Product,parent: "HomeWindow") -> None:
        super(ProductFrame,self).__init__()
        self.ui = Ui_Product()
        ui = self.ui
        ui.setupUi(self)
        self.main = parent
        
        self.product = product
        
        ui.Name.setText(f"{product.type} | {product.name}")
        ui.Description.setText(ui.Description.text()  + product.description)
        ui.Creator.setText(ui.Creator.text()  + product.creator)
        ui.Seller.setText(ui.Seller.text()  + product.seller)
        ui.Price.setText(ui.Price.text()  + str(product.price))
        ui.Counter.setText(ui.Counter.text()  + product.counter)
        ui.Count.setText(ui.Count.text()  + str(product.count))
        ui.Discount.setText(str(product.discount)+ ui.Discount.text())
        
        if product.image:
            image = QPixmap(product.image.path)
            ui.Image.setPixmap(image)

        if product.count<=0:
            ui.Name.setStyleSheet("color:blue")
        elif product.discount> 15:
            ui.Name.setStyleSheet("color:#2E8B57")
            
        ui.Update.clicked.connect(self.updateProduct)
        ui.Delete.clicked.connect(self.deleteProduct)
    
    def updateProduct(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.main.initialize()
        
    def deleteProduct(self):
        if QMessageBox.Yes == QMessageBox.question(self, "Внимание", "Вы уверены что хотите удалить это?"):
            self.product.delete()
        self.main.initialize()
        

class HomeWindow(QMainWindow):
    def __init__(self,user:User| None = None) -> None:
        super(HomeWindow,self).__init__()
        self.ui = Ui_HomeWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.Exit.clicked.connect(self.exit)
        
        ui.FIO.setText(f"{user.surname} {user.name} {user.patronymic}" if user else "Гость")
        
        sorting = ["По возрастанию", "По убыванию"]
        filtering = ["Все поставщики", *list(set([i.seller for i in Product.objects.all()]))]
        
        ui.comboBoxSort.addItems(sorting)
        ui.comboBoxFilter.addItems(filtering)
        
        
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        ui.Search.textChanged.connect(self.initialize)
        
        ui.CreateProduct.clicked.connect(self.createProduct)
        
        self.initialize()
        
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
        filter = ui.comboBoxFilter.currentText()
        sort = ui.comboBoxSort.currentText()
        
        if search.replace(" ", "") != "":
            products = products.filter(Q(name__icontains=search) | Q(type__icontains=search)| Q(description__icontains=search)| Q(creator__icontains=search)| Q(seller__icontains=search)| Q(price__icontains=search)| Q(counter__icontains=search)| Q(count__icontains=search)| Q(discount__icontains=search))
        
        if filter != "Все поставщики":
            products = products.filter(seller = filter)
        
        if sort == "По возрастанию":
            products = products.order_by("count")
        else:
            products = products.order_by("-count")
            
        
        for i in products:
            widget = ProductFrame(i,self)
            ui.scrollAreaWidgetContents.layout().addWidget(widget) 
        
    
    def createProduct(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()
    
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()




class ProductDialog(QDialog):
    def __init__(self,product:Product| None = None) -> None:
        super(ProductDialog,self).__init__()
        self.ui = Ui_ProductDialog()
        ui = self.ui
        ui.setupUi(self)
        self.product= product
        
        types = list(set([i.type for i in Product.objects.all()]))
        creators = list(set([i.creator for i in Product.objects.all()]))
        
        ui.comboBoxType.addItems(types)
        ui.comboBoxCreator.addItems(creators)
        
        if product:
            ui.Article.setText(product.article)
            ui.Name.setText(product.name)
            ui.Description.setText(product.description)
            ui.Seller.setText(product.seller)
            ui.Price.setText(str(product.price))
            ui.Counter.setText(product.counter)
            ui.Count.setText(str(product.count))
            ui.Discount.setText(str(product.discount))
            
            
            ui.comboBoxType.setCurrentText(product.type)
            ui.comboBoxCreator.setCurrentText(product.creator)
            
            if product.image:
                ui.Path.setText(product.image.path)
                image = QPixmap(product.image.path)
                ui.Image.setPixmap(image)
        
        ui.Save.clicked.connect(self.save)
        ui.OpenFile.clicked.connect(self.openFile)
        
    def openFile(self):
        file,_ = QFileDialog.getOpenFileName(self, "Выберите изображение","", "Images *.png *.jpeg *.jpg")
        
        if file !="":
            self.ui.Path.setText(file)
            image = QPixmap(file)
            self.ui.Image.setPixmap(image)
        else:
            self.ui.Path.setText(file)
            image = QPixmap("D:/time/import/picture.png")
            self.ui.Image.setPixmap(image)
    
    def save(self):
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
        
        if all([i.replace(" ", "") != '' for i in [article, name,type,description,creator,seller,price,counter,count,discount]]):
            try:
                price = int(price)
                count = int(count)
                discount = int(discount)
                
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
                    p.discount = discount
                    
                    if path != "":
                        file_name = os.path.basename(path)
                        with open(file_name,'rb') as f:
                            p.image.delete()
                            p.image.save(file_name, File(f),save = True)
                    p.save()
                else:
                    p = Product.objects.create(article = article, name = name, type = type, description = description, creator = creator, seller = seller, price = price, counter = counter ,count = count, discount = discount)
                    
                    if path != "":
                        file_name = os.path.basename(path)
                        with open(file_name,'rb') as f:

                            p.image.save(file_name, File(f),save = True)
                    p.save()
                    
                self.close()
                
            except Exception as e:
                print(e)
                QMessageBox.warning(self,"Ошибка", "Неверные типы данных")
        else:
            QMessageBox.warning(self,"Ошибка", "Не все поля заполнены")