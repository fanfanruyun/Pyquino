# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kmol/桌面/Pyquino/core/vrep/vrep_setting.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(797, 512)
        Dialog.setSizeGripEnabled(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMaximumSize(QtCore.QSize(420, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.xAxisrigh = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxisrigh.sizePolicy().hasHeightForWidth())
        self.xAxisrigh.setSizePolicy(sizePolicy)
        self.xAxisrigh.setMinimumSize(QtCore.QSize(125, 50))
        self.xAxisrigh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/arrow-right-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisrigh.setIcon(icon)
        self.xAxisrigh.setIconSize(QtCore.QSize(30, 30))
        self.xAxisrigh.setObjectName("xAxisrigh")
        self.gridLayout.addWidget(self.xAxisrigh, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        self.yAxisup = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAxisup.sizePolicy().hasHeightForWidth())
        self.yAxisup.setSizePolicy(sizePolicy)
        self.yAxisup.setMinimumSize(QtCore.QSize(125, 50))
        self.yAxisup.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arrow-up-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisup.setIcon(icon1)
        self.yAxisup.setIconSize(QtCore.QSize(30, 30))
        self.yAxisup.setObjectName("yAxisup")
        self.gridLayout.addWidget(self.yAxisup, 0, 1, 1, 1)
        self.yAxisdown = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAxisdown.sizePolicy().hasHeightForWidth())
        self.yAxisdown.setSizePolicy(sizePolicy)
        self.yAxisdown.setMinimumSize(QtCore.QSize(125, 50))
        self.yAxisdown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow-down-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisdown.setIcon(icon2)
        self.yAxisdown.setIconSize(QtCore.QSize(30, 30))
        self.yAxisdown.setObjectName("yAxisdown")
        self.gridLayout.addWidget(self.yAxisdown, 2, 1, 1, 1)
        self.xAxisleft = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxisleft.sizePolicy().hasHeightForWidth())
        self.xAxisleft.setSizePolicy(sizePolicy)
        self.xAxisleft.setMinimumSize(QtCore.QSize(125, 50))
        self.xAxisleft.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/arrow-left-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisleft.setIcon(icon3)
        self.xAxisleft.setIconSize(QtCore.QSize(30, 30))
        self.xAxisleft.setObjectName("xAxisleft")
        self.gridLayout.addWidget(self.xAxisleft, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.stepbox = QtWidgets.QSpinBox(self.widget)
        self.stepbox.setMaximum(100)
        self.stepbox.setSingleStep(0)
        self.stepbox.setProperty("value", 10)
        self.stepbox.setObjectName("stepbox")
        self.horizontalLayout_2.addWidget(self.stepbox)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.unlockMachine = QtWidgets.QPushButton(self.widget)
        self.unlockMachine.setObjectName("unlockMachine")
        self.verticalLayout_3.addWidget(self.unlockMachine)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openGcodeFile = QtWidgets.QPushButton(Dialog)
        self.openGcodeFile.setObjectName("openGcodeFile")
        self.horizontalLayout.addWidget(self.openGcodeFile)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.gcodeList = QtWidgets.QListWidget(Dialog)
        self.gcodeList.setObjectName("gcodeList")
        self.verticalLayout_2.addWidget(self.gcodeList)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "step"))
        self.label_12.setText(_translate("Dialog", "mm"))
        self.unlockMachine.setText(_translate("Dialog", "connect"))
        self.openGcodeFile.setText(_translate("Dialog", "Open"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

