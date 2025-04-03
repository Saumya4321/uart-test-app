# UART Communication Testing App

## Overview
The **UART Test App** is a PyQt-based application that allows users to test and debug UART communication between two devices. It provides a simple and interactive GUI to configure serial communication parameters, send and receive data, and console-log errors. This tool is useful for embedded systems engineers, hardware developers, and anyone working with serial communication. 

## Motivation
This UART communication app was mainly developed to perform experiments on connecting with a custom laser scancard. 

## Features
- **Customizable Serial Configuration:** Set baud rate, parity, data bits, and stop bits.
- **Live Console Output:** View incoming data in real time.
- **Send Custom Commands:** Transmit messages to connected devices.
- **Error Handling:** Detect and display UART errors such as parity errors, framing errors, and overrun errors.
- **Auto-Detect Available COM Ports:** Automatically lists all available serial ports for easy selection.
- **Lightweight and Fast:** Built with PyQt for a responsive and user-friendly interface.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed. You can download it from [Python's official website](https://www.python.org/).

### Install Dependencies
Clone this repository and install the required dependencies:
```
git clone https://github.com/Saumya4321/uart-test-app.git
cd uart-test-app
pip install -r requirements.txt
```

### Running the Application
Run the following command to launch the application:
```
python main.py
```

## Usage
1. **Connect the UART Device:** Ensure your device is connected to your PC via a serial port.
2. **Select the COM Port:** Choose the correct COM port from the dropdown list.
3. **Set Communication Parameters:** Adjust baud rate, parity, stop bits, and other settings.
4. **Send and Receive Data:** Type messages to send and view received responses in the console.
5. **Monitor Errors:** View real-time errors detected during communication.

## Screenshots
![image](https://github.com/user-attachments/assets/44c17fa9-0de6-448e-91c3-5af1144debfb)


## Future Enhancements
- **Hex/ASCII View Toggle** for raw data display.
- **Packet Monitoring Graph** to visualize incoming data.
- **Ethernet-Based Communication** support for testing over TCP/IP.
- **Standalone Executable Release** for Windows and Linux.
- **Logging Support** to save communication logs for debugging and analysis.

## Contributing
Contributions are welcome! :) To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.



