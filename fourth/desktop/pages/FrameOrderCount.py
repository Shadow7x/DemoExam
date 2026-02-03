# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrderCount.ui'
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
    QSizePolicy, QSpinBox, QWidget)

class Ui_FrameOrderCount(object):
    def setupUi(self, FrameOrderCount):
        if not FrameOrderCount.objectName():
            FrameOrderCount.setObjectName(u"FrameOrderCount")
        FrameOrderCount.resize(278, 45)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        FrameOrderCount.setFont(font)
        self.horizontalLayout = QHBoxLayout(FrameOrderCount)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Article = QLabel(FrameOrderCount)
        self.Article.setObjectName(u"Article")
        self.Article.setFont(font)

        self.horizontalLayout.addWidget(self.Article)

        self.Count = QSpinBox(FrameOrderCount)
        self.Count.setObjectName(u"Count")

        self.horizontalLayout.addWidget(self.Count)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(FrameOrderCount)

        QMetaObject.connectSlotsByName(FrameOrderCount)
    # setupUi

    def retranslateUi(self, FrameOrderCount):
        FrameOrderCount.setWindowTitle(QCoreApplication.translate("FrameOrderCount", u"Frame", None))
        self.Article.setText(QCoreApplication.translate("FrameOrderCount", u"TextLabel", None))
    # retranslateUi

