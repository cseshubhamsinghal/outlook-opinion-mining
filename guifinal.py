
#from graphstreaming import *
from preprocessing import preprocess

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
## import the packages in order to fetch tweets from twitter in real time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#------------------------------------------------------------------------------------------------------------------------------------------
## import json in order to dump the tweets on the system in json format

import json

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
## cleaning the tweets

def clean_tweet(tweet):
        '''
        using regex statements to clean tweet text by removing links, special characters.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#------------------------------------------------------------------------------------------------------------------------------------------
## listener class which will listen to the tweets from the twitter

class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)                                 # tweets are dumped on the system in the json format
            tweet_text = all_data["text"]                               # only test part of the tweets will be fetched
            tweet = clean_tweet(tweet_text)                             # further cleaning of the tweets

            preprocess(tweet)
            print(all_data)
            
            #----------------------------------------------

        except:
            return True

    def on_error(self, status):
        print(status)

#------------------------------------------------------------------------------------------------------------------------------------------
## App class which contains all the widgets
        
class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'OUTLOOK-OPINION MINING'
        self.left = 20
        self.top = 20
        self.width = 700
        self.height = 500
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)                                 ## set window title
        self.setGeometry(self.left, self.top, self.width, self.height)  ## set window geometry
        self.setWindowIcon(QIcon('guipics/upes.jpg'))                   ## set window icon

        self.setAutoFillBackground(True)                                ## set window background color
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)                     
        self.setPalette(p)

        label = QLabel(self)                                            ## create label
        pixmap = QPixmap('guipics/upeslogo.PNG')                        ## create image on label
        label.setPixmap(pixmap)
        label.move(120,55)
        label.resize(400,60)

        label1 = QLabel(self)                                           ## create label1
        pixmap = QPixmap('guipics/outlook.PNG')                         ## create image on label1
        label1.setPixmap(pixmap)
        label1.move(265,65)
        label1.resize(400,60)

        label2 = QLabel('ENTER QUERY / KEYWORD', self)                  ## create label2
        label2.move(78,160)
        label2.resize(520,40)

        label3 = QLabel('Technologies Used', self)                      ## create label3
        label3.move(320,380)
        label3.resize(520,40)

        label4 = QLabel(self)                                           ## create label4
        pixmap = QPixmap('guipics/ml.PNG')                              ## create image on label4
        label4.setPixmap(pixmap)
        label4.move(205,425)
        label4.resize(400,60)

        label5 = QLabel(self)                                           ## create label5
        pixmap = QPixmap('guipics/pythonlogo.PNG')                      ## create image on label5
        label5.setPixmap(pixmap)
        label5.move(330,425)
        label5.resize(400,60)

        label6 = QLabel(self)                                           ## create label6
        pixmap = QPixmap('guipics/nltklogo.PNG')                        ## create image on label6
        label6.setPixmap(pixmap)
        label6.move(390,425)
        label6.resize(400,60)

        self.textbox = QLineEdit(self)                                  ## Create textbox
        self.textbox.move(210, 160)
        self.textbox.resize(320,40)
        self.textbox.setFont(QFont("Times New Roman",13))
        self.textbox.setMaxLength(50)

        regexp = QRegExp('([a-z A-Z]+)')                                ## Regular Expression Validator
        validator = QRegExpValidator(regexp)
        self.textbox.setValidator(validator)
 
        self.button1 = QPushButton('Submit', self)                      ## Create a button1 in the window
        self.button1.move(210,230)
        self.button1.resize(150,30)

        self.button2 = QPushButton('View DB', self)                     ## Create a button2 in the window
        self.button2.move(380,230)
        self.button2.resize(150,30)

        self.button3 = QPushButton('Live Streaming', self)              ## Create a button3 in the window
        self.button3.move(210,280)
        self.button3.resize(320,30)

#----------------------------------------------------- 
        ## connect button1 to function on_click
        self.button1.clicked.connect(self.on_click)

#----------------------------------------------------
        ## connect button2 to function on_clickk
        self.button2.clicked.connect(self.on_clickk)

#----------------------------------------------------
        ## connect button3 to function on_clickkk
        self.button3.clicked.connect(self.on_clickkk)

        self.show()

#------------------------------------------------------------------------------------------------------------------------------------------
## function for button1
        
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        ckey="cQqTOddpuQFqOfLioTnRzOckF"
        csecret="AqRozmkBB0pN7PDDfI8QznrY4WAvI9zYamBbdG65UV3X0SKIXu"
        atoken="951815779757932544-HUYIzaclC3P1SxHAgSkonGwp3kpmZSo"
        asecret="RWWHVtuidcitIA0TaOanFJokg16oh3wIEHfJJNsnYWai3"
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=[textboxValue])
        
#------------------------------------------------------------------------------------------------------------------------------------------        
## function for button2
        
    #@pyqtSlot()
    def on_clickk(self):
        obj=DB()
        obj.openDB()

#------------------------------------------------------------------------------------------------------------------------------------------        
## function for button3
        
    #@pyqtSlot()
    def on_clickkk(self):
        print("f")

#------------------------------------------------------------------------------------------------------------------------------------------
## function to delete content of twitter-out file
        
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

#------------------------------------------------------------------------------------------------------------------------------------------
## main function
        
if __name__ == '__main__':

    out = open("twitter-out.txt","w")
    deleteContent(out)
    out.close()
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
