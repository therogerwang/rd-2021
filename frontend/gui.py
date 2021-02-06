from PyQt5 import QtCore, QtGui, QtWidgets
import backend.main as bm


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 652)
        MainWindow.setStyleSheet("background-color:rgb(42, 57, 144)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 341, 71))
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 321, 31))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 210, 281, 24))
        self.lineEdit.setStyleSheet("color:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 110, 341, 31))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 160, 341, 451))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 121, 32))
        self.pushButton.setStyleSheet("color:rgb(42, 57, 144);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "recommendr"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">recommendr</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<h2>Enter your business name</h2>"))
        self.label_3.setText(_translate("MainWindow", "<h2>Your Top Recommendations</h2>"))
        self.label_3.hide()
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">item1<br/><br/>item2<br/><br/>item3<br/><br/>item4<br/><br/>item5<br/><br/>item6<br/><br/>item7<br/><br/>item8<br/><br/>item9<br/><br/>item10</span></p></body></html>"))
        self.label_4.hide()
        self.pushButton.setText(_translate("MainWindow", "Recommend!"))
        self.pushButton.clicked.connect(self.btn_down)

    def btn_down(self):
        busi_name = self.lineEdit.text()
        recs = bm.recommend(busi_name)
        recs_str = self.to_html(recs)
        self.label_4.setText(recs_str)
        self.label_3.show()
        self.label_4.show()

    def to_html(self, arr):
        ret_str = "<html><head/><body><p><span style=\" font-size:10pt;\">"

        arr_len = len(arr)
        for i in range(arr_len):
            ret_str += arr[i]
            if i < arr_len - 1:
                ret_str += "<br/><br/>"

        ret_str += "</span></p></body></html>"
        return ret_str


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
