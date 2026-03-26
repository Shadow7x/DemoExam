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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(700, 199)
        Frame.setMinimumSize(QSize(700, 0))
        Frame.setMaximumSize(QSize(700, 16777215))
        Frame.setBaseSize(QSize(700, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        Frame.setFont(font)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 680, 69))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FIO = QLabel(Frame)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setWordWrap(True)

        self.verticalLayout.addWidget(self.FIO)

        self.Status = QLabel(Frame)
        self.Status.setObjectName(u"Status")
        self.Status.setWordWrap(True)

        self.verticalLayout.addWidget(self.Status)

        self.Address = QLabel(Frame)
        self.Address.setObjectName(u"Address")
        self.Address.setWordWrap(True)

        self.verticalLayout.addWidget(self.Address)

        self.Date = QLabel(Frame)
        self.Date.setObjectName(u"Date")

        self.verticalLayout.addWidget(self.Date)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.DateDelivery = QLabel(Frame)
        self.DateDelivery.setObjectName(u"DateDelivery")

        self.verticalLayout_3.addWidget(self.DateDelivery)

        self.Update = QPushButton(Frame)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_3.addWidget(self.Update)

        self.Delete = QPushButton(Frame)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_3.addWidget(self.Delete)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.FIO.setText(QCoreApplication.translate("Frame", u"\u0424\u0418\u041e \u041a\u043b\u0438\u0435\u043d\u0442\u0430: ", None))
        self.Status.setText(QCoreApplication.translate("Frame", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0417\u0430\u043a\u0430\u0437\u0430:", None))
        self.Address.setText(QCoreApplication.translate("Frame", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438: ", None))
        self.Date.setText(QCoreApplication.translate("Frame", u"\u0414\u0430\u0442\u0430 \u0417\u0430\u043a\u0430\u0437\u0430", None))
        self.DateDelivery.setText(QCoreApplication.translate("Frame", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438: ", None))
        self.Update.setText(QCoreApplication.translate("Frame", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("Frame", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

