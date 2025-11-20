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
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(462, 596)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        OrderDialog.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.JPG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OrderDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(OrderDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(OrderDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.Date = QCalendarWidget(OrderDialog)
        self.Date.setObjectName(u"Date")

        self.gridLayout.addWidget(self.Date, 4, 2, 1, 1)

        self.label_3 = QLabel(OrderDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.comboBoxAddress = QComboBox(OrderDialog)
        self.comboBoxAddress.setObjectName(u"comboBoxAddress")

        self.gridLayout.addWidget(self.comboBoxAddress, 3, 2, 1, 1)

        self.comboBoxStatus = QComboBox(OrderDialog)
        self.comboBoxStatus.setObjectName(u"comboBoxStatus")

        self.gridLayout.addWidget(self.comboBoxStatus, 2, 2, 1, 1)

        self.DateDelivery = QCalendarWidget(OrderDialog)
        self.DateDelivery.setObjectName(u"DateDelivery")

        self.gridLayout.addWidget(self.DateDelivery, 5, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.label_5 = QLabel(OrderDialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.comboBoxArticle = QComboBox(OrderDialog)
        self.comboBoxArticle.setObjectName(u"comboBoxArticle")

        self.gridLayout.addWidget(self.comboBoxArticle, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.label_4 = QLabel(OrderDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_2 = QLabel(OrderDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.Save = QPushButton(OrderDialog)
        self.Save.setObjectName(u"Save")

        self.gridLayout.addWidget(self.Save, 6, 1, 1, 2)


        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"\u0417\u0430\u043a\u0430\u0437", None))
        self.label.setText(QCoreApplication.translate("OrderDialog", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_3.setText(QCoreApplication.translate("OrderDialog", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0443\u043d\u043a\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_5.setText(QCoreApplication.translate("OrderDialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_4.setText(QCoreApplication.translate("OrderDialog", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_2.setText(QCoreApplication.translate("OrderDialog", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.Save.setText(QCoreApplication.translate("OrderDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

