# encoding=utf-8

config = {
    'webConfig': {'port': 5000},
    'devConfig': [{'name': 'xBee', 'port': 9001}, {'name': 'light', 'port': 4001},
                  {'name': 'rfidListener', 'port': 9999}, ],
    'serialConfig': [
        {'name': 'rfid', 'serialName': {'Windows': 'COM11', 'Linux': '/dev/ttyUSB0'}, 'baudrate': 38400}, ],
}
