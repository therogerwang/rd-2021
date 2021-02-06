import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

class MyWindow:
    def __init__(self, win):
        helloMsg = QLabel('<h1>Hello World!</h1>', parent=win)
        helloMsg.move(60, 15)


app = QApplication(sys.argv)
window = QWidget()
my_win = MyWindow(window)

window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 1000, 600)
window.move(60, 15)

window.show()
sys.exit(app.exec_())