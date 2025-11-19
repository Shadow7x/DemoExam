# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderWindow.ui'
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

class Ui_OrderWindow(object):
    def setupUi(self, OrderWindow):
        if not OrderWindow.objectName():
            OrderWindow.setObjectName(u"OrderWindow")
        OrderWindow.resize(882, 600)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        OrderWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.JPG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OrderWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(OrderWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout.addWidget(self.Exit)

        self.AddOrder = QPushButton(self.centralwidget)
        self.AddOrder.setObjectName(u"AddOrder")

        self.verticalLayout.addWidget(self.AddOrder)

        self.Products = QPushButton(self.centralwidget)
        self.Products.setObjectName(u"Products")

        self.verticalLayout.addWidget(self.Products)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 696, 552))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)

        OrderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrderWindow)

        QMetaObject.connectSlotsByName(OrderWindow)
    # setupUi

    def retranslateUi(self, OrderWindow):
        OrderWindow.setWindowTitle(QCoreApplication.translate("OrderWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.Exit.setText(QCoreApplication.translate("OrderWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.AddOrder.setText(QCoreApplication.translate("OrderWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u041f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.Products.setText(QCoreApplication.translate("OrderWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.FIO.setText("")
    # retranslateUi

