# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDialog,
    QGridLayout, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(494, 545)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.JPG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OrderDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(OrderDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Date = QCalendarWidget(OrderDialog)
        self.Date.setObjectName(u"Date")

        self.gridLayout.addWidget(self.Date, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.comboBoxArticle = QComboBox(OrderDialog)
        self.comboBoxArticle.setObjectName(u"comboBoxArticle")

        self.gridLayout.addWidget(self.comboBoxArticle, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 3, 1, 1)

        self.DateDelivery = QCalendarWidget(OrderDialog)
        self.DateDelivery.setObjectName(u"DateDelivery")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        self.DateDelivery.setFont(font)

        self.gridLayout.addWidget(self.DateDelivery, 6, 1, 1, 1)

        self.comboBoxLocation = QComboBox(OrderDialog)
        self.comboBoxLocation.setObjectName(u"comboBoxLocation")

        self.gridLayout.addWidget(self.comboBoxLocation, 4, 1, 1, 1)

        self.comboBoxStatus = QComboBox(OrderDialog)
        self.comboBoxStatus.setObjectName(u"comboBoxStatus")

        self.gridLayout.addWidget(self.comboBoxStatus, 3, 1, 1, 1)

        self.Save = QPushButton(OrderDialog)
        self.Save.setObjectName(u"Save")

        self.gridLayout.addWidget(self.Save, 7, 1, 1, 1)


        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"\u0417\u0430\u043a\u0430\u0437", None))
        self.Save.setText(QCoreApplication.translate("OrderDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

