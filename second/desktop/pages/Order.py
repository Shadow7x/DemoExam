# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Order.ui'
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

class Ui_Order(object):
    def setupUi(self, Order):
        if not Order.objectName():
            Order.setObjectName(u"Order")
        Order.resize(621, 123)
        Order.setMinimumSize(QSize(621, 0))
        Order.setMaximumSize(QSize(621, 16777215))
        Order.setBaseSize(QSize(621, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        Order.setFont(font)
        self.horizontalLayout = QHBoxLayout(Order)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Article = QLabel(Order)
        self.Article.setObjectName(u"Article")
        font1 = QFont()
        font1.setBold(True)
        self.Article.setFont(font1)

        self.verticalLayout.addWidget(self.Article)

        self.Status = QLabel(Order)
        self.Status.setObjectName(u"Status")

        self.verticalLayout.addWidget(self.Status)

        self.Location = QLabel(Order)
        self.Location.setObjectName(u"Location")
        self.Location.setWordWrap(True)

        self.verticalLayout.addWidget(self.Location)

        self.date = QLabel(Order)
        self.date.setObjectName(u"date")

        self.verticalLayout.addWidget(self.date)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.DateDelivery = QLabel(Order)
        self.DateDelivery.setObjectName(u"DateDelivery")

        self.verticalLayout_2.addWidget(self.DateDelivery)

        self.Update = QPushButton(Order)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(Order)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Order)

        QMetaObject.connectSlotsByName(Order)
    # setupUi

    def retranslateUi(self, Order):
        Order.setWindowTitle(QCoreApplication.translate("Order", u"Frame", None))
        self.Article.setText(QCoreApplication.translate("Order", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b \u0437\u0430\u043a\u0430\u0437: ", None))
        self.Status.setText(QCoreApplication.translate("Order", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.Location.setText(QCoreApplication.translate("Order", u"\u0410\u0434\u0440\u0435\u0441\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438: ", None))
        self.date.setText(QCoreApplication.translate("Order", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437", None))
        self.DateDelivery.setText(QCoreApplication.translate("Order", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0442\u0441\u0430\u0432\u043a\u0438: ", None))
        self.Update.setText(QCoreApplication.translate("Order", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Order", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

