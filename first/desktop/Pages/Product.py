# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Product.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Product(object):
    def setupUi(self, Product):
        if not Product.objectName():
            Product.setObjectName(u"Product")
        Product.resize(544, 483)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        Product.setFont(font)
        self.gridLayout = QGridLayout(Product)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Image = QLabel(Product)
        self.Image.setObjectName(u"Image")
        self.Image.setEnabled(True)
        self.Image.setMinimumSize(QSize(140, 140))
        self.Image.setMaximumSize(QSize(140, 140))
        self.Image.setBaseSize(QSize(140, 140))
        self.Image.setLayoutDirection(Qt.LeftToRight)
        self.Image.setPixmap(QPixmap(u"C:/Users/logvl/Downloads/picture.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignCenter)
        self.Image.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.Image, 0, 1, 1, 1)

        self.Name = QLineEdit(Product)
        self.Name.setObjectName(u"Name")

        self.gridLayout.addWidget(self.Name, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_2 = QLabel(Product)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.Type = QLineEdit(Product)
        self.Type.setObjectName(u"Type")

        self.gridLayout.addWidget(self.Type, 2, 2, 1, 1)

        self.label = QLabel(Product)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ChooseFile = QPushButton(Product)
        self.ChooseFile.setObjectName(u"ChooseFile")

        self.verticalLayout.addWidget(self.ChooseFile)

        self.Path = QLineEdit(Product)
        self.Path.setObjectName(u"Path")
        self.Path.setDragEnabled(True)
        self.Path.setReadOnly(True)

        self.verticalLayout.addWidget(self.Path)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.Button = QPushButton(Product)
        self.Button.setObjectName(u"Button")

        self.gridLayout.addWidget(self.Button, 11, 1, 1, 2)

        self.label_7 = QLabel(Product)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)

        self.Article = QLineEdit(Product)
        self.Article.setObjectName(u"Article")

        self.gridLayout.addWidget(self.Article, 3, 2, 1, 1)

        self.label_3 = QLabel(Product)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.Creator = QLineEdit(Product)
        self.Creator.setObjectName(u"Creator")

        self.gridLayout.addWidget(self.Creator, 7, 2, 1, 1)

        self.label_9 = QLabel(Product)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)

        self.Description = QLineEdit(Product)
        self.Description.setObjectName(u"Description")

        self.gridLayout.addWidget(self.Description, 10, 2, 1, 1)

        self.label_4 = QLabel(Product)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.label_5 = QLabel(Product)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        self.Counter = QLineEdit(Product)
        self.Counter.setObjectName(u"Counter")

        self.gridLayout.addWidget(self.Counter, 5, 2, 1, 1)

        self.Seller = QLineEdit(Product)
        self.Seller.setObjectName(u"Seller")

        self.gridLayout.addWidget(self.Seller, 6, 2, 1, 1)

        self.label_10 = QLabel(Product)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)

        self.Count = QLineEdit(Product)
        self.Count.setObjectName(u"Count")

        self.gridLayout.addWidget(self.Count, 9, 2, 1, 1)

        self.Discount = QLineEdit(Product)
        self.Discount.setObjectName(u"Discount")

        self.gridLayout.addWidget(self.Discount, 8, 2, 1, 1)

        self.label_11 = QLabel(Product)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 1, 1, 1)

        self.Price = QLineEdit(Product)
        self.Price.setObjectName(u"Price")

        self.gridLayout.addWidget(self.Price, 4, 2, 1, 1)

        self.label_6 = QLabel(Product)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)


        self.retranslateUi(Product)

        QMetaObject.connectSlotsByName(Product)
    # setupUi

    def retranslateUi(self, Product):
        Product.setWindowTitle(QCoreApplication.translate("Product", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.Image.setText("")
        self.label_2.setText(QCoreApplication.translate("Product", u"\u0422\u0438\u043f \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("Product", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.ChooseFile.setText(QCoreApplication.translate("Product", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.Button.setText(QCoreApplication.translate("Product", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Product", u"\u0415\u0434\u0435\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Product", u"\u0426\u0435\u043d\u0430", None))
        self.label_9.setText(QCoreApplication.translate("Product", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Product", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_5.setText(QCoreApplication.translate("Product", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_10.setText(QCoreApplication.translate("Product", u"\u041a\u043e\u043b-\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.label_11.setText(QCoreApplication.translate("Product", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("Product", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
    # retranslateUi

