import sys
from PySide2.QtWidgets import QApplication
from layout_function import layoutfunction


app = QApplication(sys.argv)
Mainwindow = layoutfunction()

Mainwindow.show()
sys.exit(app.exec_())