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
    QGridLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(673, 792)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        OrderDialog.setFont(font)
        self.gridLayout = QGridLayout(OrderDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(OrderDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 489, 175))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 6, 1, 1, 2)

        self.Date = QCalendarWidget(OrderDialog)
        self.Date.setObjectName(u"Date")
        font1 = QFont()
        font1.setPointSize(8)
        self.Date.setFont(font1)

        self.gridLayout.addWidget(self.Date, 4, 2, 1, 1)

        self.DateDelivery = QCalendarWidget(OrderDialog)
        self.DateDelivery.setObjectName(u"DateDelivery")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(9)
        self.DateDelivery.setFont(font2)

        self.gridLayout.addWidget(self.DateDelivery, 5, 2, 1, 1)

        self.comboBoxFIO = QComboBox(OrderDialog)
        self.comboBoxFIO.setObjectName(u"comboBoxFIO")

        self.gridLayout.addWidget(self.comboBoxFIO, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.comboBoxAddress = QComboBox(OrderDialog)
        self.comboBoxAddress.setObjectName(u"comboBoxAddress")

        self.gridLayout.addWidget(self.comboBoxAddress, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label = QLabel(OrderDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_4 = QLabel(OrderDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_3 = QLabel(OrderDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_5 = QLabel(OrderDialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.comboBoxStatus = QComboBox(OrderDialog)
        self.comboBoxStatus.setObjectName(u"comboBoxStatus")

        self.gridLayout.addWidget(self.comboBoxStatus, 2, 2, 1, 1)

        self.label_2 = QLabel(OrderDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.Save = QPushButton(OrderDialog)
        self.Save.setObjectName(u"Save")

        self.gridLayout.addWidget(self.Save, 7, 1, 1, 2)

        self.gridLayout.setRowStretch(6, 1)

        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("OrderDialog", u"\u0424\u0418\u041e \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("OrderDialog", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_3.setText(QCoreApplication.translate("OrderDialog", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u0442\u043a\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_5.setText(QCoreApplication.translate("OrderDialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_2.setText(QCoreApplication.translate("OrderDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.Save.setText(QCoreApplication.translate("OrderDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

