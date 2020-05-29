from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import praw
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dad joke finder")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setup = QtWidgets.QLabel(self.centralwidget)
        self.setup.setGeometry(QtCore.QRect(50, 50, 691, 141))
        self.setup.setFont(QFont('Comic Sans MS', 10))
        self.setup.setObjectName("")
        self.setup.setWordWrap(True)

        self.punchline = QtWidgets.QLabel(self.centralwidget)
        self.punchline.setGeometry(QtCore.QRect(50, 170, 691, 211))
        self.punchline.setFont(QFont('Comic Sans MS', 10))
        self.punchline.setObjectName("")
        self.punchline.setWordWrap(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 331, 51))
        self.pushButton.setFont(QFont('Comic Sans MS', 10))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowIcon(QtGui.QIcon('qupjfpl4gvoy.jpg'))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.newjoke)

    def newjoke(self):
        reddit = praw.Reddit(client_id="sm7eOQz3ZZZ8cg",
                             client_secret="vd2fVwseAFnFj-ILna5W4IjT8nw",
                             user_agent="my user agent")
        global x
        x = reddit.subreddit("DadJokes").random()
        self.setup.setText(x.title)
        self.punchline.setText(x.selftext)
        self.setup.adjustSize()
        self.punchline.adjustSize()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jokes!"))
        self.pushButton.setText(_translate("MainWindow", "New joke!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
