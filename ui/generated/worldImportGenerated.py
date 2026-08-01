# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorldImportWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_WorldImport(object):
    def setupUi(self, WorldImport):
        if not WorldImport.objectName():
            WorldImport.setObjectName(u"WorldImport")
        WorldImport.resize(960, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WorldImport.sizePolicy().hasHeightForWidth())
        WorldImport.setSizePolicy(sizePolicy)
        WorldImport.setMinimumSize(QSize(960, 30))
        WorldImport.setMaximumSize(QSize(960, 30))
        WorldImport.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.layoutWidget = QWidget(WorldImport)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 961, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.levelFilePath = QLineEdit(self.layoutWidget)
        self.levelFilePath.setObjectName(u"levelFilePath")
        sizePolicy.setHeightForWidth(self.levelFilePath.sizePolicy().hasHeightForWidth())
        self.levelFilePath.setSizePolicy(sizePolicy)
        self.levelFilePath.setMinimumSize(QSize(650, 30))
        self.levelFilePath.setMaximumSize(QSize(650, 30))
        font = QFont()
        font.setPointSize(12)
        self.levelFilePath.setFont(font)
        self.levelFilePath.setPlaceholderText(u"level.dat")

        self.horizontalLayout.addWidget(self.levelFilePath)

        self.browseButton = QPushButton(self.layoutWidget)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setMinimumSize(QSize(30, 30))
        self.browseButton.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setWeight(QFont.Black)
        self.browseButton.setFont(font1)
        self.browseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.browseButton.setAutoRepeat(False)
        self.browseButton.setAutoDefault(False)
        self.browseButton.setFlat(False)

        self.horizontalLayout.addWidget(self.browseButton)

        self.horizontalSpacer = QSpacerItem(170, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QSize(75, 30))
        self.loadButton.setMaximumSize(QSize(75, 30))
        self.loadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loadButton.setCheckable(False)
        self.loadButton.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.loadButton)

        self.horizontalLayout.setStretch(0, 650)
        self.horizontalLayout.setStretch(1, 30)
        self.horizontalLayout.setStretch(2, 170)
        self.horizontalLayout.setStretch(3, 75)

        self.retranslateUi(WorldImport)

        self.browseButton.setDefault(False)


        QMetaObject.connectSlotsByName(WorldImport)
    # setupUi

    def retranslateUi(self, WorldImport):
        WorldImport.setWindowTitle(QCoreApplication.translate("WorldImport", u"WorldImport", None))
        self.browseButton.setText(QCoreApplication.translate("WorldImport", u"...", None))
        self.loadButton.setText(QCoreApplication.translate("WorldImport", u"\u8f09\u5165", None))
    # retranslateUi

