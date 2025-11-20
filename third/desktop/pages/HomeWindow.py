# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(865, 600)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        HomeWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/Icon.JPG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        HomeWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout.addWidget(self.Exit)

        self.AddProduct = QPushButton(self.centralwidget)
        self.AddProduct.setObjectName(u"AddProduct")

        self.verticalLayout.addWidget(self.AddProduct)

        self.Orders = QPushButton(self.centralwidget)
        self.Orders.setObjectName(u"Orders")

        self.verticalLayout.addWidget(self.Orders)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 682, 518))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Search = QLineEdit(self.centralwidget)
        self.Search.setObjectName(u"Search")

        self.horizontalLayout.addWidget(self.Search)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxSort = QComboBox(self.centralwidget)
        self.comboBoxSort.setObjectName(u"comboBoxSort")

        self.horizontalLayout.addWidget(self.comboBoxSort)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBoxFilter = QComboBox(self.centralwidget)
        self.comboBoxFilter.setObjectName(u"comboBoxFilter")

        self.horizontalLayout.addWidget(self.comboBoxFilter)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 1, 1, 1)

        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.Exit.setText(QCoreApplication.translate("HomeWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.AddProduct.setText(QCoreApplication.translate("HomeWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.Orders.setText(QCoreApplication.translate("HomeWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.label_2.setText(QCoreApplication.translate("HomeWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("HomeWindow", u"\u041e\u0442\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("HomeWindow", u"\u041e\u0442\u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e", None))
        self.FIO.setText("")
    # retranslateUi

