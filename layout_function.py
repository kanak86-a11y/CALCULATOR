import sys
from PySide2.QtWidgets import QFrame, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PySide2 import QtGui, QtCore
from PySide2.QtUiTools import QUiLoader

#loader = QUiLoader()
class layoutfunction(QMainWindow):
    def __init__(self):
        super().__init__()
       
        # loader.load("main.ui", self)
        self.setFixedSize(463, 484)
        self.setWindowTitle("Calculator")
        
     
        self.setGeometry(0, 0, 463, 484)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(11, 78, 441, 395)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.SEVEN = QPushButton(self.frame)
        self.SEVEN.setGeometry(40, 60, 61, 28)
        font = self.SEVEN.font()
        font.setWeight(75)
        font.setBold(True)
        self.SEVEN.setFont(font)
        self.SEVEN.setText("7")
        self.EIGHT = QPushButton(self.frame)
        self.EIGHT.setGeometry(160, 60, 61, 28)
        font = self.EIGHT.font()
        font.setWeight(75)
        font.setBold(True)
        self.EIGHT.setFont(font)
        self.EIGHT.setText("8")
        self.NINE = QPushButton(self.frame)
        self.NINE.setGeometry(280, 60, 61, 28)
        font = self.NINE.font()
        font.setWeight(75)
        font.setBold(True)
        self.NINE.setFont(font)
        self.NINE.setText("9")
        self.plus = QPushButton(self.frame)
        self.plus.setGeometry(400, 60, 30, 30)
        self.plus.setMinimumSize(30, 30)
        self.plus.setMaximumSize(30, 30)
        font = self.plus.font()
        font.setWeight(75)
        font.setBold(True)
        self.plus.setFont(font)
        self.plus.setText("+")
        self.FOUR = QPushButton(self.frame)
        self.FOUR.setGeometry(40, 120, 61, 28)
        font = self.FOUR.font()
        font.setWeight(75)
        font.setBold(True)
        self.FOUR.setFont(font)
        self.FOUR.setText("4")
        self.FIVE = QPushButton(self.frame)
        self.FIVE.setGeometry(160, 120, 61, 28)
        font = self.FIVE.font()
        font.setWeight(75)
        font.setBold(True)
        self.FIVE.setFont(font)
        self.FIVE.setText("5")
        self.SIX = QPushButton(self.frame)
        self.SIX.setGeometry(280, 120, 61, 28)
        font = self.SIX.font()
        font.setWeight(75)
        font.setBold(True)
        self.SIX.setFont(font)
        self.SIX.setText("6")
        self.minus = QPushButton(self.frame)
        self.minus.setGeometry(400, 120, 30, 30)
        self.minus.setMinimumSize(30, 30)
        self.minus.setMaximumSize(30, 30)
        font = self.minus.font()
        font.setWeight(75)
        font.setBold(True)
        self.minus.setFont(font)
        self.minus.setText("-")
        self.initUI()

    def initUI(self):
        # Create the central widget and the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the display label
        self.display_label = QLabel()
        self.display_label.setAlignment(QtCore.Qt.AlignRight)
        self.display_label.setFixedHeight(40)
        self.display_label.setFont(QtGui.QFont('Arial', 16))
        layout.addWidget(self.display_label)

        # Create the button grid
        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        # Define the button labels
        button_labels = [
            ('7', (0, 0)), ('8', (0, 1)), ('9', (0, 2)), ('%', (0, 3)),
            ('4', (1, 0)), ('5', (1, 1)), ('6', (1, 2)), ('*', (1, 3)),
            ('1', (2, 0)), ('2', (2, 1)), ('3', (2, 2)), ('-', (2, 3)),
            ('0', (3, 0)), ('=', (3, 1)), ('/', (3, 2)), ('+', (3, 3)),
            ('C', (4, 0)), ('CE', (4, 1)),
        ]

        # Add the buttons to the grid and connect the signals to slots
        for label, pos in button_labels:
            button = QPushButton(label)
            button.setFixedSize(50, 50)
            button_grid.addWidget(button, *pos)

            if label == 'C':
                button.clicked.connect(self.clear)
            elif label == 'CE':
                button.clicked.connect(self.clear_entry)
            elif label == '=':
                button.clicked.connect(self.calculate)
            else:
                button.clicked.connect(self.append_digit)
                
        # Add the buttons to the grid and connect the signals to slots
        for label, pos in button_labels:
            button = QPushButton(label)
            button.setFixedSize(50, 50)
            button_grid.addWidget(button, *pos)

            if label == 'C':
                button.clicked.connect(self.clear)
                button.setStyleSheet("background-color: red;")
            elif label == 'CE':
                button.clicked.connect(self.clear_entry)
                button.setStyleSheet("background-color: orange;")
            elif label == '=':
                button.clicked.connect(self.calculate)
                button.setStyleSheet("background-color: green;")
            elif label in ['+', '-', '*', '/', '%']:
                button.setStyleSheet("background-color: blue;")
            elif label == '.':
                button.setStyleSheet("background-color: purple;")
            else:
                button.clicked.connect(self.append_digit)


        # Set the window properties
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)
        self.show()
        result_frame = QFrame()
        result_frame.setFrameShape(QFrame.StyledPanel)
        result_frame.setFrameShadow(QFrame.Raised)
        result_layout = QHBoxLayout(result_frame)

        # Add the result label to the frame
        self.result_label = QLabel('=0')
        self.result_label.setFont(QtGui.QFont('Arial', 14, weight=QtGui.QFont.Bold))
        result_layout.addWidget(self.result_label)

        # Add the result frame to the main layout
        layout.addWidget(result_frame)

    def append_digit(self):
        sender = self.sender()
        self.display_label.setText(self.display_label.text() + sender.text())


    def clear(self):
        self.display_label.setText('')


    def clear_entry(self):
        text = self.display_label.text()[:-1]
        self.display_label.setText(text)


    def calculate(self):
        text = self.display_label.text()
        try:
            result = eval(text)
            self.display_label.setText(str(result))
        except Exception as e:
            self.display_label.setText('Error: ' + str(e))
            
    






        
        
           
        