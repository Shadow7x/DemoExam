# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProdcutFrame.ui'
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

class Ui_ProductFrame(object):
    def setupUi(self, ProductFrame):
        if not ProductFrame.objectName():
            ProductFrame.setObjectName(u"ProductFrame")
        ProductFrame.resize(670, 177)
        ProductFrame.setMinimumSize(QSize(670, 0))
        ProductFrame.setMaximumSize(QSize(670, 16777215))
        ProductFrame.setBaseSize(QSize(670, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        ProductFrame.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(ProductFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Image = QLabel(ProductFrame)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(150, 150))
        self.Image.setMaximumSize(QSize(150, 150))
        self.Image.setBaseSize(QSize(150, 150))
        self.Image.setPixmap(QPixmap(u"./picture.png"))
        self.Image.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.Image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Article = QLabel(ProductFrame)
        self.Article.setObjectName(u"Article")
        font1 = QFont()
        font1.setBold(True)
        self.Article.setFont(font1)
        self.Article.setWordWrap(True)

        self.verticalLayout.addWidget(self.Article)

        self.Description = QLabel(ProductFrame)
        self.Description.setObjectName(u"Description")
        self.Description.setWordWrap(True)

        self.verticalLayout.addWidget(self.Description)

        self.Creator = QLabel(ProductFrame)
        self.Creator.setObjectName(u"Creator")

        self.verticalLayout.addWidget(self.Creator)

        self.Seller = QLabel(ProductFrame)
        self.Seller.setObjectName(u"Seller")

        self.verticalLayout.addWidget(self.Seller)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(ProductFrame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.Price = QLabel(ProductFrame)
        self.Price.setObjectName(u"Price")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setStrikeOut(True)
        self.Price.setFont(font2)
        self.Price.setStyleSheet(u"color:red;")

        self.horizontalLayout.addWidget(self.Price)

        self.NewPrice = QLabel(ProductFrame)
        self.NewPrice.setObjectName(u"NewPrice")

        self.horizontalLayout.addWidget(self.NewPrice)

        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Count = QLabel(ProductFrame)
        self.Count.setObjectName(u"Count")

        self.verticalLayout.addWidget(self.Count)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Discount = QLabel(ProductFrame)
        self.Discount.setObjectName(u"Discount")

        self.verticalLayout_2.addWidget(self.Discount)

        self.Update = QPushButton(ProductFrame)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(ProductFrame)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(ProductFrame)

        QMetaObject.connectSlotsByName(ProductFrame)
    # setupUi

    def retranslateUi(self, ProductFrame):
        ProductFrame.setWindowTitle(QCoreApplication.translate("ProductFrame", u"Frame", None))
        self.Image.setText("")
        self.Article.setText("")
        self.Description.setText(QCoreApplication.translate("ProductFrame", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430: ", None))
        self.Creator.setText(QCoreApplication.translate("ProductFrame", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: ", None))
        self.Seller.setText(QCoreApplication.translate("ProductFrame", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a: ", None))
        self.label_6.setText(QCoreApplication.translate("ProductFrame", u"\u0426\u0435\u043d\u0430: ", None))
        self.Price.setText(QCoreApplication.translate("ProductFrame", u"TextLabel", None))
        self.NewPrice.setText(QCoreApplication.translate("ProductFrame", u"TextLabel", None))
        self.Count.setText(QCoreApplication.translate("ProductFrame", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435: ", None))
        self.Discount.setText(QCoreApplication.translate("ProductFrame", u" %", None))
        self.Update.setText(QCoreApplication.translate("ProductFrame", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("ProductFrame", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

