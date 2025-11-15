# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrdersList.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_OrderWindow(object):
    def setupUi(self, OrderWindow):
        if not OrderWindow.objectName():
            OrderWindow.setObjectName(u"OrderWindow")
        OrderWindow.resize(730, 599)
        self.centralwidget = QWidget(OrderWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.scrollArea.setFont(font)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 619, 560))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.User = QLabel(self.centralwidget)
        self.User.setObjectName(u"User")
        self.User.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.User, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.CreateOrder = QPushButton(self.centralwidget)
        self.CreateOrder.setObjectName(u"CreateOrder")

        self.gridLayout.addWidget(self.CreateOrder, 1, 0, 1, 1)

        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.gridLayout.addWidget(self.Exit, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.Orders = QPushButton(self.centralwidget)
        self.Orders.setObjectName(u"Orders")

        self.gridLayout.addWidget(self.Orders, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        OrderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrderWindow)

        QMetaObject.connectSlotsByName(OrderWindow)
    # setupUi

    def retranslateUi(self, OrderWindow):
        OrderWindow.setWindowTitle(QCoreApplication.translate("OrderWindow", u"MainWindow", None))
        self.User.setText("")
        self.CreateOrder.setText(QCoreApplication.translate("OrderWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0417\u0430\u043a\u0430\u0437", None))
        self.Exit.setText(QCoreApplication.translate("OrderWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.Orders.setText(QCoreApplication.translate("OrderWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
    # retranslateUi

