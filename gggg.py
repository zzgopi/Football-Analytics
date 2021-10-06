from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
	app=QApplication(sys.argv)
	win=QMainWindow()
	win.setGeometry(500,500,10,10)
	
	label= QtWidgets.QLabel(win)

	label.setText('testing')
	label.move(50,50)
	win.show()
	sys.exit(app.exec_())

window()