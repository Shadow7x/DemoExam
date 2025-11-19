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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Product(object):
    def setupUi(self, Product):
        if not Product.objectName():
            Product.setObjectName(u"Product")
        Product.resize(668, 204)
        Product.setMinimumSize(QSize(668, 0))
        Product.setMaximumSize(QSize(668, 16777215))
        Product.setBaseSize(QSize(668, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        Product.setFont(font)
        self.horizontalLayout = QHBoxLayout(Product)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Product)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 140))
        self.label.setMaximumSize(QSize(140, 140))
        self.label.setBaseSize(QSize(140, 140))
        self.label.setPixmap(QPixmap(u"../../../../../../../time/import/picture.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Name = QLabel(Product)
        self.Name.setObjectName(u"Name")
        font1 = QFont()
        font1.setBold(True)
        self.Name.setFont(font1)

        self.verticalLayout.addWidget(self.Name)

        self.Description = QLabel(Product)
        self.Description.setObjectName(u"Description")
        self.Description.setWordWrap(True)

        self.verticalLayout.addWidget(self.Description)

        self.Creator = QLabel(Product)
        self.Creator.setObjectName(u"Creator")

        self.verticalLayout.addWidget(self.Creator)

        self.Seller = QLabel(Product)
        self.Seller.setObjectName(u"Seller")

        self.verticalLayout.addWidget(self.Seller)

        self.Price = QLabel(Product)
        self.Price.setObjectName(u"Price")

        self.verticalLayout.addWidget(self.Price)

        self.Counter = QLabel(Product)
        self.Counter.setObjectName(u"Counter")

        self.verticalLayout.addWidget(self.Counter)

        self.Count = QLabel(Product)
        self.Count.setObjectName(u"Count")

        self.verticalLayout.addWidget(self.Count)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Discount = QLabel(Product)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setFont(font)

        self.verticalLayout_2.addWidget(self.Discount)

        self.Update = QPushButton(Product)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(Product)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Product)

        QMetaObject.connectSlotsByName(Product)
    # setupUi

    def retranslateUi(self, Product):
        Product.setWindowTitle(QCoreApplication.translate("Product", u"Frame", None))
        self.label.setText("")
        self.Name.setText("")
        self.Description.setText(QCoreApplication.translate("Product", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430:", None))
        self.Creator.setText(QCoreApplication.translate("Product", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: ", None))
        self.Seller.setText(QCoreApplication.translate("Product", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a: ", None))
        self.Price.setText(QCoreApplication.translate("Product", u"\u0426\u0435\u043d\u0430: ", None))
        self.Counter.setText(QCoreApplication.translate("Product", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f: ", None))
        self.Count.setText(QCoreApplication.translate("Product", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435: ", None))
        self.Discount.setText(QCoreApplication.translate("Product", u"%", None))
        self.Update.setText(QCoreApplication.translate("Product", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Product", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

