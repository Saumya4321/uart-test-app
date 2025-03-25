
# pyqt libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QComboBox, QPushButton, QLineEdit
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import sys
from uart import SerialComm
import os

import app_ui  # Import the generated Python UI file

# The main GUI class, which defines our application window with all of it's functionalities
class gui(QMainWindow, app_ui.Ui_MainWindow):
    # signal to update console
    update_console_signal = pyqtSignal(dict)
    

    def __init__(self, main):
    
        super().__init__()
        self.setupUi(self)  

        self.setWindowTitle("UART Laser Testing")

        self.init_default_values()
        self.init_classes()
        self.init_ui_elements()
        self.refresh_port_list()

        self.show()



    def init_ui_elements(self):
        
        self.baudRateComboBox = self.findChild(QComboBox, "baudRateComboBox")
        self.baudRateComboBox.currentTextChanged.connect(lambda: self.update_baud_rate(self.baudRateComboBox.currentText()))
        self.baudRateComboBox.setCurrentIndex(2)


        self.commPortComboBox = self.findChild(QComboBox,"commPortComboBox")

        self.connectButton = self.findChild(QPushButton,"ConnectButton")
        self.connectButton.clicked.connect(self.connection_start)

        self.disconnectButton = self.findChild(QPushButton, "disconnectButton")
        self.disconnectButton.clicked.connect(self.serial_class.disconnect)

        self.cmdLineEdit = self.findChild(QLineEdit,"cmdLineEdit")
        self.cmdLineEdit.returnPressed.connect(self.submit_button_clicked)

        self.cmdSubmitButton = self.findChild(QPushButton, "cmdSubmitButton")
        self.cmdSubmitButton.clicked.connect(self.submit_button_clicked)

        self.response_log = self.findChild(QListWidget, "response_log")

        self.history_console = self.findChild(QListWidget, "history_console")

    def init_default_values(self):
        self.port_selected = None
        self.baud_rate_selected = 9600

    def init_classes(self):
        self.serial_class = SerialComm(self)

    def update_baud_rate(self,rate):
        self.baud_rate_selected = int(rate)


    def connection_start(self):
        self.port_selected = self.commPortComboBox.currentText()
        if self.port_selected == None:
            self.log_history({"error":"Select a comm port first!!"})
        
        else:
            self.log_history({"info":f"Connecting to {self.port_selected} with a baud rate of \n  {self.baud_rate_selected}"})
            self.serial_class.connect(self.port_selected,self.baud_rate_selected)


    def submit_button_clicked(self):
        self.serial_class.send_data(self.cmdLineEdit)


    def closeEvent(self, event):
        """Ensure the serial port is closed on exit."""
        self.serial_class.closeEvent()
        event.accept()

    def refresh_port_list(self):
        self.commPortComboBox.clear()
        ports = self.serial_class.send_port_list()
        for port in ports:
            self.commPortComboBox.addItem(port.device)



    # ---------- Printing to consoles ----------------

     # function used to add text to response log window
    def log_response(self,dict):
        if "error" in dict.keys():
            self.addConsoleItem(self.response_log, dict["error"], is_error=True)
        else:
            self.addConsoleItem(self.response_log, dict["info"])

    # function used to add text to history logs window
    def log_history(self,dict):
        if "error" in dict.keys():
            self.addConsoleItem(self.history_console, dict["error"], is_error=True)
        else:
            self.addConsoleItem(self.history_console, dict["info"])


    # function to add sentences to console; in case of error, text is printed in red. Else it is printed in white        
    def addConsoleItem(self,console_widget, text, is_error=False):
        # Create a new QListWidgetItem
        item = QListWidgetItem(f"> {text}")
    
        # Set the color based on whether it's an error or not
        if is_error:
            item.setForeground(QColor("red"))  # Error color
        else:
            item.setForeground(QColor("white"))  # Regular log color
                
        # Add the item to the ListWidget
        console_widget.addItem(item)
        # scroll to bottom of list so that newly added line is visible
        console_widget.scrollToBottom()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    UI = gui("main")
    app.exec_()
