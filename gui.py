from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
import sys
import keywords

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
        #self.screen2 = self.layout2()
        #add the two screen layouts to the stackwidget after setting them up
        self.stackwidget.addWidget(self.screen1)
        #self.stackwidget.addWidget(self.screen2)
        #add stackedwidget to main layout
        layout.addWidget(self.stackwidget)
        self.setLayout(layout)

#sets up screen layout 1
    def layout1(self):
        #widget to hold screen layout, added to stackwidget
        screen1 = QWidget()
        box_layout = QVBoxLayout()
        #using self. syntax for text_box since it needs to be accessed in handler function
        self.text_box = QPlainTextEdit()
        box_layout.addWidget(self.text_box)
        button = QPushButton("print text")
        box_layout.addWidget(button)
        #need to connect the signal of button being clicked to handler function. using lambda to have access to text_box in this function
        button.clicked.connect(self.button_clicked)
        
        screen1.setLayout(box_layout)
        return screen1
        
#sets up screen layout 2
    def layout2(self):
        #widget to hold screen layout, added to stackwidget
        screen2 = QWidget()
        box_layout = QVBoxLayout()
        #keywords table
        table = QTableWidget()
        #set row  and column count
        num_keywords = len(self.key_words)
        table.setRowCount(num_keywords)
        table.setColumnCount(2)

        #add items from keywords dict to table
        #make a list of the keys
        keys = list(self.key_words.keys())
        print(self.key_words)
        row = 0
        col = 0
        for i in range(num_keywords):
            table.setItem(row, col, QTableWidgetItem(keys[i]))
            #Qtablewidget items cannot be ints, but they can be str
            table.setItem(row, col+1, QTableWidgetItem(str(self.key_words[keys[i]])))
            row += 1

        #change column titles
        table.setHorizontalHeaderLabels(["Keyword", "Frequency"])

        #remove the row titles
        table.verticalHeader().hide()

         #Table will fit the screen horizontally
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        box_layout.addWidget(table)
        screen2.setLayout(box_layout)
        return screen2
    
    def button_clicked(self):
        text = self.text_box.toPlainText()
        self.key_words = keywords.create_keywords_table(text)
        self.screen2 = self.layout2()
        self.stackwidget.addWidget(self.screen2)
        self.stackwidget.setCurrentIndex(1)



if __name__ == '__main__':
    #create an application
    app = QApplication(sys.argv)
    stack = QStackedWidget()
    #create window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())