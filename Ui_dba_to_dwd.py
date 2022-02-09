# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/xxx/Downloads/工作资料/dba_to_dwd_tools/dba_to_dwd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 520)
        MainWindow.setMinimumSize(QtCore.QSize(684, 520))
        MainWindow.setMaximumSize(QtCore.QSize(684, 520))
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_dba = QtWidgets.QLabel(self.centralwidget)
        self.label_dba.setGeometry(QtCore.QRect(25, 155, 111, 16))
        self.label_dba.setObjectName("label_dba")
        self.label_dwd = QtWidgets.QLabel(self.centralwidget)
        self.label_dwd.setGeometry(QtCore.QRect(385, 155, 111, 16))
        self.label_dwd.setObjectName("label_dwd")
        self.pushButton_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_transfer.setGeometry(QtCore.QRect(289, 255, 75, 28))
        self.pushButton_transfer.setObjectName("pushButton_transfer")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(289, 290, 75, 28))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_savePath = QtWidgets.QLabel(self.centralwidget)
        self.label_savePath.setGeometry(QtCore.QRect(30, 20, 52, 18))
        self.label_savePath.setObjectName("label_savePath")
        self.lineEdit_savePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_savePath.setGeometry(QtCore.QRect(90, 20, 561, 21))
        self.lineEdit_savePath.setObjectName("lineEdit_savePath")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 136, 631, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(530, 470, 111, 16))
        self.label_author.setStyleSheet("color:gray")
        self.label_author.setObjectName("label_author")
        self.plainTextEdit_dba = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_dba.setGeometry(QtCore.QRect(15, 180, 270, 280))
        self.plainTextEdit_dba.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_dba.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_dba.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_dba.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_dba.setObjectName("plainTextEdit_dba")
        self.plainTextEdit_dwd = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_dwd.setGeometry(QtCore.QRect(370, 180, 270, 280))
        self.plainTextEdit_dwd.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_dwd.setObjectName("plainTextEdit_dwd")
        self.label_sysName = QtWidgets.QLabel(self.centralwidget)
        self.label_sysName.setGeometry(QtCore.QRect(30, 50, 52, 18))
        self.label_sysName.setObjectName("label_sysName")
        self.lineEdit_sysName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sysName.setGeometry(QtCore.QRect(90, 50, 561, 21))
        self.lineEdit_sysName.setObjectName("lineEdit_sysName")
        self.label_databaseType = QtWidgets.QLabel(self.centralwidget)
        self.label_databaseType.setGeometry(QtCore.QRect(30, 110, 52, 18))
        self.label_databaseType.setObjectName("label_databaseType")
        self.radioButton_mysql = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_mysql.setGeometry(QtCore.QRect(90, 110, 100, 20))
        self.radioButton_mysql.setChecked(True)
        self.radioButton_mysql.setObjectName("radioButton_mysql")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_mysql)
        self.radioButton_oracle = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_oracle.setGeometry(QtCore.QRect(170, 110, 100, 20))
        self.radioButton_oracle.setChecked(False)
        self.radioButton_oracle.setObjectName("radioButton_oracle")
        self.buttonGroup.addButton(self.radioButton_oracle)
        self.label_tbName = QtWidgets.QLabel(self.centralwidget)
        self.label_tbName.setGeometry(QtCore.QRect(30, 80, 52, 18))
        self.label_tbName.setObjectName("label_tbName")
        self.lineEdit_tbName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tbName.setGeometry(QtCore.QRect(90, 80, 561, 21))
        self.lineEdit_tbName.setReadOnly(True)
        self.lineEdit_tbName.setObjectName("lineEdit_tbName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBA_to_DWD建表转换工具"))
        self.label_dba.setText(_translate("MainWindow", "DBA建表语句"))
        self.label_dwd.setText(_translate("MainWindow", "DWD建表语句"))
        self.pushButton_transfer.setText(_translate("MainWindow", ">>"))
        self.pushButton_save.setText(_translate("MainWindow", "save"))
        self.label_savePath.setText(_translate("MainWindow", "保存路径"))
        self.label_author.setText(_translate("MainWindow", "Author: zenanhe"))
        self.label_sysName.setText(_translate("MainWindow", "系统名称"))
        self.label_databaseType.setText(_translate("MainWindow", "源库类型"))
        self.radioButton_mysql.setText(_translate("MainWindow", "MySQL"))
        self.radioButton_oracle.setText(_translate("MainWindow", "Oracle"))
        self.label_tbName.setText(_translate("MainWindow", "解析表名"))
