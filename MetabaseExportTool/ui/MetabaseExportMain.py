# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MetabaseExportMain.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 382)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dbSourceToMigrate = QtWidgets.QLineEdit(self.tab)
        self.dbSourceToMigrate.setObjectName("dbSourceToMigrate")
        self.gridLayout.addWidget(self.dbSourceToMigrate, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.databaseToMigrate = QtWidgets.QSpinBox(self.tab)
        self.databaseToMigrate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.databaseToMigrate.setObjectName("databaseToMigrate")
        self.horizontalLayout_2.addWidget(self.databaseToMigrate)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.collectionToMigrate = QtWidgets.QSpinBox(self.tab)
        self.collectionToMigrate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.collectionToMigrate.setObjectName("collectionToMigrate")
        self.horizontalLayout.addWidget(self.collectionToMigrate)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.dbTargetToMigrate = QtWidgets.QLineEdit(self.tab)
        self.dbTargetToMigrate.setObjectName("dbTargetToMigrate")
        self.gridLayout_2.addWidget(self.dbTargetToMigrate, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.changeToDatabaseId = QtWidgets.QSpinBox(self.tab)
        self.changeToDatabaseId.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.changeToDatabaseId.setObjectName("changeToDatabaseId")
        self.horizontalLayout_3.addWidget(self.changeToDatabaseId)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 3, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 4, 0, 1, 1)
        self.Migrate = QtWidgets.QPushButton(self.tab)
        self.Migrate.setObjectName("Migrate")
        self.gridLayout_5.addWidget(self.Migrate, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.databaseToExport = QtWidgets.QSpinBox(self.tab_2)
        self.databaseToExport.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.databaseToExport.setObjectName("databaseToExport")
        self.horizontalLayout_4.addWidget(self.databaseToExport)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)
        self.dbSourceToExport = QtWidgets.QLineEdit(self.tab_2)
        self.dbSourceToExport.setObjectName("dbSourceToExport")
        self.gridLayout_3.addWidget(self.dbSourceToExport, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 4, 1, 1, 1)
        self.Export = QtWidgets.QPushButton(self.tab_2)
        self.Export.setObjectName("Export")
        self.gridLayout_3.addWidget(self.Export, 4, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.collectionToExport = QtWidgets.QSpinBox(self.tab_2)
        self.collectionToExport.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.collectionToExport.setObjectName("collectionToExport")
        self.horizontalLayout_5.addWidget(self.collectionToExport)
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.changeToSchemaName = QtWidgets.QLineEdit(self.tab_2)
        self.changeToSchemaName.setObjectName("changeToSchemaName")
        self.gridLayout_3.addWidget(self.changeToSchemaName, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dbTargetToDelete = QtWidgets.QLineEdit(self.tab_3)
        self.dbTargetToDelete.setObjectName("dbTargetToDelete")
        self.gridLayout_4.addWidget(self.dbTargetToDelete, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.collectionToDelete = QtWidgets.QSpinBox(self.tab_3)
        self.collectionToDelete.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.collectionToDelete.setObjectName("collectionToDelete")
        self.horizontalLayout_7.addWidget(self.collectionToDelete)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.databaseToDelete = QtWidgets.QSpinBox(self.tab_3)
        self.databaseToDelete.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.databaseToDelete.setObjectName("databaseToDelete")
        self.horizontalLayout_6.addWidget(self.databaseToDelete)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 2, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 3, 1, 1, 1)
        self.Delete = QtWidgets.QPushButton(self.tab_3)
        self.Delete.setObjectName("Delete")
        self.gridLayout_4.addWidget(self.Delete, 3, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.outputLog = QtWidgets.QTextEdit(self.centralwidget)
        self.outputLog.setEnabled(True)
        self.outputLog.setReadOnly(True)
        self.outputLog.setObjectName("outputLog")
        self.verticalLayout.addWidget(self.outputLog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metabase Export Tool"))
        self.label_6.setText(_translate("MainWindow", "Source"))
        self.dbSourceToMigrate.setText(_translate("MainWindow", "metabase"))
        self.label_4.setText(_translate("MainWindow", "Database to migrate"))
        self.label_3.setText(_translate("MainWindow", "Collection to migrate"))
        self.label.setText(_translate("MainWindow", "Source Database"))
        self.label_7.setText(_translate("MainWindow", "Target"))
        self.label_2.setText(_translate("MainWindow", "Target Database"))
        self.label_5.setText(_translate("MainWindow", "Change to Database Id"))
        self.dbTargetToMigrate.setText(_translate("MainWindow", "metabase_target"))
        self.Migrate.setText(_translate("MainWindow", "Migrate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Migrate"))
        self.dbSourceToExport.setText(_translate("MainWindow", "metabase"))
        self.label_8.setText(_translate("MainWindow", "Database to export"))
        self.Export.setText(_translate("MainWindow", "Export"))
        self.label_9.setText(_translate("MainWindow", "Collection to export"))
        self.label_10.setText(_translate("MainWindow", "Source Database"))
        self.label_14.setText(_translate("MainWindow", "Change schema name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Export"))
        self.dbTargetToDelete.setText(_translate("MainWindow", "metabase_target"))
        self.label_11.setText(_translate("MainWindow", "Database to delete"))
        self.label_13.setText(_translate("MainWindow", "Target Database"))
        self.label_12.setText(_translate("MainWindow", "Collection to delete"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Delete"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
