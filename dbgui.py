from detector import *
from pandatogui import *
from graphstreaming import *

import sqlite3
import pandas as pd
#------------------------------------------------------------------------------------------------------------------------------------------
## import the packages in order to create GUI

import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#------------------------------------------------------------------------------------------------------------------------------------------
## import regular expression in order to clean the tweets

import re

#------------------------------------------------------------------------------------------------------------------------------------------
## class DB has function openDB() which is responsible for showing the MiningReport table

class DB:
    def openDB(self):
        conn = sqlite3.connect('database/database.db')
        print("opened database successfully")
        cursor = conn.execute("SELECT sessionid, date, query, positive, negative from MiningReport;")

        data = []
        
        for row in cursor:
            datarow = [row[0],row[1],row[2],row[3],row[4]]
            data.append(datarow)
            df = pd.DataFrame(data,columns=['Session ID','Date','Query','Positive%','Negative%'])
        print(df)

        conn.close()



#------------------------------------------------------------------------------------------------------------------------------------------
## App class which contains all the widgets
        
class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'OUTLOOK-OPINION MINING'
        self.left = 730
        self.top = 40
        self.width = 170
        self.height = 320
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)                                 ## set window title
        self.setGeometry(self.left, self.top, self.width, self.height)  ## set window geometry
        self.setWindowIcon(QIcon('guipics/upes.jpg'))                   ## set window icon

        self.setAutoFillBackground(True)                                ## set window background color
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)                     
        self.setPalette(p)

 
        self.button1 = QPushButton('LIVE STREAMING', self)              ## Create a button1 in the window
        self.button1.move(35,50)
        self.button1.resize(100,100)

        self.button2 = QPushButton('VIEW DB', self)                     ## Create a button2 in the window
        self.button2.move(35,160)
        self.button2.resize(100,100)


#----------------------------------------------------- 
        ## connect button1 to function on_click
        self.button1.clicked.connect(self.on_click)

#----------------------------------------------------
        ## connect button2 to function on_clickk
        self.button2.clicked.connect(self.on_clickk)

        self.show()

#------------------------------------------------------------------------------------------------------------------------------------------
## function for button1
        
    @pyqtSlot()
    def on_click(self):
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

        
#------------------------------------------------------------------------------------------------------------------------------------------        
## function for button2
        
    #@pyqtSlot()
    def on_clickk(self):
        function()
##        ani = animation.FuncAnimation(fig, animate, interval=1000)
##        plt.show()
      

#------------------------------------------------------------------------------------------------------------------------------------------
## main function
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
