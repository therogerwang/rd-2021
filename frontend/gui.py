import sys

import backend.main as bm
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot


class MyWindow:

    def __init__(self, win):
        self.win = win

        self.titlelbl = QLabel("<h1>RecommendMe</h1>", win)
        self.titlelbl.move(60, 15)

        self.entrylbl = QLabel("<h2>Enter your business name</h2>", win)
        self.entrylbl.move(75, 90)

        self.entrybox = QLineEdit(win)
        self.entrybox.setFont(QFont("Arial, 13"))
        self.entrybox.move(75, 130)

        self.btn = QPushButton(win)
        self.btn.setText("Recommend!")
        self.btn.move(75, 160)
        self.btn.clicked.connect(self.btn_down)

        self.teset = QLabel(win)
        self.teset.move(500, 500)

    def btn_down(self):
        print("HI")
        busi_name = self.entrybox.text()
        recs = bm.recommend(busi_name)

        self.teset.setText(recs)

        # transform return into html before calling below
        resulttitlelbl = QLabel("<h2>Your Top Recommendations</h2>", self.win)
        resulttitlelbl.move(600, 90)

        resultlbl = QLabel(recs, self.win)
        resultlbl.move(600, 135)


app = QApplication(sys.argv)
window = QWidget()
my_win = MyWindow(window)

window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 1000, 600)
window.move(60, 15)

window.show()
sys.exit(app.exec_())