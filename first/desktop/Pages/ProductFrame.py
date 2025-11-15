# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ProductFrame(object):
    def setupUi(self, ProductFrame):
        if not ProductFrame.objectName():
            ProductFrame.setObjectName(u"ProductFrame")
        ProductFrame.resize(573, 161)
        ProductFrame.setMinimumSize(QSize(573, 0))
        ProductFrame.setMaximumSize(QSize(573, 16777215))
        ProductFrame.setBaseSize(QSize(573, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        ProductFrame.setFont(font)
        self.gridLayout_2 = QGridLayout(ProductFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Counter = QLabel(ProductFrame)
        self.Counter.setObjectName(u"Counter")

        self.gridLayout.addWidget(self.Counter, 5, 0, 1, 1)

        self.Description = QLabel(ProductFrame)
        self.Description.setObjectName(u"Description")
        self.Description.setWordWrap(True)

        self.gridLayout.addWidget(self.Description, 1, 0, 1, 1)

        self.Count = QLabel(ProductFrame)
        self.Count.setObjectName(u"Count")

        self.gridLayout.addWidget(self.Count, 6, 0, 1, 1)

        self.Seller = QLabel(ProductFrame)
        self.Seller.setObjectName(u"Seller")

        self.gridLayout.addWidget(self.Seller, 3, 0, 1, 1)

        self.Price = QLabel(ProductFrame)
        self.Price.setObjectName(u"Price")

        self.gridLayout.addWidget(self.Price, 4, 0, 1, 1)

        self.Creator = QLabel(ProductFrame)
        self.Creator.setObjectName(u"Creator")

        self.gridLayout.addWidget(self.Creator, 2, 0, 1, 1)

        self.Name = QLabel(ProductFrame)
        self.Name.setObjectName(u"Name")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.Name.setFont(font1)
        self.Name.setStyleSheet(u"")
        self.Name.setScaledContents(False)

        self.gridLayout.addWidget(self.Name, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.Discount = QLabel(ProductFrame)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Discount)

        self.Delete = QPushButton(ProductFrame)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setEnabled(True)
        self.Delete.setMinimumSize(QSize(128, 0))
        self.Delete.setMaximumSize(QSize(128, 16777215))
        self.Delete.setBaseSize(QSize(128, 0))

        self.verticalLayout.addWidget(self.Delete)

        self.Update = QPushButton(ProductFrame)
        self.Update.setObjectName(u"Update")
        self.Update.setMinimumSize(QSize(128, 0))
        self.Update.setMaximumSize(QSize(128, 16777215))
        self.Update.setBaseSize(QSize(128, 0))

        self.verticalLayout.addWidget(self.Update)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.Image = QLabel(ProductFrame)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(140, 140))
        self.Image.setMaximumSize(QSize(140, 140))
        self.Image.setBaseSize(QSize(140, 140))
        self.Image.setText(u"")
        self.Image.setPixmap(QPixmap(u"C:/Users/logvl/Downloads/picture.png"))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.Image, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.retranslateUi(ProductFrame)

        QMetaObject.connectSlotsByName(ProductFrame)
    # setupUi

    def retranslateUi(self, ProductFrame):
        ProductFrame.setWindowTitle("")
        self.Counter.setText(QCoreApplication.translate("ProductFrame", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f:", None))
        self.Description.setText(QCoreApplication.translate("ProductFrame", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430:", None))
        self.Count.setText(QCoreApplication.translate("ProductFrame", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.Seller.setText(QCoreApplication.translate("ProductFrame", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.Price.setText(QCoreApplication.translate("ProductFrame", u"\u0426\u0435\u043d\u0430:", None))
        self.Creator.setText(QCoreApplication.translate("ProductFrame", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.Name.setText("")
        self.Discount.setText(QCoreApplication.translate("ProductFrame", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.Delete.setText(QCoreApplication.translate("ProductFrame", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Update.setText(QCoreApplication.translate("ProductFrame", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

