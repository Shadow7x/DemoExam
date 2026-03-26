# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductsWindow.ui'
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

class Ui_ProductsWindow(object):
    def setupUi(self, ProductsWindow):
        if not ProductsWindow.objectName():
            ProductsWindow.setObjectName(u"ProductsWindow")
        ProductsWindow.resize(869, 597)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        ProductsWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../../time/import/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ProductsWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(ProductsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 515))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 1, 1, 1)

        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout_2.addWidget(self.Exit)

        self.CreateProduct = QPushButton(self.centralwidget)
        self.CreateProduct.setObjectName(u"CreateProduct")

        self.verticalLayout_2.addWidget(self.CreateProduct)

        self.Orders = QPushButton(self.centralwidget)
        self.Orders.setObjectName(u"Orders")

        self.verticalLayout_2.addWidget(self.Orders)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Search = QLineEdit(self.centralwidget)
        self.Search.setObjectName(u"Search")

        self.horizontalLayout.addWidget(self.Search)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

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

        ProductsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductsWindow)

        QMetaObject.connectSlotsByName(ProductsWindow)
    # setupUi

    def retranslateUi(self, ProductsWindow):
        ProductsWindow.setWindowTitle(QCoreApplication.translate("ProductsWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.FIO.setText(QCoreApplication.translate("ProductsWindow", u"FIO", None))
        self.Exit.setText(QCoreApplication.translate("ProductsWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.CreateProduct.setText(QCoreApplication.translate("ProductsWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.Orders.setText(QCoreApplication.translate("ProductsWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.label.setText(QCoreApplication.translate("ProductsWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("ProductsWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("ProductsWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

