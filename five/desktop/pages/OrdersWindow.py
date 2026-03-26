# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrdersWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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

class Ui_OrdersWindow(object):
    def setupUi(self, OrdersWindow):
        if not OrdersWindow.objectName():
            OrdersWindow.setObjectName(u"OrdersWindow")
        OrdersWindow.resize(894, 597)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        OrdersWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OrdersWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(OrdersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout_2.addWidget(self.Exit)

        self.CreateOrder = QPushButton(self.centralwidget)
        self.CreateOrder.setObjectName(u"CreateOrder")

        self.verticalLayout_2.addWidget(self.CreateOrder)

        self.Products = QPushButton(self.centralwidget)
        self.Products.setObjectName(u"Products")

        self.verticalLayout_2.addWidget(self.Products)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 746, 550))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 1)

        OrdersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrdersWindow)

        QMetaObject.connectSlotsByName(OrdersWindow)
    # setupUi

    def retranslateUi(self, OrdersWindow):
        OrdersWindow.setWindowTitle(QCoreApplication.translate("OrdersWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.Exit.setText(QCoreApplication.translate("OrdersWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.CreateOrder.setText(QCoreApplication.translate("OrdersWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.Products.setText(QCoreApplication.translate("OrdersWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.FIO.setText(QCoreApplication.translate("OrdersWindow", u"FIO", None))
    # retranslateUi

