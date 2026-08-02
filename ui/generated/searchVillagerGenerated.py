# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchVillagerDesign.ui'
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
        self.posXSpinBox = QSpinBox(self.layoutWidget)
        self.posXSpinBox.setObjectName(u"posXSpinBox")
        sizePolicy.setHeightForWidth(self.posXSpinBox.sizePolicy().hasHeightForWidth())
        self.posXSpinBox.setSizePolicy(sizePolicy)
        self.posXSpinBox.setMinimumSize(QSize(80, 30))
        self.posXSpinBox.setMaximumSize(QSize(80, 30))
        self.posXSpinBox.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posXSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posXSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posXSpinBox.setMinimum(-30000000)
        self.posXSpinBox.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posXSpinBox)

        self.posYSpinBox = QSpinBox(self.layoutWidget)
        self.posYSpinBox.setObjectName(u"posYSpinBox")
        sizePolicy.setHeightForWidth(self.posYSpinBox.sizePolicy().hasHeightForWidth())
        self.posYSpinBox.setSizePolicy(sizePolicy)
        self.posYSpinBox.setMinimumSize(QSize(80, 30))
        self.posYSpinBox.setMaximumSize(QSize(80, 30))
        self.posYSpinBox.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posYSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posYSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posYSpinBox.setMinimum(-30000000)
        self.posYSpinBox.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posYSpinBox)

        self.posZSpinBox = QSpinBox(self.layoutWidget)
        self.posZSpinBox.setObjectName(u"posZSpinBox")
        sizePolicy.setHeightForWidth(self.posZSpinBox.sizePolicy().hasHeightForWidth())
        self.posZSpinBox.setSizePolicy(sizePolicy)
        self.posZSpinBox.setMinimumSize(QSize(80, 30))
        self.posZSpinBox.setMaximumSize(QSize(80, 30))
        self.posZSpinBox.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.posZSpinBox.setToolTipDuration(-1)
        self.posZSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.posZSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.posZSpinBox.setMinimum(-30000000)
        self.posZSpinBox.setMaximum(30000000)

        self.horizontalLayout.addWidget(self.posZSpinBox)

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

        self.librarianSelectorComboBox = QComboBox(self.layoutWidget)
        self.librarianSelectorComboBox.setObjectName(u"librarianSelectorComboBox")
        sizePolicy.setHeightForWidth(self.librarianSelectorComboBox.sizePolicy().hasHeightForWidth())
        self.librarianSelectorComboBox.setSizePolicy(sizePolicy)
        self.librarianSelectorComboBox.setMinimumSize(QSize(460, 30))
        self.librarianSelectorComboBox.setMaximumSize(QSize(460, 30))
        self.librarianSelectorComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.librarianSelectorComboBox)

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

