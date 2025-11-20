from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTabWidget, QWidget, QFrame, QDialog, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate
from .pages.MainWindow import Ui_MainWindow
from .pages.HomeWindow import Ui_HomeWindow
from .pages.Product import Ui_Product
from .pages.ProductDialog import Ui_ProductDialog
from .pages.OrdersWindow import Ui_OrderWindow
from .pages.Order import Ui_Order
from .pages.OrderDialog import Ui_OrderDialog
from django.db.models import Q
from .models import*
from django.core.files import File
import os


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.Login.setText("94d5ous@gmail.com")
        ui.Password.setText("uzWC67")
        
        ui.Enter.clicked.connect(self.enter)
        
        ui.Guest.clicked.connect(self.openHome)
        
    def enter(self):
        login = self.ui.Login.text()
        password = self.ui.Password.text()
        if User.objects.filter(login = login, password=password).exists():
            self.openHome(User.objects.filter(login = login, password=password).first())
        else:
            QMessageBox.warning(self, "Ошибка","Такого пользователя не существует")
            
    def openHome(self, user:None | User = None):
        self.home = HomeWindow(user)
        self.home.show()
        self.close()

class ProductFrame(QFrame):
    def __init__(self,product: Product, parent:"HomeWindow", user: User| None) -> None:
        super(ProductFrame, self).__init__()
        self.ui = Ui_Product()
        ui = self.ui
        ui.setupUi(self)
        
        self.product = product
        self.main = parent
        
        ui.Type.setText(f"{product.type} | {product.name}")
        ui.Description.setText(ui.Description.text() + product.description)
        ui.Creator.setText(ui.Creator.text() + product.creator)
        ui.Seller.setText(ui.Seller.text() + product.seller)
        
        ui.Counter.setText(ui.Counter.text() + product.counter)
        ui.Count.setText(ui.Count.text() + str(product.count))
        ui.Discount.setText(str(product.discount)+ui.Discount.text())
        
        
        if product.image:
            image = QPixmap(product.image.path)
            ui.Image.setPixmap(image)
        if product.count <=0:
            ui.Type.setStyleSheet("color:blue")
        elif product.discount>15:
            ui.Type.setStyleSheet("color:#2E8B57")
        if product.discount==0:
            ui.OldPrice.deleteLater()
        
        ui.OldPrice.setText(str(product.price))
        ui.NewPrice.setText( str(product.price - product.price*product.discount*0.01))
        if not user or user.role !="Администратор":
            ui.Update.setEnabled(False)
            ui.Delete.setEnabled(False)
        
        ui.Update.clicked.connect(self.updateProduct)
        ui.Delete.clicked.connect(self.deleteProduct)
        
    def updateProduct(self):
        dialog = ProductDialog(self.product)
        dialog.exec()
        
        self.main.initialize()

    def deleteProduct(self):
        self.product.delete()
        
        self.main.initialize()
        
class OrderFrame(QFrame):
    def __init__(self,order: NewOrder, parent:"OrdersWindow", user: User| None) -> None:
        super(OrderFrame, self).__init__()
        self.ui = Ui_Order()
        ui = self.ui
        ui.setupUi(self)
        
        self.order = order
        self.main = parent
        
        ui.Article.setText(ui.Article.text() + order.article.article)
        ui.Status.setText(ui.Status.text() + order.status)
        ui.Address.setText(ui.Address.text() + order.location.location)
        
        ui.Date.setText(ui.Date.text() + str(order.date))
        ui.DateDelivery.setText(ui.DateDelivery.text() + str(order.dateDelivery))
        if not user or user.role !="Администратор":
            ui.Update.setEnabled(False)
            ui.Delete.setEnabled(False)
        
        ui.Update.clicked.connect(self.updateOrder)
        ui.Delete.clicked.connect(self.deleteOrder)
        
    def updateOrder(self):
        dialog = OrderDialog(self.order)
        dialog.exec()
        
        self.main.initialize()

    def deleteOrder(self):
        self.order.delete()
        
        self.main.initialize()
        

class HomeWindow(QMainWindow):
    def __init__(self,user: User | None = None) -> None:
        super(HomeWindow, self).__init__()
        self.ui = Ui_HomeWindow()
        ui = self.ui
        ui.setupUi(self)
        self.user = user
        
        ui.FIO.setText(f"{user.surname} {user.name} {user.patronymic}"if user else "Гость")
        
        ui.Exit.clicked.connect(self.exit)
        
        sorts = ["По возратсанию","По убыванию"]
        filters = ["Все поставщики" , *list(set([i.seller for i in Product.objects.all()]))]
        
        ui.comboBoxSort.addItems(sorts)
        ui.comboBoxFilter.addItems(filters)
            
        ui.comboBoxFilter.currentTextChanged.connect(self.initialize)
        ui.comboBoxSort.currentTextChanged.connect(self.initialize)
        ui.Search.textChanged.connect(self.initialize)
        
        ui.AddProduct.clicked.connect(self.addProduct)
        
        ui.Orders.clicked.connect(self.openOrders)
        
        if not user or user.role !="Администратор":
            ui.AddProduct.setEnabled(False)
        if not user or user.role =="Авторизированный клиент":
            ui.Orders.setEnabled(False)
            while ui.horizontalLayout.layout().count():
                item = ui.horizontalLayout.layout().takeAt(0)
                try:
                    item.widget().deleteLater()
                except:
                    pass
            # ui.horizontalLayout.layout().setEnabled(False)
        
        self.initialize()
    
    def openOrders(self):
        self.orders = OrdersWindow(self.user)
        self.orders.show()
        self.close()
        
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
        if search!="":
            products = products.filter(Q(type__icontains = search)| Q(name__icontains=search)| Q(description__icontains=search)| Q(seller__icontains=search)| Q(price__icontains=search)| Q(counter__icontains=search)| Q(count__icontains=search)| Q(discount__icontains=search))
        
        if filter!= "Все поставщики":
            products =products.filter(seller = filter)
            
        if sort == "По возратсанию":
            products = products.order_by("count")
        else:
            products = products.order_by("-count")

        
        for i in products:
            frame = ProductFrame(i,self, self.user)
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
    
    def addProduct(self):
        dialog = ProductDialog()
        dialog.exec()
        
        self.initialize()
    
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
        

class OrdersWindow(QMainWindow):
    def __init__(self,user: User | None = None) -> None:
        super(OrdersWindow, self).__init__()
        self.ui = Ui_OrderWindow()
        ui = self.ui
        ui.setupUi(self)
        self.user = user
        
        ui.FIO.setText(f"{user.surname} {user.name} {user.patronymic}"if user else "Гость")
        
        ui.Exit.clicked.connect(self.exit)
        
        ui.AddOrder.clicked.connect(self.addOrder)
        
        ui.Products.clicked.connect(self.openProducts)
        
        if not user or user.role !="Администратор":
            ui.AddOrder.setEnabled(False)
        
        self.initialize()
    
    def openProducts(self):
        self.products = HomeWindow(self.user)
        self.products.show()
        self.close()
        
    def initialize(self):
        ui = self.ui
        while ui.scrollAreaWidgetContents.layout().count():
            item = ui.scrollAreaWidgetContents.layout().takeAt(0)
            try:
                item.widget().deleteLater()
            except:
                pass
        
        orders = NewOrder.objects.all()
        
        for i in orders:
            frame = OrderFrame(i,self,self.user)
            ui.scrollAreaWidgetContents.layout().addWidget(frame)
    
    def addOrder(self):
        dialog = OrderDialog()
        dialog.exec()
        
        self.initialize()
    
    def exit(self):
        self.main = MainWindow()
        self.main.show()
        self.close()
        

class ProductDialog(QDialog):
    def __init__(self,product: Product | None = None) -> None:
        super(ProductDialog, self).__init__()
        self.ui = Ui_ProductDialog()
        ui = self.ui
        ui.setupUi(self)
        
        self.product = product
        
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
                image = QPixmap(product.image.path)
                ui.Image.setPixmap(image)
                ui.Path.setText(product.image.path)
        
        ui.Save.clicked.connect(self.save)
        
        ui.OpenFile.clicked.connect(self.choose_file)
        
    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images *.png *.jpg *.jpeg")

        self.ui.Path.setText(file_path)
        if file_path!= "":
            image = QPixmap(file_path)
            self.ui.Image.setPixmap(image)
        else:
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
        
        if all([i.replace(" ", "") !="" for i in [article, name, type, description, creator, seller, price, counter,count,discount]]):
            
            try:
                price = int(price)
                count = int(count)
                discount = int(discount)
            
                if self.product:
                    p = self.product
                    
                    p.article =article
                    p.name =name
                    p.type =type
                    p.description =description
                    p.creator =creator
                    p.seller =seller
                    p.price =price
                    p.counter =counter
                    p.count =count
                    p.discount =discount
                    
                    if path!='':
                        p.image.delete()
                        with open(path, 'rb') as f:
                            file_name= os.path.basename(path)
                            p.image.save(file_name, File(f),save=True)
                    
                    p.save()
                else:
                    product = Product.objects.create(article =article,name =name,type =type,description =description,creator =creator,seller =seller,price =price,counter =counter,count =count,discount =discount)
                    
                    if path!='':
                        with open(path, 'rb') as f:
                            file_name= os.path.basename(path)
                            product.image.save(file_name, File(f),save=True)
                    product.save()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", "Не правлиьные типы даннных")
        else:
            QMessageBox.warning(self, "Ошибка", "Не все поля заполнены")
        
        
class OrderDialog(QDialog):
    def __init__(self,order: NewOrder | None = None) -> None:
        super(OrderDialog, self).__init__()
        self.ui = Ui_OrderDialog()
        ui = self.ui
        ui.setupUi(self)
        
        self.order = order
        
        articles = [i.article for i in Product.objects.all()]
        statuses = ["Новый","Завершен"]
        addreses = [i.location for i in OrderLocation.objects.all()]
        
        ui.comboBoxAddress.addItems(addreses)
        ui.comboBoxArticle.addItems(articles)
        ui.comboBoxStatus.addItems(statuses)
        

        if order:
            ui.comboBoxArticle.setCurrentText(order.article.article)
            ui.comboBoxStatus.setCurrentText(order.status)
            ui.comboBoxAddress.setCurrentText(order.location.location)
            
            ui.Date.setSelectedDate(QDate(*list(map(int,str(order.date).split('-')))))
            ui.DateDelivery.setSelectedDate(QDate(*list(map(int,str(order.dateDelivery).split('-')))))
        
        
        ui.Save.clicked.connect(self.save)
            
    def save(self):
        ui = self.ui
        article = ui.comboBoxArticle.currentText()
        status = ui.comboBoxStatus.currentText()
        address = ui.comboBoxAddress.currentText()
        
        date = ui.Date.selectedDate().toPython()
        dateDelivery = ui.DateDelivery.selectedDate().toPython()
       
            
        try:
            if self.order:
                o = self.order
                
                o.article = Product.objects.filter(article = article).first()
                o.status = status
                o.location = OrderLocation.objects.filter(location = address).first()
                
                o.date = date
                o.dateDelivery  = dateDelivery
                
                
                
                o.save()
            else:
                
                NewOrder.objects.create(article = Product.objects.filter(article = article).first(), status = status, location = OrderLocation.objects.filter(location = address).first(),date = date, dateDelivery  = dateDelivery)
                
            self.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Ошибка", "Ошибка добавления")
    