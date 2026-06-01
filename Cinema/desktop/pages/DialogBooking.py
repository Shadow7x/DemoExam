# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BookingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_DialogBooking(object):
    def setupUi(self, DialogBooking):
        if not DialogBooking.objectName():
            DialogBooking.setObjectName(u"DialogBooking")
        DialogBooking.resize(400, 300)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        DialogBooking.setFont(font)
        self.gridLayout_2 = QGridLayout(DialogBooking)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(DialogBooking)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)


        self.retranslateUi(DialogBooking)

        QMetaObject.connectSlotsByName(DialogBooking)
    # setupUi

    def retranslateUi(self, DialogBooking):
        DialogBooking.setWindowTitle(QCoreApplication.translate("DialogBooking", u"\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("DialogBooking", u"\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

