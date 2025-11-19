# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProductDialog(object):
    def setupUi(self, ProductDialog):
        if not ProductDialog.objectName():
            ProductDialog.setObjectName(u"ProductDialog")
        ProductDialog.resize(426, 607)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        ProductDialog.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.JPG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ProductDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ProductDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Counter = QLineEdit(ProductDialog)
        self.Counter.setObjectName(u"Counter")

        self.gridLayout.addWidget(self.Counter, 8, 1, 1, 3)

        self.Save = QPushButton(ProductDialog)
        self.Save.setObjectName(u"Save")
        self.Save.setFont(font)

        self.gridLayout.addWidget(self.Save, 11, 1, 1, 1)

        self.Article = QLineEdit(ProductDialog)
        self.Article.setObjectName(u"Article")

        self.gridLayout.addWidget(self.Article, 1, 1, 1, 3)

        self.comboBoxCreator = QComboBox(ProductDialog)
        self.comboBoxCreator.setObjectName(u"comboBoxCreator")

        self.gridLayout.addWidget(self.comboBoxCreator, 5, 1, 1, 3)

        self.Description = QLineEdit(ProductDialog)
        self.Description.setObjectName(u"Description")

        self.gridLayout.addWidget(self.Description, 4, 1, 1, 3)

        self.Seller = QLineEdit(ProductDialog)
        self.Seller.setObjectName(u"Seller")

        self.gridLayout.addWidget(self.Seller, 6, 1, 1, 3)

        self.Image = QLabel(ProductDialog)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(140, 140))
        self.Image.setMaximumSize(QSize(140, 140))
        self.Image.setBaseSize(QSize(140, 140))
        self.Image.setPixmap(QPixmap(u"../../../../../../../time/import/picture.png"))
        self.Image.setScaledContents(True)

        self.gridLayout.addWidget(self.Image, 0, 0, 1, 2)

        self.label_2 = QLabel(ProductDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Discount = QLineEdit(ProductDialog)
        self.Discount.setObjectName(u"Discount")

        self.gridLayout.addWidget(self.Discount, 10, 1, 1, 3)

        self.label_8 = QLabel(ProductDialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_9 = QLabel(ProductDialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.comboBoxType = QComboBox(ProductDialog)
        self.comboBoxType.setObjectName(u"comboBoxType")

        self.gridLayout.addWidget(self.comboBoxType, 3, 1, 1, 3)

        self.label_10 = QLabel(ProductDialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_11 = QLabel(ProductDialog)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.Count = QLineEdit(ProductDialog)
        self.Count.setObjectName(u"Count")

        self.gridLayout.addWidget(self.Count, 9, 1, 1, 3)

        self.Price = QLineEdit(ProductDialog)
        self.Price.setObjectName(u"Price")

        self.gridLayout.addWidget(self.Price, 7, 1, 1, 3)

        self.label_7 = QLabel(ProductDialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_5 = QLabel(ProductDialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(ProductDialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.Name = QLineEdit(ProductDialog)
        self.Name.setObjectName(u"Name")

        self.gridLayout.addWidget(self.Name, 2, 1, 1, 3)

        self.label_3 = QLabel(ProductDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(ProductDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpenImage = QPushButton(ProductDialog)
        self.OpenImage.setObjectName(u"OpenImage")

        self.verticalLayout.addWidget(self.OpenImage)

        self.Path = QLineEdit(ProductDialog)
        self.Path.setObjectName(u"Path")
        self.Path.setReadOnly(True)

        self.verticalLayout.addWidget(self.Path)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.retranslateUi(ProductDialog)

        QMetaObject.connectSlotsByName(ProductDialog)
    # setupUi

    def retranslateUi(self, ProductDialog):
        ProductDialog.setWindowTitle(QCoreApplication.translate("ProductDialog", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.Save.setText(QCoreApplication.translate("ProductDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Image.setText("")
        self.label_2.setText(QCoreApplication.translate("ProductDialog", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_8.setText(QCoreApplication.translate("ProductDialog", u"\u0426\u0435\u043d\u0430", None))
        self.label_9.setText(QCoreApplication.translate("ProductDialog", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_10.setText(QCoreApplication.translate("ProductDialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.label_11.setText(QCoreApplication.translate("ProductDialog", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("ProductDialog", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_5.setText(QCoreApplication.translate("ProductDialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("ProductDialog", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("ProductDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("ProductDialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.OpenImage.setText(QCoreApplication.translate("ProductDialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
    # retranslateUi

