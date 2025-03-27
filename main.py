# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    # Init/Constructor
    def __init__(self):
        super().__init__() # this is necessary
        # App Settings
        self.setWindowTitle("Calculator")
        self.resize(250,300)

        # Objects/Widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Arial",30)) # set font of text box
        self.text_box.setStyleSheet("QLineEdit { color: white; font-style: bold; border: none; padding-left: 8px; padding-right: 8px; margin-top: 50px; margin-bottom: 10px }")
        
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(2) # remove horizontal and vertical margins between buttons
        self.grid.setVerticalSpacing(2) 

        self.buttons = ["7","8","9","/",
                        "4","5","6","*",
                        "1","2","3","-",
                        ".","0","=","+"]

        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("""
                                 QPushButton { 
                                    font: 18px Arial; 
                                    color: white; 
                                    background-color: #131313; 
                                    border: none; 
                                    padding-left: 30px;
                                    padding-right: 30px;
                                    padding-top: 15px;
                                    padding-bottom: 15px;}
                                 QPushButton:hover { background-color: #4a4a4a; }
                                 QPushButton:pressed { background-color: #464646; }
                                """) # CSS
            self.grid.addWidget(button, row, col)
            col += 1
            
            if col > 3:
                col = 0
                row += 1
            
        # Buttons with no margins
        self.clear = QPushButton("C")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("""
                                 QPushButton { font: 18px Arial; color: white; background-color: #134369; border: none; padding: 10px; margin: 0px; }
                                 QPushButton:hover { background-color: #363636; }
                                 QPushButton:pressed { background-color: #464646; }
                                 """)
        
        self.delete.setStyleSheet("""
                                 QPushButton { font: 18px Arial; color: white; background-color: #134369; border: none; padding: 10px; margin: 0px; }
                                 QPushButton:hover { background-color: #363636; }
                                 QPushButton:pressed { background-color: #464646; }
                                 """)
        
        # Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        
        # Remove any margin and spacing in the button row layout
        button_row.setContentsMargins(0, 0, 0, 0)
        button_row.setSpacing(1)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(2,2,2,2) # CSS set margins
        
        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    # Method - a function in a class
    def button_click(self):
        button = app.sender() # listen to which button was clicked
        text = button.text()
        
        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res)) # set text as updated value
            except Exception as e:
                self.text_box.setText("Error")
                print("Error:", e)
        
        elif text == "C":
            self.text_box.clear() # clear whats inside the text box
        
        elif text == "<":
            current_value = self.text_box.text() # current value = whats inside the text box
            self.text_box.setText(current_value[:-1])
        
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

# Run
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #1f1f1f; margin: 0 }")
    main_window.show()
    app.exec_()
    
