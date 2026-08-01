# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchVillagerWidget.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SearchVillager(object):
    def setupUi(self, SearchVillager):
        if not SearchVillager.objectName():
            SearchVillager.setObjectName(u"SearchVillager")
        SearchVillager.setEnabled(True)
        SearchVillager.resize(970, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchVillager.sizePolicy().hasHeightForWidth())
        SearchVillager.setSizePolicy(sizePolicy)
        SearchVillager.setMinimumSize(QSize(960, 570))
        SearchVillager.setMaximumSize(QSize(970, 570))
        self.layoutWidget = QWidget(SearchVillager)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, 0, 982, 585))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.posX = QSpinBox(self.layoutWidget)
        self.posX.setObjectName(u"posX")
        sizePolicy.setHeightForWidth(self.posX.sizePolicy().hasHeightForWidth())
        self.posX.setSizePolicy(sizePolicy)
        self.posX.setMinimumSize(QSize(80, 30))
        self.posX.setMaximumSize(QSize(80, 30))
        self.posX.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posX.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posX.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posX.setMinimum(-30000000)
        self.posX.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posX)

        self.posY = QSpinBox(self.layoutWidget)
        self.posY.setObjectName(u"posY")
        sizePolicy.setHeightForWidth(self.posY.sizePolicy().hasHeightForWidth())
        self.posY.setSizePolicy(sizePolicy)
        self.posY.setMinimumSize(QSize(80, 30))
        self.posY.setMaximumSize(QSize(80, 30))
        self.posY.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posY.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posY.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posY.setMinimum(-30000000)
        self.posY.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posY)

        self.posZ = QSpinBox(self.layoutWidget)
        self.posZ.setObjectName(u"posZ")
        sizePolicy.setHeightForWidth(self.posZ.sizePolicy().hasHeightForWidth())
        self.posZ.setSizePolicy(sizePolicy)
        self.posZ.setMinimumSize(QSize(80, 30))
        self.posZ.setMaximumSize(QSize(80, 30))
        self.posZ.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posZ.setToolTipDuration(-1)
        self.posZ.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posZ.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posZ.setMinimum(-30000000)
        self.posZ.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posZ)

        self.searchButton = QPushButton(self.layoutWidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QSize(60, 30))
        self.searchButton.setMaximumSize(QSize(60, 30))
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton.setCheckable(False)

        self.horizontalLayout.addWidget(self.searchButton)

        self.horizontalSpacer = QSpacerItem(130, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.villagerSelector = QComboBox(self.layoutWidget)
        self.villagerSelector.setObjectName(u"villagerSelector")
        sizePolicy.setHeightForWidth(self.villagerSelector.sizePolicy().hasHeightForWidth())
        self.villagerSelector.setSizePolicy(sizePolicy)
        self.villagerSelector.setMinimumSize(QSize(460, 30))
        self.villagerSelector.setMaximumSize(QSize(460, 30))
        self.villagerSelector.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.villagerSelector)

        self.horizontalLayout.setStretch(0, 80)
        self.horizontalLayout.setStretch(1, 80)
        self.horizontalLayout.setStretch(2, 80)
        self.horizontalLayout.setStretch(3, 60)
        self.horizontalLayout.setStretch(4, 130)
        self.horizontalLayout.setStretch(5, 460)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.modifyVillagerLayout = QVBoxLayout()
        self.modifyVillagerLayout.setSpacing(0)
        self.modifyVillagerLayout.setObjectName(u"modifyVillagerLayout")

        self.verticalLayout.addLayout(self.modifyVillagerLayout)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 540)

        self.retranslateUi(SearchVillager)

        QMetaObject.connectSlotsByName(SearchVillager)
    # setupUi

    def retranslateUi(self, SearchVillager):
        SearchVillager.setWindowTitle(QCoreApplication.translate("SearchVillager", u"searchVillager", None))
        self.searchButton.setText(QCoreApplication.translate("SearchVillager", u"\u641c\u5c0b", None))
    # retranslateUi

