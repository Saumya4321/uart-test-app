from PyQt5.QtCore import QThread, pyqtSignal

class SerialReader(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port and self.serial_port.is_open:
                try:
                    data = self.serial_port.readline().decode('utf-8').strip()
                    if data:
                        self.data_received.emit(data)
                except:
                    break

    def stop(self):
        self.running = False
        self.quit()
        self.wait()
