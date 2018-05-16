import sys
import os
import argparse
import time
import serial
#import struct
import dataset.bt_command
import dataset.showlogo as slogo
import dataset.hciresponse
##https://stackoverflow.com/questions/15570526/sending-hex-over-serial-with-python

#Global Variable

path = os.getcwd() + '\\'
app_name = __file__.replace(path,'')
version_string = "0.0.7"
Description_enable = True
raw_buffer = []
#log
#20180419 add the serial command test


#Basic Configuration
serial1_port="COM5"
serial_baudrate=115200
duration_timer = 1

test_command_set = {
    'HCI Inquiry'        : b'\x01\x01\x04\x05\x33\x8B\x9E\x30\x00', #LAP = 0x9E8B33 Len=0x30
    'HCI Inquiry1'        : b'\x01\x01\x04\x05\x00\x00\x00\x00\x00', #LAP = 0x9E8B33 Len=0x30
    'HCI Inquiry Cancel' : b'\x01\x02\x04\x00',
}

'''
def command_hci_read_local_support_feature(ser):
    send_data = dataset.bt_command.generate_command('HCI Read Local Supported Features')
    print(send_data)
    serial_write(ser,send_data)
    time.sleep(.1)
    rx_buffer = serial_read(ser)
    print(rx_buffer)
'''
def license_alarm():
    print(slogo.decode('+--------------------------------------------------------------------------%'))
    print(slogo.decode('|'), '            Python BLE HCI Command Test  - ', app_name, slogo.decode('      |'))
    print(slogo.decode('|'), '                              '+version_string+'                                     ', slogo.decode('|'))
    #print(slogo.decode('|'), '            Copyright (c) Wayne Chiu 2018. All Rights Reserved          ', slogo.decode('|'))
    print(slogo.decode('k--------------------------------------------------------------------------f'))
    print(slogo.decode('|'), '                                                                        ', slogo.decode('|'))
    print(slogo.decode('|'), '  1. build com port for test command                                    ', slogo.decode('|'))
    print(slogo.decode('|'), '              to be continue...                                         ', slogo.decode('|'))
    print(slogo.decode('p--------------------------------------------------------------------------q'))

def save_file_log(file_string, data_buffer, open_type):
    file = open(file_string+".txt", open_type)
    file.write(data_buffer)
    file.close()


def serial_open(ser):
    print('Port:', ser.port,' BaudRate:', ser.baudrate)
    if ser.isOpen():
        serial_close(ser)
        time.sleep(0.5)
    ser.open()

def serial_close(ser):
    ser.close()

def serial_write(ser,bytes1):

    if bytes1 is None:
        print(" No Such Command Found!")
        return None
    #ser.flushOutput()
    ser.write(bytes1)

def serial_read(ser):
    rx_data = 0
    time.sleep(1)
    if ser.inWaiting() > 0:
        rx_data = ser.read(ser.inWaiting())
        #time.sleep(0.1)
    return rx_data

def hci_command_test(ser,str1):
    global duration_time
    send_data = dataset.bt_command.generate_command(str1, True)

    list_byte = list(send_data)
    if Description_enable is True:
        dataset.bt_command.description_command(send_data)
        print('Send the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))

    serial_write(ser,send_data)
    #time.sleep(.3)
    for i in range(duration_time):
        time.sleep(.3)
        rx_buffer = serial_read(ser)
        if rx_buffer is not 0:
            list_byte = list(rx_buffer)
            if Description_enable is True:
                dataset.hciresponse.rx_data_analyzer(rx_buffer)
                print('Receive the data: 0x' + ' 0x'.join("{:02X}".format(b) for b in list_byte))
    duration_time = 1

def hci_command_test_by_inner_string(ser, str1):
    global duration_time
    send_data = test_command_set.get(str1)
    list_byte = list(send_data)

    if Description_enable is True:
        dataset.bt_command.description_command(send_data)
        print('Send the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))
    serial_write(ser,send_data)

    time.sleep(.3)
    for i in range(duration_time):
        time.sleep(.3)
        rx_buffer = serial_read(ser)
        if rx_buffer is not 0:
            list_byte = list(rx_buffer)
            if Description_enable is True:
                dataset.hciresponse.rx_data_analyzer(rx_buffer)
                print('Receive the data: 0x' + ' 0x'.join("{:02X}".format(b) for b in list_byte))
    duration_time = 1

def hci_command_test_by_std_raw(ser,list1):
    global duration_time
    send_data =b''
    for item in list1:
        hex_item = int(item,16)
        binary_data = int.to_bytes(hex_item,length=1,byteorder='big')
        send_data += binary_data
    if Description_enable is True:
        dataset.bt_command.description_command(send_data)
        print('Send the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list(send_data)))

    serial_write(ser,send_data)

    time.sleep(.3)

    for i in range(duration_time):
        time.sleep(.3)
        rx_buffer = serial_read(ser)
        if rx_buffer is not 0:
            list_byte = list(rx_buffer)
            if Description_enable is True:
                dataset.hciresponse.rx_data_analyzer(rx_buffer)
                print('Receive the data: 0x' + ' 0x'.join("{:02X}".format(b) for b in list_byte))
    duration_time = 1

def parse_args_check():
    parser = argparse.ArgumentParser(description='Usage for HCI Command Test')
    parser.add_argument('-v', '--version', action='version', version=' %(prog)s reversion: ' + version_string, help='Show the %(prog)s version.')
    parser.add_argument('--com', action='store', nargs=1, dest='com_port', help='COM Port')
    parser.add_argument('--baudrate', action='store', nargs=1, dest='baud_rate', help='Baudrate')
    parser.add_argument('--raw', action='store', nargs='*', dest='raw_data',  help='Using command with raw data.')
    parser.add_argument('--time', action='store', nargs=1, dest='duration', help='Scan event timer')
    parser.add_argument('-l','--license', action='store_true',dest='show_logo_switch',default=None,help='Show logo')
    args = parser.parse_args()
    if args.show_logo_switch is True:
        license_alarm()
        quit(0)
    if args.raw_data is not None:
        global raw_buffer
        raw_buffer = args.raw_data
    if args.com_port is not None:
        global serial1_port
        serial1_port = args.com_port[0]
    if args.baud_rate is not None:
        global serial_baudrate
        serial_baudrate = int(args.baud_rate[0], 10)
    if args.duration is not None:
        global duration_time
        duration_time = int(args.duration[0], 10)

def main():
    global raw_buffer
    command_for_return_parameter = None
    parse_args_check()

    #init...
    #serial_baudrate1 = int(serial_baudrate,0)
    ser = serial.Serial(serial1_port,serial_baudrate,timeout=None, xonxoff=False,rtscts=False,dsrdtr=False)
    serial_open(ser)

    '''    hci_command_test(ser, 'HCI_Read_Local_Supported_Features')
    hci_command_test(ser, 'HCI_LE_Set_Event_Mask')
    hci_command_test(ser, 'HCI_LE_Read_Buffer_Size')
    hci_command_test(ser, 'HCI_Read_Buffer_Size')
    hci_command_test(ser,'HCI_LE_Read_Local_Supported_Features')
    hci_command_test(ser, 'HCI_Read_BD_ADDR')
    hci_command_test(ser, 'HCI_Read_Local_Name')
    hci_command_test(ser, 'HCI_Read_Local_Version_Information')
    hci_command_test(ser, 'HCI_Inquiry')
    hci_command_test(ser, 'HCI_Inquiry_Cancel')'''



    hci_command_test_by_std_raw(ser,raw_buffer)
    #hci_command_test_by_inner_string(ser, 'HCI Inquiry Cancel')
    serial_close(ser)

if __name__ == '__main__':
    main()