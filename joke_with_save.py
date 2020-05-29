import praw
from PyQt5 import QtCore, QtGui, QtWidgets
import add_joke
import sqlite3

reddit = praw.Reddit(client_id="sm7eOQz3ZZZ8cg",
                             client_secret="vd2fVwseAFnFj-ILna5W4IjT8nw",
                             user_agent="my user agent")

class Ui_MainWindow(object):
    conn = None
    testing = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dad Joke Finder")
        MainWindow.setWindowIcon(QtGui.QIcon('qupjfpl4gvoy.jpg'))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setup = QtWidgets.QLabel(self.centralwidget)
        self.setup.setGeometry(QtCore.QRect(50, 50, 411, 141))
        self.setup.setFont(font)
        self.setup.setWordWrap(True)
        self.setup.setObjectName("setup")

        self.punchline = QtWidgets.QLabel(self.centralwidget)
        self.punchline.setGeometry(QtCore.QRect(50, 220, 401, 211))
        self.punchline.setFont(font)
        self.punchline.setAutoFillBackground(False)
        self.punchline.setWordWrap(True)
        self.punchline.setObjectName("punchline")

        self.nwjk = QtWidgets.QPushButton(self.centralwidget)
        self.nwjk.setGeometry(QtCore.QRect(50, 480, 231, 71))
        self.nwjk.setFont(font)
        self.nwjk.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nwjk.setAcceptDrops(False)
        self.nwjk.setFlat(False)
        self.nwjk.setObjectName("pushButton")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(310, 480, 231, 71))
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.save.setAcceptDrops(False)
        self.save.setFlat(False)
        self.save.setObjectName("pushButton_2")

        self.moreinfo = QtWidgets.QPushButton(self.centralwidget)
        self.moreinfo.setGeometry(QtCore.QRect(570, 480, 161, 71))
        self.moreinfo.setFont(font)
        self.moreinfo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.moreinfo.setAcceptDrops(False)
        self.moreinfo.setFlat(False)
        self.moreinfo.setObjectName("pushButton_4")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(350, 70, 400, 361))
        self.scrollArea.setMinimumSize(QtCore.QSize(211, 361))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")


        self.history_heading = QtWidgets.QLabel(self.centralwidget)
        self.history_heading.setGeometry(QtCore.QRect(530, 20, 251, 31))
        self.history_heading.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.nwjk.clicked.connect(self.newjoke)
        self.save.clicked.connect(self.savejoke)
        self.moreinfo.clicked.connect(self.saved)

    def newjoke(self):
        global x
        x = reddit.subreddit("DadJokes").random()
        if len(x.title) <= 100 and len(x.selftext) <= 300:
            self.setup.setText(x.title)
            self.punchline.setText(x.selftext)
            self.setup.adjustSize()
            self.punchline.adjustSize()
            self.joketitle = str(x.title)
            self.jokeselftext = str(x.selftext)
            self.jokeauthor = str(x.author)
            self.jokeurl = str(x.shortlink)
        else:
            self.newjoke()

    def savejoke(self):
        add_joke.add_joke(self.joketitle, self.jokeselftext, self.jokeurl, self.jokeauthor)

    hist = []
    def saved(self):
        conn = sqlite3.connect('jokes_db.db')
        c = conn.cursor()
        c.execute("SELECT id, Title, selftext, url, author from jokes_list")
        rows = c.fetchall()

        for row in rows:
            if row[1] not in self.hist:
                name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                name.setObjectName("label_5")
                name.setText(row[1] + '\n-----------------------------------------\n' + row[2] + '\nWritten by: ' + row[4] + '\n'+ 'Find at: '+ row[3])
                self.verticalLayout.addWidget(name)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                name.setWordWrap(True)
                name.setStyleSheet('border:0.5px solid black;')
                self.hist.append(row[1])
            else:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setup.setText(_translate("MainWindow", "TextLabel"))
        self.punchline.setText(_translate("MainWindow", "punchline"))
        self.nwjk.setText(_translate("MainWindow", "New joke!"))
        self.save.setText(_translate("MainWindow", "SAVE"))
        self.moreinfo.setText(_translate("MainWindow", "More info"))
        self.history_heading.setText(_translate("MainWindow", "Saved jokes"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.newjoke()
    ui.saved()
    sys.exit(app.exec_())
