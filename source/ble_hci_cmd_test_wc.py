import sys
import os
import argparse
import time
import serial
import dataset.bt_command
import dataset.showlogo as slogo
import dataset.hciresponse
##https://stackoverflow.com/questions/15570526/sending-hex-over-serial-with-python

#Global Variable

path = os.getcwd() + '\\'
app_name = __file__.replace(path,'')
version_string = "0.0.1"
Description_enable = True
#log
#20180419 add the serial command test


#Basic Configuration
serial1_port="COM5"
serial_baudrate=115200

test_command_set = {
    'HCI Inquiry'        : b'\x01\x01\x04\x05\x33\x8B\x9E\x30\x00', #LAP = 0x9E8B33 Len=0x30
    'HCI Inquiry1'        : b'\x01\x01\x04\x05\x00\x00\x00\x00\x00', #LAP = 0x9E8B33 Len=0x30
    'HCI Inquiry Cancel' : b'\x01\x44\x04\x00',
}

def license_alarm():
    print(slogo.decode('+--------------------------------------------------------------------------%'))
    print(slogo.decode('|'), '            Python BLE HCI Command Test  - ', app_name, slogo.decode('      |'))
    print(slogo.decode('|'), '                              '+version_string+'                                     ', slogo.decode('|'))
    print(slogo.decode('|'), '            Copyright (c) Wayne Chiu 2018. All Rights Reserved          ', slogo.decode('|'))
    print(slogo.decode('k--------------------------------------------------------------------------f'))
    print(slogo.decode('|'), '                                                                        ', slogo.decode('|'))
    print(slogo.decode('|'), '  1. build com port for test command                                    ', slogo.decode('|'))
    print(slogo.decode('|'), '              to be continue...                                         ', slogo.decode('|'))
    print(slogo.decode('p--------------------------------------------------------------------------q'))

def description_command(str1):
    find_it, target_group = dataset.bt_command.find_command(str1)
    if find_it is True:
        command_number =  int.from_bytes(dataset.bt_command.find_command_number(str1),byteorder='big')
        command_number_string= '(0x'+''.join("{:02X} ".format(command_number))+')'
        target_group_number = int.from_bytes(dataset.bt_command.opcode_group_field_set.get(target_group),byteorder='big')
        target_group_number_string = '(0x'+''.join("{:02X} ".format(target_group_number))+')'
    else:
        command_number_string = '(None)'
        target_group_number_string = '(None)'
    print(slogo.decode('+--------------------------------------------------------------------------%'))
    print(slogo.decode('|'),' CMD: ',str1, command_number_string)
    print(slogo.decode('|'),' GROUP: ',target_group,target_group_number_string)
    print(slogo.decode('|'),str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
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

def command_hci_read_local_support_feature(ser):
    send_data = dataset.bt_command.generate_command('HCI Read Local Supported Features')
    print(send_data)
    serial_write(ser,send_data)
    time.sleep(.1)
    rx_buffer = serial_read(ser)
    print(rx_buffer)

def hci_command_test(ser,str1):
    send_data = dataset.bt_command.generate_command(str1)
    if Description_enable is True:
        description_command(str1)

    list_byte = list(send_data)
    if Description_enable is True:
        print('Send the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))
    serial_write(ser,send_data)

    time.sleep(.1)

    rx_buffer = serial_read(ser)

    print('check',rx_buffer)
    #quit()
    list_byte = list(rx_buffer)
    print('check',list_byte)
    #quit()

    if Description_enable is True:
        dataset.hciresponse.rx_data_analyzer(rx_buffer)
        print('Receive the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))

def hci_command_raw_test(ser, str1):
    send_data = test_command_set.get(str1)
    if Description_enable is True:
        description_command(str1)

    list_byte = list(send_data)
    if Description_enable is True:
        print('Send the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))
    serial_write(ser,send_data)

    time.sleep(.3)

    rx_buffer = serial_read(ser)
    print('raw check',rx_buffer)
    #quit()
    list_byte = list(rx_buffer)
    print('raw check',list_byte)
    #quit()
    if Description_enable is True:
        dataset.hciresponse.rx_data_analyzer(rx_buffer)
        print('Receive the data: 0x'+' 0x'.join("{:02X}".format(b) for b in list_byte))

def parse_args_check():
    parser = argparse.ArgumentParser(description='Usage for HCI Command Test')
    parser.add_argument('-v', '--version', action='version', version=' %(prog)s reversion: ' + version_string
                        , help='Show the %(prog)s version.')
    parser.add_argument('-r', '--raw', help='Using command with raw data.')
    parser.add_argument('-l','--license', action='store_true',dest='show_logo_switch',default=None,help='Show logo')
    args = parser.parse_args()
    if args.show_logo_switch is True:
        license_alarm()

def main():
    '''
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Simple_tree() Argument List:' , str(sys.argv))
    print(app_name)
    '''
    parse_args_check()
    #resp.display_response()

    '''
    #init...
    ser = serial.Serial(serial1_port,serial_baudrate,timeout=None, xonxoff=False,rtscts=False,dsrdtr=False)
    serial_open(ser)

    #hci_command_test(ser, 'HCI Read RSSI')
    #hci_command_test(ser, 'HCI Inquiry Cancel')
    #hci_command_test(ser, 'HCI Read Local Supported Commands')
    #time.sleep(1)
    hci_command_test(ser, 'HCI Exit Periodic Inquiry Mode')
    #hci_command_raw_test(ser, 'HCI Inquiry Cancel')
    #hci_command_raw_test(ser, 'HCI Inquiry')
    #hci_command_raw_test(ser, 'HCI Inquiry1')
    #hci_command_test(ser,'HCI Read Local Supported Features')
    #hci_command_test(ser,'HCI Read Buffer Size')
    #hci_command_test(ser, 'HCI Read BD_ADDR')
    #if serial1_Enable==True:
    serial_close(ser)
    '''



if __name__ == '__main__':
    main()