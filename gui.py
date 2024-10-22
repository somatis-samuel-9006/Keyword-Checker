from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import keyword_functions
from win32api import GetMonitorInfo, MonitorFromPoint

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #create a window
        self.setWindowTitle("Keyword Checker")
        dimensions = self.window_dimsensions()
        self.setGeometry(dimensions[0], dimensions[1], 1300, 500)

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
        outer_layout = QVBoxLayout()
        #layout for top row of vertical box layout
        inner_layout = QHBoxLayout()

        prompt = QLabel("Enter a description:")
        inner_layout.addWidget(prompt, alignment=QtCore.Qt.AlignLeft)

        button1 = QPushButton("Add words")
        button1.clicked.connect(self.edit_button_clicked)
        #widgets in layout that need to be a manually specified size use setFixedSize
        button1.setFixedSize(QtCore.QSize(188, 34))
        inner_layout.addWidget(button1, alignment=QtCore.Qt.AlignRight)
        outer_layout.addLayout(inner_layout)
        #using self. syntax for text_box since it needs to be accessed in handler function
        self.text_box = QPlainTextEdit()
        outer_layout.addWidget(self.text_box)
        button2 = QPushButton("Find Keywords")
        #need to connect the signal of button being clicked to handler function
        button2.clicked.connect(self.keyword_button_clicked)
        button2.setFixedSize(QtCore.QSize(248, 34))

        outer_layout.addWidget(button2, alignment=QtCore.Qt.AlignCenter)
        
        screen1.setLayout(outer_layout)
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
        goback_button.clicked.connect(self.goback_button_clicked)
        goback_button.setFixedSize(QtCore.QSize(248, 34))

        box_layout.addWidget(goback_button, alignment=QtCore.Qt.AlignCenter)
        screen2.setLayout(box_layout)
        return screen2
    
    #this is the screen for viewing, adding, and removing keywords
    def layout3(self):
        screen3 = QWidget()
        outer_layout = QVBoxLayout()

        #list widget for keywords display
        keywords_display = QListWidget()
        keywords_display.setFixedSize(QtCore.QSize(640, 480))
        #print(keywords_display.size())

        #read in keywords list
        with open("Keywords.txt", "r+") as f:
            file_words = f.readlines()

        for i in range(len(file_words)):
            file_words[i] = file_words[i].strip('\n')
            #add it to the display
            keywords_display.addItem(QListWidgetItem(file_words[i]))

        #display number of words above list, Qlabel needs to be a string (not updating when new word is added)
        number_of_words = QLabel("Word count: " + str(len(file_words)))
        outer_layout.addWidget(number_of_words)
        #layout to hold the list widget and the Vboxlayout of the buttons
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(keywords_display, alignment=QtCore.Qt.AlignLeft)
        button_layout = QVBoxLayout()
    

        add_button = QPushButton("Add")
        add_button.setFixedSize(QtCore.QSize(248, 45))
        #use lamda function to pass additional argument to signal handler
        add_button.clicked.connect(lambda: self.add_to_list(keywords_display, number_of_words))
        button_layout.addWidget(add_button)

        remove_button = QPushButton("Remove")
        remove_button.setFixedSize(QtCore.QSize(248, 45))
        remove_button.clicked.connect(lambda: self.remove_from_list(keywords_display, number_of_words))
        button_layout.addWidget(remove_button)

        search_button = QPushButton("Search")
        search_button.setFixedSize(QtCore.QSize(248, 45))
        search_button.clicked.connect(self.search_list)
        button_layout.addWidget(search_button)

        inner_layout.addLayout(button_layout)
        outer_layout.addLayout(inner_layout)

        goback_button = QPushButton("Back")
        goback_button.clicked.connect(self.goback_button_clicked)
        goback_button.setFixedSize(QtCore.QSize(248, 34))
        outer_layout.addWidget(goback_button, alignment=QtCore.Qt.AlignLeft)

        outer_layout.setContentsMargins(100, 20, 100, 20)
        screen3.setLayout(outer_layout)
        return screen3
    
    #calculates and returns the appropriate geometry values for the main window
    def window_dimsensions(self):
        #make sure we are using the primary monitor, which has its upper left corner at 0,0
        primary_monitor = GetMonitorInfo(MonitorFromPoint((0,0)))
        #centering window in WORK AREA (desktop - taskbar) dimensions. GetMonitorInfo returns a dict which has work area info
        #assigned to the 'Work' key. index 2 and 3 are the work area dimensions
        work_area = primary_monitor.get("Work")
        work_width = work_area[2]
        work_height = work_area[3]
        # #standard with and height of the window that I like
        window_width = 1300
        window_height = 500
        # #center top left corner of window
        x = (work_width - window_width) // 2
        y = (work_height - window_height) // 2
        return [x , y]


    #sets up the pop up window that displays the given message
    def pop_up(self, window_title, msg):
        box = QMessageBox(self)
        box.setWindowTitle(window_title)
        box.setText(msg)
        box.exec()

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
                self.pop_up("Error", "No keywords were found in this description.")
    
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

    #add a new keyword to the keywords display
    def add_to_list(self, listwidget, count_label):
        #input dialog to get the word from user
        #this syntax is from documentation of QinputDialog. word is the value user enters, ok is true is they click 'ok' an
        #false if they click cancel
        dialog = QInputDialog()
        word, ok = dialog.getText(self, "Add Word", "Enter a word")
        if word and ok:
        #add the word to keywords.txt
            #add_word will return false if word already in file
            if keyword_functions.add_word(word):
                listwidget.addItem(QListWidgetItem(word))
                #update the list widget
                listwidget.repaint()

                #update the count
                label_text = count_label.text()
                #text is formated: Word Count: xxxxx so need to get everything after first 12 chars
                num = int(label_text[12:])
                num += 1
                count_label.setText("Word count: " + str(num))
            else:
                #display pop up for duplicate word
                self.pop_up("Error", "This word is already in the list.")


    def remove_from_list(self, listwidget, count_label):
        #input dialog to get the word from user
        #this syntax is from documentation of QinputDialog. word is the value user enters, ok is true is they click 'ok' an
        #false if they click cancel
        dialog = QInputDialog()
        word, ok = dialog.getText(self, "Remove Word", "Enter a word")
        if word and ok:
        #add the word to keywords.txt
            if keyword_functions.remove_word(word):
                #find qlistwidgetitem with the string name of the word, returns list with one element
                row_item = listwidget.findItems(word, QtCore.Qt.MatchExactly)
                #get index in listwidget of item to be removed
                index = listwidget.row(row_item[0])
                listwidget.takeItem(index)
                #update the list widget
                listwidget.repaint()

                #update the count
                label_text = count_label.text()
                #text is formated: Word Count: xxxxx so need to get everything after first 12 chars
                num = int(label_text[12:])
                num -= 1
                count_label.setText("Word count: " + str(num))
            else:
                #display pop up for duplicate word
                self.pop_up("Error", "Word not found in list.")
   
    def search_list(self):
        dialog = QInputDialog()
        word, ok = dialog.getText(self, "Search", "Enter a word")
        if word and ok:
            if keyword_functions.check_for_word(word):
                self.pop_up("Result", f"{word} is in the list.")
            else:
                self.pop_up("Result", "Word not found in list.")
        


    def goback_button_clicked(self):
        self.stackwidget.setCurrentIndex(0)

    def edit_button_clicked(self):
        self.stackwidget.setCurrentIndex(2)



if __name__ == '__main__':
    #create an application
    app = QApplication(sys.argv)
    #from stack overflow, disables the '?' button in the input dialog for adding words (application wide)
    #because disabling it in the constructor for said dialog would not work, don't know why
    app.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)
    #create window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())