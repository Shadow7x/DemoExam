# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow):
        if not ProductWindow.objectName():
            ProductWindow.setObjectName(u"ProductWindow")
        ProductWindow.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        ProductWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ProductWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(ProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 553))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout.addWidget(self.Exit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 2, 1, 1)

        ProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductWindow)

        QMetaObject.connectSlotsByName(ProductWindow)
    # setupUi

    def retranslateUi(self, ProductWindow):
        ProductWindow.setWindowTitle(QCoreApplication.translate("ProductWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.Exit.setText(QCoreApplication.translate("ProductWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.FIO.setText("")
    # retranslateUi

