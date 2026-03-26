# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderDeteilsFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QSizePolicy, QSpinBox, QWidget)

class Ui_OrderDetailsFrame(object):
    def setupUi(self, OrderDetailsFrame):
        if not OrderDetailsFrame.objectName():
            OrderDetailsFrame.setObjectName(u"OrderDetailsFrame")
        OrderDetailsFrame.resize(460, 38)
        OrderDetailsFrame.setMinimumSize(QSize(460, 0))
        OrderDetailsFrame.setMaximumSize(QSize(460, 16777215))
        OrderDetailsFrame.setBaseSize(QSize(460, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        OrderDetailsFrame.setFont(font)
        self.horizontalLayout = QHBoxLayout(OrderDetailsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CheckBox = QCheckBox(OrderDetailsFrame)
        self.CheckBox.setObjectName(u"CheckBox")

        self.horizontalLayout.addWidget(self.CheckBox)

        self.Num = QSpinBox(OrderDetailsFrame)
        self.Num.setObjectName(u"Num")

        self.horizontalLayout.addWidget(self.Num)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(OrderDetailsFrame)

        QMetaObject.connectSlotsByName(OrderDetailsFrame)
    # setupUi

    def retranslateUi(self, OrderDetailsFrame):
        OrderDetailsFrame.setWindowTitle(QCoreApplication.translate("OrderDetailsFrame", u"Frame", None))
        self.CheckBox.setText(QCoreApplication.translate("OrderDetailsFrame", u"check box", None))
    # retranslateUi

