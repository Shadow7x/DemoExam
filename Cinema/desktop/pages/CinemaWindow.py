# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CinemaWindow.ui'
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

class Ui_CinemaWindow(object):
    def setupUi(self, CinemaWindow):
        if not CinemaWindow.objectName():
            CinemaWindow.setObjectName(u"CinemaWindow")
        CinemaWindow.resize(800, 600)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        CinemaWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CinemaWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(CinemaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.FIO = QLabel(self.centralwidget)
        self.FIO.setObjectName(u"FIO")
        self.FIO.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.FIO, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")

        self.verticalLayout.addWidget(self.Exit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 553))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)

        CinemaWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CinemaWindow)

        QMetaObject.connectSlotsByName(CinemaWindow)
    # setupUi

    def retranslateUi(self, CinemaWindow):
        CinemaWindow.setWindowTitle(QCoreApplication.translate("CinemaWindow", u"\u0424\u0438\u043b\u044c\u043c\u044b", None))
        self.FIO.setText(QCoreApplication.translate("CinemaWindow", u"TextLabel", None))
        self.Exit.setText(QCoreApplication.translate("CinemaWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

