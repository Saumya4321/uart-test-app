import sys
import serial
import serial.tools.list_ports
from receiver_thread import SerialReader
import time


class SerialComm:
    def __init__(self, parent=None):
        try:
            
            self.parent = parent
            self.serial_port = None 

            # Console logging
            self.history_console = self.parent.history_console
            self.response_log = self.parent.response_log
         

        except Exception as e:
            print(f"Serial Communication class initialization failed. {e}")


    def send_port_list(self):
        """Scan and list available COM ports."""
        ports = serial.tools.list_ports.comports()
        return ports

    def disconnect(self):
        """Connect or disconnect the serial port."""
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.parent.log_history({"info":f"Serial port communicaton via {self.serial_port.port} with \n baud rate of {self.serial_port.baudrate} disconnected..."})
            self.text_receive = ""
           


    def connect(self, port, baud_rate):
            selected_port = port
            try:
                self.serial_port = serial.Serial(selected_port, baudrate=baud_rate,timeout=2, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
                self.parent.log_history({"info":f"Port {port} exists and is accessible \n"})
                self.parent.log_response({"info":f"Port {port} exists and is accessible \n"})
                
            except Exception as e:
                self.parent.log_history({"error":f"Connection to {port} failed! \n {e}"})
                self.parent.log_response({"error":f"Connection to {port} failed! \n {e}"})
            
        
            try:
                if self.serial_port.is_open:
                    self.reader = SerialReader(self.serial_port)
                    self.reader.data_received.connect(self.display_received_data)
                    self.reader.start()
            except Exception as e:
                self.parent.log_history({"error":f"Error while receiving data \n {e}"})



    def send_data(self, LineEdit):
        """Send data via UART."""
        # if self.serial_port and self.serial_port.is_open:
        try:
                data = LineEdit.text()
               

                if data[:8] == "LASERPWR":
                    percent_val = int(float(data[9:12]))
                    power_val = int((percent_val / 100) * 255)

                    payload = "LASERPWR" + " "+ str(power_val)

                else: 
                     payload = data

                self.serial_port.write((payload + '\r').encode('utf-8'))
                LineEdit.clear()
                self.parent.log_history({"info":f"Message `{data}` is sent"})
        except Exception as e:
                self.parent.log_history({"error":f"Data could not be sent \n {e}"})
                print(e)

    def closeEvent(self):
        """Ensure the serial port is closed on exit."""
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()

    def display_received_data(self, data):
        self.parent.log_response({"info":f"Message received: {data}"})
       

        




