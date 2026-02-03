from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QMessageBox, QFrame
from PySide6.QtGui import QPixmap
from .pages.MainWindow import Ui_MainWindow
from .pages.Product import Ui_Product
from .pages.ProductWindow import Ui_ProductWindow
from .models import *



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
    def __init__(self, product : Product) -> None:
        super(ProductFrame,self).__init__()
        
        self.ui = Ui_Product()
        ui = self.ui
        ui.setupUi(self)
        
        self.product = product
        
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

        if product.image != None:
            pixmap = QPixmap(product.image.path)
            ui.Image.setPixmap(pixmap)
        

class ProductWindow(QMainWindow):
    def __init__(self, user : User | None) -> None:
        super(ProductWindow,self).__init__()
        
        self.ui = Ui_ProductWindow()
        ui = self.ui
        ui.setupUi(self)
        
        if user:
            self.user = user
            ui.FIO.setText(user.__str__())
        else: 
            ui.FIO.setText("Гость")
        
        self.initialize()
        ui.Exit.clicked.connect(self.exit)
        
    def initialize(self):
        ui = self.ui
        products = Product.objects.all()
        
        for p in products:
            frame = ProductFrame(p)
            
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
        
        
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
        
        
            
        
        