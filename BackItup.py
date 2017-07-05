# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QFileDialog
from Controller import Controller
from PopUp import Ui_Dialog

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


class Ui_Form(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.popup = Ui_Dialog()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("BackItUp"))
        Form.setFixedSize(402, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.fromfile = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromfile.sizePolicy().hasHeightForWidth())
        self.fromfile.setSizePolicy(sizePolicy)
        self.fromfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fromfile.setObjectName(_fromUtf8("fromfile"))
        self.verticalLayout.addWidget(self.fromfile)
        self.fromfile.clicked.connect(self.Search_For_Doc)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.tobutton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tobutton.sizePolicy().hasHeightForWidth())
        self.tobutton.setSizePolicy(sizePolicy)
        self.tobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tobutton.setObjectName(_fromUtf8("tobutton"))
        self.verticalLayout.addWidget(self.tobutton)
        self.tobutton.clicked.connect(self.Search_For_Doc1)
        self.Transfer = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Transfer.sizePolicy().hasHeightForWidth())
        self.Transfer.setSizePolicy(sizePolicy)
        self.Transfer.setObjectName(_fromUtf8("Transfer"))
        self.verticalLayout.addWidget(self.Transfer)
        self.Transfer.clicked.connect(self.Transferit)
        self.control = Controller(self.lineEdit, self.lineEdit_2,self.popup)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "BackItUp", None))
        self.label.setText(_translate("Form", "From:", None))
        self.fromfile.setText(_translate("Form", "Change", None))
        self.label_2.setText(_translate("Form", "To:", None))
        self.tobutton.setText(_translate("Form", "Change", None))
        self.Transfer.setText(_translate("Form", "Transfer", None))

    def Search_For_Doc(self, ):
        filepath = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(filepath)

    def Search_For_Doc1(self, ):
        filepath = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(filepath)

    def Transferit(self):
        self.control.copy_it(self.lineEdit.text(), self.lineEdit_2.text())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
