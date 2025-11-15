# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Order.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_OrderFrame(object):
    def setupUi(self, OrderFrame):
        if not OrderFrame.objectName():
            OrderFrame.setObjectName(u"OrderFrame")
        OrderFrame.resize(573, 100)
        OrderFrame.setMinimumSize(QSize(573, 100))
        OrderFrame.setMaximumSize(QSize(573, 100))
        OrderFrame.setBaseSize(QSize(573, 100))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        OrderFrame.setFont(font)
        self.gridLayout_2 = QGridLayout(OrderFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.DateDelivery = QLabel(OrderFrame)
        self.DateDelivery.setObjectName(u"DateDelivery")

        self.verticalLayout_2.addWidget(self.DateDelivery)

        self.Delete = QPushButton(OrderFrame)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)

        self.Update = QPushButton(OrderFrame)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Article = QLabel(OrderFrame)
        self.Article.setObjectName(u"Article")
        font1 = QFont()
        font1.setBold(True)
        self.Article.setFont(font1)

        self.verticalLayout.addWidget(self.Article)

        self.Status = QLabel(OrderFrame)
        self.Status.setObjectName(u"Status")

        self.verticalLayout.addWidget(self.Status)

        self.Address = QLabel(OrderFrame)
        self.Address.setObjectName(u"Address")

        self.verticalLayout.addWidget(self.Address)

        self.Date = QLabel(OrderFrame)
        self.Date.setObjectName(u"Date")

        self.verticalLayout.addWidget(self.Date)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 4)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.retranslateUi(OrderFrame)

        QMetaObject.connectSlotsByName(OrderFrame)
    # setupUi

    def retranslateUi(self, OrderFrame):
        OrderFrame.setWindowTitle(QCoreApplication.translate("OrderFrame", u"Frame", None))
        self.DateDelivery.setText(QCoreApplication.translate("OrderFrame", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438: ", None))
        self.Delete.setText(QCoreApplication.translate("OrderFrame", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Update.setText(QCoreApplication.translate("OrderFrame", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Article.setText(QCoreApplication.translate("OrderFrame", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b \u0437\u0430\u043a\u0430\u0437\u0430: ", None))
        self.Status.setText(QCoreApplication.translate("OrderFrame", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430: ", None))
        self.Address.setText(QCoreApplication.translate("OrderFrame", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.Date.setText(QCoreApplication.translate("OrderFrame", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430: ", None))
    # retranslateUi

