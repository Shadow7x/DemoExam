# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrameCinema.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FrameCinema(object):
    def setupUi(self, FrameCinema):
        if not FrameCinema.objectName():
            FrameCinema.setObjectName(u"FrameCinema")
        FrameCinema.resize(650, 168)
        FrameCinema.setMinimumSize(QSize(650, 0))
        FrameCinema.setMaximumSize(QSize(650, 16777215))
        FrameCinema.setBaseSize(QSize(650, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        FrameCinema.setFont(font)
        self.horizontalLayout = QHBoxLayout(FrameCinema)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Image = QLabel(FrameCinema)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(150, 150))
        self.Image.setMaximumSize(QSize(150, 150))
        self.Image.setBaseSize(QSize(150, 150))
        self.Image.setFont(font)
        self.Image.setPixmap(QPixmap(u"../../picture.png"))
        self.Image.setScaledContents(True)

        self.horizontalLayout.addWidget(self.Image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Name = QLabel(FrameCinema)
        self.Name.setObjectName(u"Name")

        self.verticalLayout.addWidget(self.Name)

        self.Producer = QLabel(FrameCinema)
        self.Producer.setObjectName(u"Producer")

        self.verticalLayout.addWidget(self.Producer)

        self.Genre = QLabel(FrameCinema)
        self.Genre.setObjectName(u"Genre")

        self.verticalLayout.addWidget(self.Genre)

        self.Description = QLabel(FrameCinema)
        self.Description.setObjectName(u"Description")
        self.Description.setWordWrap(True)

        self.verticalLayout.addWidget(self.Description)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(FrameCinema)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.OldPrice = QLabel(FrameCinema)
        self.OldPrice.setObjectName(u"OldPrice")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setStrikeOut(True)
        self.OldPrice.setFont(font1)
        self.OldPrice.setStyleSheet(u"color:red")

        self.horizontalLayout_2.addWidget(self.OldPrice)

        self.NewPrice = QLabel(FrameCinema)
        self.NewPrice.setObjectName(u"NewPrice")

        self.horizontalLayout_2.addWidget(self.NewPrice)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.Count = QLabel(FrameCinema)
        self.Count.setObjectName(u"Count")

        self.verticalLayout.addWidget(self.Count)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Discount = QLabel(FrameCinema)
        self.Discount.setObjectName(u"Discount")

        self.verticalLayout_2.addWidget(self.Discount)

        self.Update = QPushButton(FrameCinema)
        self.Update.setObjectName(u"Update")

        self.verticalLayout_2.addWidget(self.Update)

        self.Delete = QPushButton(FrameCinema)
        self.Delete.setObjectName(u"Delete")

        self.verticalLayout_2.addWidget(self.Delete)

        self.pushButton = QPushButton(FrameCinema)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(FrameCinema)

        QMetaObject.connectSlotsByName(FrameCinema)
    # setupUi

    def retranslateUi(self, FrameCinema):
        FrameCinema.setWindowTitle(QCoreApplication.translate("FrameCinema", u"Frame", None))
        self.Image.setText("")
        self.Name.setText(QCoreApplication.translate("FrameCinema", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ", None))
        self.Producer.setText(QCoreApplication.translate("FrameCinema", u"\u0420\u0435\u0436\u0438\u0441\u0435\u0440: ", None))
        self.Genre.setText(QCoreApplication.translate("FrameCinema", u"\u0416\u0430\u043d\u0440: ", None))
        self.Description.setText(QCoreApplication.translate("FrameCinema", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: ", None))
        self.label_5.setText(QCoreApplication.translate("FrameCinema", u"\u0426\u0435\u043d\u0430:", None))
        self.OldPrice.setText(QCoreApplication.translate("FrameCinema", u"TextLabel", None))
        self.NewPrice.setText(QCoreApplication.translate("FrameCinema", u"TextLabel", None))
        self.Count.setText(QCoreApplication.translate("FrameCinema", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0432\u0442\u043e \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0445 \u043c\u0435\u0441\u0442: ", None))
        self.Discount.setText(QCoreApplication.translate("FrameCinema", u" %", None))
        self.Update.setText(QCoreApplication.translate("FrameCinema", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("FrameCinema", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("FrameCinema", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

