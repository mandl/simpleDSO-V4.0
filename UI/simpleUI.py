# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(658, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon2/icon2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gwScreen = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gwScreen.sizePolicy().hasHeightForWidth())
        self.gwScreen.setSizePolicy(sizePolicy)
        self.gwScreen.setMinimumSize(QtCore.QSize(640, 480))
        self.gwScreen.setMaximumSize(QtCore.QSize(640, 480))
        self.gwScreen.setInteractive(True)
        self.gwScreen.setObjectName(_fromUtf8("gwScreen"))
        self.verticalLayout_2.addWidget(self.gwScreen)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.updateValue = QtGui.QSpinBox(self.groupBox_2)
        self.updateValue.setMinimum(50)
        self.updateValue.setMaximum(9999)
        self.updateValue.setProperty("value", 1000)
        self.updateValue.setObjectName(_fromUtf8("updateValue"))
        self.horizontalLayout_2.addWidget(self.updateValue)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuAction.addAction(self.actionAbout)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionExit)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL(_fromUtf8("triggered(QAction*)")), MainWindow.processAction)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.loadDataFromDso)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.loadScreenFromDso)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveProgramScreen)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.setAutoUpdate)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.updateValue.setEnabled)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox.setChecked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveDataToCSV)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.loadDataFromDso)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DSO screenshoter", None))
        self.groupBox.setTitle(_translate("MainWindow", "Actions", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Loads data from DSO and paint wave by yourselves", None))
        self.pushButton.setText(_translate("MainWindow", "Load data from DSO", None))
        self.pushButton_4.setText(_translate("MainWindow", "Save data to CSV", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Load screen data from DSO and paint them to program view", None))
        self.pushButton_2.setText(_translate("MainWindow", "Screenshot from DSO", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Save programs view to file", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save program screen", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings", None))
        self.checkBox.setText(_translate("MainWindow", "Auto load data from DSO", None))
        self.updateValue.setSuffix(_translate("MainWindow", "ms", None))
        self.menuAction.setTitle(_translate("MainWindow", "Action", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

