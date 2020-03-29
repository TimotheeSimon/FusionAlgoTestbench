import serial

ser = serial.Serial('COM9', baudrate = 9600, timeout = 1)

while True:
    try:
        data_read = ser.readline().decode('ascii').strip().strip('\x00')
        data_read = str(data_read).split(',')
        print(data_read)
        #print(ser.readline())
    except:
        pass