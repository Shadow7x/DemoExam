# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Product.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Product(object):
    def setupUi(self, Product):
        if not Product.objectName():
            Product.setObjectName(u"Product")
        Product.resize(658, 205)
        Product.setMinimumSize(QSize(658, 0))
        Product.setMaximumSize(QSize(658, 16777215))
        Product.setBaseSize(QSize(658, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        Product.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(Product)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Image = QLabel(Product)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(150, 150))
        self.Image.setMaximumSize(QSize(150, 150))
        self.Image.setBaseSize(QSize(150, 150))
        self.Image.setPixmap(QPixmap(u"../../../../../../../time/import/picture.png"))
        self.Image.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.Image)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.OldPrice = QLabel(Product)
        self.OldPrice.setObjectName(u"OldPrice")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setStrikeOut(True)
        self.OldPrice.setFont(font1)
        self.OldPrice.setStyleSheet(u"color:red; text-decoration:line-through;")

        self.gridLayout.addWidget(self.OldPrice, 4, 1, 1, 1)

        self.Price = QLabel(Product)
        self.Price.setObjectName(u"Price")

        self.gridLayout.addWidget(self.Price, 4, 0, 1, 1)

        self.NewPrice = QLabel(Product)
        self.NewPrice.setObjectName(u"NewPrice")

        self.gridLayout.addWidget(self.NewPrice, 4, 2, 1, 1)

        self.Type = QLabel(Product)
        self.Type.setObjectName(u"Type")
        font2 = QFont()
        font2.setBold(True)
        self.Type.setFont(font2)

        self.gridLayout.addWidget(self.Type, 0, 0, 1, 3)

        self.Description = QLabel(Product)
        self.Description.setObjectName(u"Description")
        self.Description.setWordWrap(True)

        self.gridLayout.addWidget(self.Description, 1, 0, 1, 3)

        self.Creator = QLabel(Product)
        self.Creator.setObjectName(u"Creator")

        self.gridLayout.addWidget(self.Creator, 2, 0, 1, 3)

        self.Seller = QLabel(Product)
        self.Seller.setObjectName(u"Seller")

        self.gridLayout.addWidget(self.Seller, 3, 0, 1, 3)

        self.Counter = QLabel(Product)
        self.Counter.setObjectName(u"Counter")

        self.gridLayout.addWidget(self.Counter, 5, 0, 1, 3)

        self.Count = QLabel(Product)
        self.Count.setObjectName(u"Count")

        self.gridLayout.addWidget(self.Count, 6, 0, 1, 3)

        self.gridLayout.setColumnStretch(2, 10)

        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Discount = QLabel(Product)
        self.Discount.setObjectName(u"Discount")

        self.verticalLayout_2.addWidget(self.Discount)

        self.Update = QPushButton(Product)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(Product)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setFont(font)

        self.verticalLayout_2.addWidget(self.Delete)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)

        self.retranslateUi(Product)

        QMetaObject.connectSlotsByName(Product)
    # setupUi

    def retranslateUi(self, Product):
        Product.setWindowTitle(QCoreApplication.translate("Product", u"Frame", None))
        self.Image.setText("")
        self.OldPrice.setText(QCoreApplication.translate("Product", u"TextLabel", None))
        self.Price.setText(QCoreApplication.translate("Product", u"\u0426\u0435\u043d\u0430: ", None))
        self.NewPrice.setText(QCoreApplication.translate("Product", u"TextLabel", None))
        self.Type.setText("")
        self.Description.setText(QCoreApplication.translate("Product", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430: ", None))
        self.Creator.setText(QCoreApplication.translate("Product", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: ", None))
        self.Seller.setText(QCoreApplication.translate("Product", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a: ", None))
        self.Counter.setText(QCoreApplication.translate("Product", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f: ", None))
        self.Count.setText(QCoreApplication.translate("Product", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0432\u0442\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435: ", None))
        self.Discount.setText(QCoreApplication.translate("Product", u"%", None))
        self.Update.setText(QCoreApplication.translate("Product", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Product", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

