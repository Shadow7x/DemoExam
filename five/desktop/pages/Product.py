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
        Product.resize(680, 179)
        Product.setMinimumSize(QSize(680, 0))
        Product.setMaximumSize(QSize(680, 16777215))
        Product.setBaseSize(QSize(680, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        Product.setFont(font)
        self.horizontalLayout = QHBoxLayout(Product)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image = QLabel(Product)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(150, 150))
        self.image.setMaximumSize(QSize(150, 150))
        self.image.setBaseSize(QSize(150, 150))
        self.image.setLineWidth(12)
        self.image.setPixmap(QPixmap(u"../../../../../../../time/import/picture.png"))
        self.image.setScaledContents(True)

        self.horizontalLayout.addWidget(self.image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Type = QLabel(Product)
        self.Type.setObjectName(u"Type")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Type.setFont(font1)

        self.verticalLayout.addWidget(self.Type)

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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(Product)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.OldPrice = QLabel(Product)
        self.OldPrice.setObjectName(u"OldPrice")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setStrikeOut(True)
        self.OldPrice.setFont(font2)
        self.OldPrice.setStyleSheet(u"text-decoration:line-through;\n"
"color: red;")

        self.horizontalLayout_2.addWidget(self.OldPrice)

        self.NewPrice = QLabel(Product)
        self.NewPrice.setObjectName(u"NewPrice")

        self.horizontalLayout_2.addWidget(self.NewPrice)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Count = QLabel(Product)
        self.Count.setObjectName(u"Count")

        self.verticalLayout.addWidget(self.Count)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Discount = QLabel(Product)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Discount)

        self.Update = QPushButton(Product)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(Product)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Product)

        QMetaObject.connectSlotsByName(Product)
    # setupUi

    def retranslateUi(self, Product):
        Product.setWindowTitle(QCoreApplication.translate("Product", u"Frame", None))
        self.image.setText("")
        self.Type.setText("")
        self.Description.setText(QCoreApplication.translate("Product", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430: ", None))
        self.Creator.setText(QCoreApplication.translate("Product", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: ", None))
        self.Seller.setText(QCoreApplication.translate("Product", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a: ", None))
        self.label_6.setText(QCoreApplication.translate("Product", u"\u0426\u0435\u043d\u0430: ", None))
        self.OldPrice.setText(QCoreApplication.translate("Product", u"TextLabel", None))
        self.NewPrice.setText(QCoreApplication.translate("Product", u"TextLabel", None))
        self.Count.setText(QCoreApplication.translate("Product", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435: ", None))
        self.Discount.setText(QCoreApplication.translate("Product", u"%", None))
        self.Update.setText(QCoreApplication.translate("Product", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Product", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

