from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QMessageBox,QFrame, QDialog, QPushButton
from PySide6.QtGui import QPixmap
from desktop.models import *
import datetime

from desktop.pages.MainWindow import Ui_MainWindow
from desktop.pages.CinemaWindow import Ui_CinemaWindow
from desktop.pages.FrameCinema import Ui_FrameCinema
from desktop.pages.DialogBooking import Ui_DialogBooking


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        ui = self.ui
        ui.setupUi(self)
        
        ui.Login.setText("admin.cinema@mail.ru")
        ui.Password.setText("9SdkLp012")
        
        ui.Enter.clicked.connect(self.enter)
        ui.Guest.clicked.connect(self.open_cinemas)
    
    def enter(self):
        login = self.ui.Login.text()
        password = self.ui.Password.text()
        if User.objects.filter(login =login,password = password).exists():
            self.open_cinemas(User.objects.filter(login =login,password = password).first())
        else:
            QMessageBox.warning(self, "Ошибка", " Такого пользователя не существует")
            
    def open_cinemas(self, user: User | None = None):
        self.windows = CinemasWindow(user)
        self.windows.show()
        self.close()


class BookingDialog(QDialog):
    def __init__(self, cinema : Cinema, parents:"CinemaFrame") -> None:
        super(BookingDialog, self).__init__()
        
        self.ui = Ui_DialogBooking()
        ui = self.ui
        ui.setupUi(self)
        
        self.parents = parents
        self.cinema = cinema
        
        self.booking =[]
        tickets = Ticket.objects.filter(cinema = cinema)
        self.closed = []
        for t in tickets:
            self.closed.append((t.row,t.column))
        grid = ui.gridLayout
        rows = range(cinema.hall.rows)
        row = 0
        for r in rows:
            row +=1
            for c in range(cinema.hall.columns):
                button = QPushButton(f"Место {c+1}")
                
                if (r,c) in self.closed:
                    button.setStyleSheet('background-color:red')
                else:button.clicked.connect(lambda _, r=r, c=c : self.results(r,c))
                
                
                grid.layout().addWidget(button,r,c)
        
        ui.pushButton.clicked.connect(self.create_booking)
                
    def results(self, row, column):
        ui = self.ui
        widget = ui.gridLayout.itemAtPosition(row,column).widget()

        current_font = widget.font()
        if (row,column) in self.booking:
            self.booking.remove((row,column))
            widget.setStyleSheet("")
        else:
            self.booking.append((row,column))
            widget.setStyleSheet("background-color:blue")
        widget.setFont(current_font)

    def create_booking(self):
        b = Booking.objects.create(date = datetime.datetime.now().date(), date_seance = datetime.datetime.now().date(), user = self.parents.parents.user,code = Booking.objects.last().pk+900 or 1, status = "Новый")
        for items in self.booking:
            Ticket.objects.create(row = items[0], column = items[1], cinema = self.cinema, booking = b)
        self.close()
        
        
class CinemaFrame(QFrame):
    def __init__(self, cinema : Cinema, parent: "CinemasWindow") -> None:
        super(CinemaFrame, self).__init__()
        
        self.ui = Ui_FrameCinema()
        ui = self.ui
        ui.setupUi(self)
        self.cinema = cinema
        self.parents = parent

        
        ui.Name.setText(ui.Name.text()+ cinema.name)
        ui.Producer.setText(ui.Producer.text()+ cinema.producer)
        ui.Genre.setText(ui.Genre.text()+ cinema.genre)
        ui.Description.setText(ui.Description.text()+ cinema.Description)
        
        count = Ticket.objects.filter(cinema=cinema).count()
        hall_count = cinema.hall.rows * cinema.hall.columns
        
        ui.Count.setText(str(hall_count-count))
        
        ui.Discount.setText(str(cinema.discount)+ ui.Discount.text())
        
        if cinema.image:
            pixmap = QPixmap(cinema.image.path)
            ui.Image.setPixmap(pixmap)
        
        if cinema.discount>0:
            ui.OldPrice.setText(str(cinema.price))
            ui.NewPrice.setText(str(cinema.price - (cinema.price*cinema.discount*0.01)))
        else:
            ui.OldPrice.hide()
            ui.NewPrice.setText(str(cinema.price ))

        ui.Update.clicked.connect(self.updateCinema)
        ui.pushButton.clicked.connect(self.open_booking)
        
        
    def updateCinema(self):
        QMessageBox.information(self,"asd","asdasd")
    
    def open_booking(self):
        dialog = BookingDialog(self.cinema,self)
        dialog.exec()
        self.parents.initialize()

class CinemasWindow(QMainWindow):
    def __init__(self, user:User|None) -> None:
        super(CinemasWindow, self).__init__()
        
        self.ui = Ui_CinemaWindow()
        ui = self.ui
        ui.setupUi(self)
        
        self.user = user
        
        ui.Exit.clicked.connect(self.exit)
        
        ui.FIO.setText(user.__str__() if user else "Гость")
        
        self.initialize()
    
    def initialize(self):
        cinemas = Cinema.objects.all()
        ui = self.ui
        
        layout = ui.scrollAreaWidgetContents.layout()
        while layout.count():
            widget = layout.takeAt(0)
            try:
                widget.widget().deleteLater()
            except:
                pass
        
        for c in cinemas:
            frame = CinemaFrame(c, self)
            layout.addWidget(frame)
    
    def exit(self):
        self.windows = MainWindow()
        self.windows.show()
        self.close()