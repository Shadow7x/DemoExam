from PySide6.QtWidgets import QMainWindow, QMessageBox,QFrame, QDialog, QFileDialog
from PySide6.QtGui import QPixmap

from .pages.MainWindow import Ui_MainWindow
from .pages.ProductFrame import Ui_ProductFrame
from .pages.ProductWindow import Ui_ProductWindow
from .pages.ProductDialog import Ui_ProductDialog

from .models import *

from django.db.models import Q
from django.core.files import File

import os

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
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
        if User.objects.filter(login = login,password=password).exists():
            self.open_products(User.objects.filter(login = login,password=password).first())
        else: QMessageBox.warning(self,"Ошибка", "Такого пользователя не существует")
    def open_products(self, user: User| None = None):
        self.windows = ProductWindow(user)
        self.windows.show()
        self.close()
        
        
class ProductsFrame(QFrame):
    def __init__(self,product:Product, parents:"ProductWindow") -> None:
        super(ProductsFrame, self).__init__()
        self.ui = Ui_ProductFrame()
        ui = self.ui
        ui.setupUi(self)
        
        self.product = product
        self.parents = parents
        
        ui.Article.setText(f"{product.type} | {product.name}")
        ui.Description.setText(f"{ui.Description.text()} {product.description}")
        ui.Creator.setText(f"{ui.Creator.text()} {product.creator}")
        ui.Seller.setText(f"{ui.Seller.text()} {product.seller}")
        
        ui.Count.setText(f"{ui.Count.text()} {product.count}")
        ui.Discount.setText(f"{product.discount} {ui.Discount.text()}")
        
        if product.discount > 15:
            ui.Discount.setStyleSheet("background-color:#2E8B57")
        else:
            ui.Discount.setStyleSheet("background-color:red")
        
        if product.discount > 0:
            ui.Price.setText(f"{product.price}")
            ui.NewPrice.setText(f"{product.price - (product.price * product.discount *0.01)}")
        else:
            ui.Price.hide()
            ui.NewPrice.setText(f"{product.price}")
        
        if product.count ==0:
            ui.Count.setStyleSheet("color:#aaa")
        
        
        if product.image:
            pixmap = QPixmap(product.image.path)
            ui.Image.setPixmap(pixmap)
            
        ui.Update.clicked.connect(self.update_product)
        ui.Delete.clicked.connect(self.delete_product)
        
    def update_product(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        self.parents.initialize()
    
    def delete_product(self):
        if QMessageBox.question(self, "Удаление", "Вы уверены что хотите удолить этот продукт?") == QMessageBox.Yes:
            if self.product.image:
                self.product.image.delete()
            self.product.delete()
            self.parents.initialize()
        
class ProductWindow(QMainWindow):
    def __init__(self,user:User|None) -> None:
        super(ProductWindow, self).__init__()
        self.ui = Ui_ProductWindow()
        ui = self.ui
        ui.setupUi(self)
        
        self.user = user
              
        ui.FIO.setText(user.__str__() if user else "Гость")
        
        ui.Exit.clicked.connect(self.exit)

        ui.comboBoxSort.addItems(["по возрастанию","по убыванию"])
        ui.comboBoxFilter.addItems(["Все поставщики", *list(set([i.seller for i in Product.objects.all()]))])
        
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.Search.textChanged.connect(self.initialize)
        
        self.initialize()
        
        ui.AddProducts.clicked.connect(self.create_product)
        
    def initialize(self):
        ui = self.ui
        layout = ui.scrollAreaWidgetContents.layout()
        while layout.count():
            item = layout.takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
            
        products = Product.objects.all()
        
        search = ui.Search.text().lower()
        filters = ui.comboBoxFilter.currentText()
        sort = ui.comboBoxSort.currentText()
        
        if sort == "по возрастанию":
            products = products.order_by("count")
        else:
            products = products.order_by("-count")
            
        if filters != "Все поставщики":
            products = products.filter(seller =filters)
        
        if search.replace(" ", "")!= "":
            products = products.filter(Q(article__icontains = search)
                                       | Q(name__icontains = search)
                                       | Q(price__icontains = search)
                                       | Q(seller__icontains = search)
                                       | Q(creator__icontains = search)
                                       | Q(type__icontains = search)
                                       | Q(discount__icontains = search)
                                       | Q(count__icontains = search)
                                       | Q(description__icontains = search)
                                       )
        
        
        for i in products:
            frame = ProductsFrame(i,self)
            layout.addWidget(frame)
    
    
    def create_product(self):
        dialog = ProductDialog()
        dialog.exec()
        self.initialize()

        
    def exit(self):
        self.windows = MainWindow()
        self.windows.show()
        self.close()
        

class ProductDialog(QDialog):
    def __init__(self, product:Product|None = None) -> None:
        super(ProductDialog, self).__init__()
        self.ui = Ui_ProductDialog()
        ui = self.ui
        ui.setupUi(self)

        self.product = product
        
        ui.comboBoxType.addItems(list(set([i.type for i in Product.objects.all()])))
        ui.comboBoxSeller.addItems(list(set([i.creator for i in Product.objects.all()])))
        ui.comboBoxCreator.addItems(list(set([i.seller for i in Product.objects.all()])))
        
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
                pixmap = QPixmap(product.image.path)
                ui.Image.setPixmap(pixmap)
                ui.Path.setText(product.image.path)
            
        ui.ChooseFile.clicked.connect(self.choose_file)
        
        ui.Save.clicked.connect(self.save)
        
    
    def choose_file(self):
        file,_ = QFileDialog.getOpenFileName(self,"Выберите файл", "", "Images *.jpg *.jpeg *.png")
        if file != "":
            pixmap = QPixmap(file)
            self.ui.Image.setPixmap(pixmap)
            self.ui.Path.setText(file)
        elif file == "":
            pixmap = QPixmap("./picture.png")
            self.ui.Image.setPixmap(pixmap)
            self.ui.Path.setText(file)
    
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
        
        if not all([i.replace(" ", "")=="" for i in [article,name,type,description,creator,seller]]):
            
            if self.product:
                p = self.product
                p.article = article
                p.name = name
                p.type = type
                p.seller = seller
                p.creator = creator
                p.description = description
                p.price = int(price)
                p.discount = discount
                p.count = count
                
                if path!="" and (not p.image or p.image.path != path):
                    filename = os.path.basename(path)
                    with open(path, "rb") as f:
                        p.image.delete()
                        p.image.save(filename,File(f),save=True)
                elif p.image and path =="":
                    p.image.delete()
            
                p.save()
            else:
                p= Product()
                p.article = article
                p.name = name
                p.type = type
                p.seller = seller
                p.creator = creator
                p.description = description
                p.price = int(price)
                p.discount = discount
                p.count = count
                p.save_base()
                if path!="":
                    filename = os.path.basename(path)
                    with open(path, "rb") as f:
                        p.image.delete()
                        p.image.save(filename,File(f),save=True)
                p.save()
            QMessageBox.information(self,"Успешно", "Успешное сохранине")
            self.close()
            
            
        else:
            QMessageBox.warning(self,"Ошибка", "Не все поля заполнены")