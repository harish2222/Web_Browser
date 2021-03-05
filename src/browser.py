import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        
        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction

App = QApplication(sys.argv)
QApplication.setApplicationName("TOR Borwser")
window = MainWindow()
App.exec_()



