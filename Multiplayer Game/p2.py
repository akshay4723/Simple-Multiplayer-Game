import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import *
from PyQt5.QtDesigner import *
from PyQt5.QtGui import *
import PyQt5
import sys
import gamelay 
from gamelay import Ui_MainWindow
import playerlay
from playerlay import Ui_GameWindow

s = socket.socket()

player1 = []
player2 = []

def game_window():
    ak.close()
    gamewindow.show()


def play_game():

    if player1[0] == "stone":
        if player2[0] == "paper":
            print("player 1 wins")
            gamewindow.player_lose()
        else :
            print("Player 2 Wins")
            gamewindow.player_won()
    elif player1[0] == "paper":
        if player2[0] == "stone":
            print("Player 2 Wins")
            gamewindow.player_won()
        else :
            print("Player 1 Wins")
            gamewindow.player_lose()
    elif player1[0] == "scissor":
        if player2[0] == "paper":
            print("Player 2 Wins")
            gamewindow.player_won()
        else :
            print("Player 1 Wins")
            gamewindow.player_lose() 


def send_mes(core):
    mes = core
    player1.append(mes)
    mes = mes.encode()
    s.send(mes)

def recv_mes():
    while 1:
        mes = s.recv(10000)
        mes = mes.decode()
        print(mes)
        player2.append(mes)   

def running():
    while 1:
        if len(player1) == 1:
            if len(player2) == 1:
                play_game()
                player1.clear()
                player2.clear()

#First Window

class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.connect_to_player)


    def connect_to_player(self):

        ip = self.ui.lineEdit.text()
        port = int(self.ui.lineEdit_2.text())
        print(ip,port)
        s.connect((ip,port))
        game_window()
        rm = threading.Thread(target=recv_mes)
        rm.start()
        run = threading.Thread(target=running)
        run.start()

#Second Window

class player_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.stone_core)
        self.ui.pushButton_2.clicked.connect(self.paper_core)
        self.ui.pushButton_3.clicked.connect(self.scissor_core)

    def stone_core(self):
        send_mes("stone")

    def paper_core(self):
        send_mes("paper")

    def scissor_core(self):
        send_mes("scissor")

    def player_won(self):
        self.ui.label.setText("You Won !")

    def player_lose(self):
        self.ui.label.setText("You Lose")

    def player_connected_message(self):
        self.ui.label_2.setText("Player Connected")



if __name__=="__main__":
    app = QApplication(sys.argv)
    ak = main()
    gamewindow = player_window()
    ak.show()
    sys.exit(app.exec_())