from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import keyword_functions

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #create a window
        self.setWindowTitle("Keyword Checker")
        self.setGeometry(250, 250, 1300, 500)
        #main window layout
        layout = QVBoxLayout()
        #stack widget to hold the two different layouts of the main window (screen 1 & 2)
        self.stackwidget = QStackedWidget()
        self.screen1 = self.layout1()
        self.screen2 = self.layout2()
        self.screen3 = self.layout3()
        #add screen 1 & 2 to stackwidget after setting it up.
        self.stackwidget.addWidget(self.screen1)
        self.stackwidget.addWidget(self.screen2)
        self.stackwidget.addWidget(self.screen3)
        #add stackedwidget to main layout
        layout.addWidget(self.stackwidget)
        self.setLayout(layout)

#sets up screen layout 1
    def layout1(self):
        #widget to hold screen layout, added to stackwidget
        screen1 = QWidget()
        box_layout = QVBoxLayout()
        button1 = QPushButton("Add words")
        button1.clicked.connect(self.edit_button_clicked)
        box_layout.addWidget(button1)
        #using self. syntax for text_box since it needs to be accessed in handler function
        self.text_box = QPlainTextEdit()
        box_layout.addWidget(self.text_box)
        button2 = QPushButton("Find Keywords")
        box_layout.addWidget(button2)
        #need to connect the signal of button being clicked to handler function
        button2.clicked.connect(self.keyword_button_clicked)
        
        screen1.setLayout(box_layout)
        return screen1
    
        
#sets up screen layout 2
    def layout2(self):
        #widget to hold screen layout, added to stackwidget
        screen2 = QWidget()
        box_layout = QVBoxLayout()
        #keywords table
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(2)

        #change column titles
        self.table.setHorizontalHeaderLabels(["Keyword", "Frequency"])

        #remove the row titles
        self.table.verticalHeader().hide()

        #Table will fit the screen horizontally
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        box_layout.addWidget(self.table)
        #go back button
        goback_button = QPushButton("Enter another description")
        box_layout.addWidget(goback_button)
        goback_button.clicked.connect(self.goback_button_clicked)
        screen2.setLayout(box_layout)
        return screen2
    
    #this is the screen for viewing, adding, and removing keywords
    def layout3(self):
        screen3 = QWidget()
        box_layout = QVBoxLayout()

        goback_button = QPushButton("Enter another description")
        box_layout.addWidget(goback_button)
        goback_button.clicked.connect(self.goback_button_clicked)

        screen3.setLayout(box_layout)
        return screen3
    
    #sets up the pop up window that is displayed when no keywords are found
    def pop_up(self):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText("No keywords were found in this description.")
        box.exec()
    
    def fill_table(self, table):
        #set row  and column count
        num_keywords = len(self.key_words)
        table.setRowCount(num_keywords)

        #add items from keywords dict to table
        #make a list of the keys
        keys = list(self.key_words.keys())
        row = 0
        col = 0
        for i in range(num_keywords):
            table.setItem(row, col, QTableWidgetItem(keys[i]))
            #Qtablewidget items cannot be ints, but they can be str
            table.setItem(row, col+1, QTableWidgetItem(str(self.key_words[keys[i]])))
            row += 1

        #return table

    #signal handler function, called when button is clicked
    def keyword_button_clicked(self):
        #string of all text entered into text box
        text = self.text_box.toPlainText()
        #block until some text is entered into the box
        if text != "":
            #create the keywords dict and setup screen layout 2 or 3
            self.key_words = keyword_functions.create_keywords_table(text)

            #clear the text box
            self.text_box.clear()
            if len(self.key_words) != 0:
                #fill the table
                self.fill_table(self.table)
                #set stackwidget to be screen 2
                self.stackwidget.setCurrentIndex(1)
            else:
                #display the no keywords pop up
                self.pop_up()

    def goback_button_clicked(self):
        self.stackwidget.setCurrentIndex(0)

    def edit_button_clicked(self):
        self.stackwidget.setCurrentIndex(2)



if __name__ == '__main__':
    #create an application
    app = QApplication(sys.argv)
    #create window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())