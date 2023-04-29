from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the central widget and the layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Create the display label
        self.display_label = QtWidgets.QLabel()
        self.display_label.setAlignment(QtCore.Qt.AlignRight)
        self.display_label.setFixedHeight(40)
        self.display_label.setFont(QtGui.QFont('Arial', 16))
        layout.addWidget(self.display_label)

        # Create the button grid
        button_grid = QtWidgets.QGridLayout()
        layout.addLayout(button_grid)

        # Define the button labels
        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'CE',
        ]

        # Add the buttons to the grid and connect the signals to slots
        row = 0
        col = 0
        for label in button_labels:
            button = QtWidgets.QPushButton(label)
            button.setFixedSize(50, 50)
            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

            if label == 'C':
                button.clicked.connect(self.clear)
            elif label == 'CE':
                button.clicked.connect(self.clear_entry)
            elif label == '=':
                button.clicked.connect(self.calculate)
            else:
                button.clicked.connect(self.append_digit)

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
