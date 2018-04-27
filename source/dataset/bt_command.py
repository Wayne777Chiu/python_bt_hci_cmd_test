import binascii
import logging
from dataset.bt_command_parameter import command_parameter_length_set
import dataset.showlogo as slogo
import time

#data command
link_control_command_set = {
    'HCI Inquiry'                                   : b'\x01',
    'HCI Inquiry Cancel'                            : b'\x02',                      
    'HCI Periodic Inquiry Mode'                     : b'\x03',             
    'HCI Exit Periodic Inquiry Mode'                : b'\x04',                  
    'HCI Create Connection'                         : b'\x05',         
    'HCI Disconnect'                                : b'\x06',  
    'HCI Add SCO Connection'                        : b'\x07',          
    'HCI Create Connection Cancel'                  : b'\x08',                
    'HCI Accept Connection Request'                 : b'\x09',                 
    'HCI Reject Connection Request'                 : b'\x0A',                 
    'HCI Link Key Request Reply'                    : b'\x0B',              
    'HCI Link Key Request Negative Reply'           : b'\x0C',                       
    'HCI PIN Code Request Reply'                    : b'\x0D',              
    'HCI PIN Code Request Negative Reply'           : b'\x0E',                       
    'HCI Change Connection Packet Type'             : b'\x0F',                     
    'HCI Authentication Requested'                  : b'\x11',                
    'HCI Set Connection Encryption'                 : b'\x13',                 
    'HCI Change Connection Link Key'                : b'\x15',                  
    'HCI Master Link Key'                           : b'\x17',       
    'HCI Remote Name Request'                       : b'\x19',           
    'HCI Remote Name Request Cancel'                : b'\x1A',                  
    'HCI Read Remote Supported Features'            : b'\x1B',                      
    'HCI Read Remote Extended Features'             : b'\x1C',                     
    'HCI Read Remote Version Information'           : b'\x1D',                       
    'HCI Read Clock Offset'                         : b'\x1F',         
    'HCI Read LMP Handle'                           : b'\x20',       
    'HCI Exchange Fixed Info'                       : b'\x21',           
    'HCI Exchange Alias Info'                       : b'\x22',           
    'HCI Private Pairing Request Reply'             : b'\x23',                     
    'HCI Private Pairing Request Negative Reply'    : b'\x24',                              
    'HCI Generated Alias'                           : b'\x25',       
    'HCI Alias Address Request Reply'               : b'\x26',                   
    'HCI Alias Address Request Negative Reply'      : b'\x27',                            
    'HCI Setup Synchronous Connection'              : b'\x28',                    
    'HCI Accept Synchronous Connection Request'     : b'\x29',                             
    'HCI Reject Synchronous Connection Request'     : b'\x2A',                             
    'HCI IO Capability Request Reply'               : b'\x2B',                   
    'HCI User Confirmation Reqest Reply'            : b'\x2C',                      
    'HCI User Confirmation Reqest Negative Reply'   : b'\x2D',                               
    'HCI User Passkey Request Reply'                : b'\x2E',                  
    'HCI User Passkey Request Negative Reply'       : b'\x2F',                           
    'HCI Remote OOB Data Request Reply'             : b'\x30',                     
    'HCI Remote OOB Data Request Negative Reply'    : b'\x33',                              
    'HCI IO Capability Request Negative Reply'      : b'\x34',                            
}
policy_command_set = {
    'HCI Hold Mode'                                 : b'\x01',
    'HCI Sniff Mode'                                : b'\x03',
    'HCI Exit Sniff Mode'                           : b'\x04',        
    'HCI Park State'                                : b'\x05',   
    'HCI Exit Park State'                           : b'\x06',        
    'HCI QoS Setup'                                 : b'\x07',  
    'HCI Role Discovery'                            : b'\x09',       
    'HCI Switch Role'                               : b'\x0B',    
    'HCI Read Link Policy Settings'                 : b'\x0C',                  
    'HCI Write Link Policy Settings'                : b'\x0D',
    'HCI Read Default Link Policy Settings'         : b'\x0E',                          
    'HCI Write Default Link Policy Settings'        : b'\x0F',
    'HCI Flow Specification'                        : b'\x10',           
    'HCI Sniff Subrating'                           : b'\x11',        
}

host_control_and_baseband_command_set = {
    'HCI Set Event Mask'                            : b'\x01',                
    'HCI Reset'                                     : b'\x03',       
    'HCI Set Event Filter'                          : b'\x05',                  
    'HCI Flush'                                     : b'\x08',       
    'HCI Read PIN Type'                             : b'\x09',               
    'HCI Write PIN Type'                            : b'\x0A',                
    'HCI Create New Unit Key'                       : b'\x0B',                     
    'HCI Read Stored Link Key'                      : b'\x0D',                      
    'HCI Write Stored Link Key'                     : b'\x11',                       
    'HCI Delete Stored Link Key'                    : b'\x12',                        
    'HCI Write Local Name'                          : b'\x13',                  
    'HCI Read Local Name'                           : b'\x14',                 
    'HCI Read Connection Accept Timeout'            : b'\x15',                                
    'HCI Write Connection Accept Timeout'           : b'\x16',                                 
    'HCI Read Page Timeout'                         : b'\x17',                   
    'HCI Write Page Timeout'                        : b'\x18',                    
    'HCI Read Scan Enable'                          : b'\x19',                  
    'HCI Write Scan Enable'                         : b'\x1A',                   
    'HCI Read Page Scan Activity'                   : b'\x1B',                         
    'HCI Write Page Scan Activity'                  : b'\x1C',                          
    'HCI Read Inquiry Scan Activity'                : b'\x1D',                            
    'HCI Write Inquiry Scan Activity'               : b'\x1E',                             
    'HCI Read Authentication Enable'                : b'\x1F',                            
    'HCI Write Authentication Enable'               : b'\x20',                             
    'HCI Read Encryption Mode'                      : b'\x21',                      
    'HCI Write Encryption Mode'                     : b'\x22',                       
    'HCI Read Class of Device'                      : b'\x23',                      
    'HCI Write Class of Device'                     : b'\x24',                       
    'HCI Read Voice Setting'                        : b'\x25',                    
    'HCI Write Voice Setting'                       : b'\x26',                     
    'HCI Read Automatic Flush Timeout'              : b'\x27',                              
    'HCI Write Automatic Flush Timeout'             : b'\x28',                               
    'HCI Read Num Broadcast Retransmissions'        : b'\x29',                                    
    'HCI Write Num Broadcast Retransmissions'       : b'\x2A',                                     
    'HCI Read Hold Mode Activity'                   : b'\x2B',                         
    'HCI Write Hold Mode Activity'                  : b'\x2C',                          
    'HCI Read Transmit Power Level'                 : b'\x2D',                           
    'HCI Read Synchronous Flow Control Enable'      : b'\x2E',                                      
    'HCI Write Synchronous Flow Control Enable'     : b'\x2F',                                       
    'HCI Set Controller to Host Flow Control'       : b'\x31',                                     
    'HCI Host Buffer Size'                          : b'\x33',                  
    'HCI Host Number Of Completed Packets'          : b'\x35',                                  
    'HCI Read Link Supervision Timeout'             : b'\x36',                               
    'HCI Write Link Supervision Timeout'            : b'\x37',                                
    'HCI Read Number of Supported IAC'              : b'\x38',                              
    'HCI Read Current IAC LAP'                      : b'\x39',                      
    'HCI Write Current IAC LAP'                     : b'\x3A',                       
    'HCI Read Page Scan Period Mode'                : b'\x3B',                            
    'HCI Write Page Scan Period Mode'               : b'\x3C',                             
    'HCI Read Page Scan Mode'                       : b'\x3D',                     
    'HCI Write Page Scan Mode'                      : b'\x3E',                      
    'HCI Set AFH Host Channel Classification'       : b'\x3F',                                     
    'HCI Read Inquiry Scan Type'                    : b'\x42',                        
    'HCI Write Inquiry Scan Type'                   : b'\x43',                         
    'HCI Read Inquiry Mode'                         : b'\x44',                   
    'HCI Write Inquiry Mode'                        : b'\x45',                    
    'HCI Read Page Scan Type'                       : b'\x46',                     
    'HCI Write Page Scan Type'                      : b'\x47',                      
    'HCI Read AFH Channel Assessment Mode'          : b'\x48',                                  
    'HCI Write AFH Channel Assessment Mode'         : b'\x49',                                   
    'HCI Read Anonymity Mode'                       : b'\x4A',                     
    'HCI Write Anonymity Mode'                      : b'\x4B',                      
    'HCI Read Alias Authentication Enable'          : b'\x4C',                                  
    'HCI Write Alias Authentication Enable'         : b'\x4D',                                   
    'HCI Read Anonymous Address Change Parameters'  : b'\x4E',                                          
    'HCI Write Anonymous Address Change Parameters' : b'\x4F',                                          
    'HCI Reset Fixed Address Attempts Counter'      : b'\x50',                                      
    'HCI Read Extended Inquiry Response'            : b'\x51',                                
    'HCI Write Extended Inquiry Response'           : b'\x52',                                 
    'HCI Refresh Encryption Key'                    : b'\x53',                        
    'HCI Read SSP Mode'                             : b'\x55',               
    'HCI Write SSP Mode'                            : b'\x56',                
    'HCI Read Local OOB Data Command'               : b'\x57',                             
    'HCI Read Inquiry Response Transmit Power Level': b'\x58',                                       
    'HCI Write Inquiry Transmit Power Level'        : b'\x59',                                          
    'HCI Read Default Erroneous Data Reporting'     : b'\x5A',                                       
    'HCI Write Default Erroneous Data Reporting'    : b'\x5B',                                        
    'HCI Enhanced Flush Command'                    : b'\x5F',                        
    'HCI Send KeyPress Notification Command'        : b'\x60',                                    
    'HCI Read Enhanced Transmit Power Level'        : b'\x68',                                    
}
informational_command_set = {
    'HCI Read Local Version Information'            : b'\x01',                          
    'HCI Read Local Supported Commands'             : b'\x02',                         
    'HCI Read Local Supported Features'             : b'\x03',                         
    'HCI Read Local Extended Features'              : b'\x04',                        
    'HCI Read Buffer Size'                          : b'\x05',            
    'HCI Read Country Code'                         : b'\x07',             
    'HCI Read BD_ADDR'                              : b'\x09',        
}

status_command_set = {
    'HCI Read Failed Contact Counter'               : b'\x01',                           
    'HCI Reset Failed Contact Counter'              : b'\x02',                            
    'HCI Read Link Quality'                         : b'\x03',                 
    'HCI Read RSSI'                                 : b'\x05',         
    'HCI Read AFH Channel Map'                      : b'\x06',                    
    'HCI Read Clock'                                : b'\x07',          
    'HCI Read Encryption Key Size'                  : b'\x08',                        
}

test_command_set = {
    'HCI Read Loopback Mode'                        : b'\x01',       
    'HCI Write Loopback Mode'                       : b'\x02',        
    'HCI Enable Device Under Test Mode'             : b'\x03',                  
    'HCI Write SSP Debug Mode'                      : b'\x04',         
}

le_command_set = {
    'HCI LE Set Event Mask'                         : b'\x01',                  
    'HCI LE Read Buffer Size'                       : b'\x02',                    
    'HCI LE Read Local Supported Features'          : b'\x03',                                 
    'HCI LE Set Random Address'                     : b'\x05',                      
    'HCI LE Set Advertising Parameters'             : b'\x06',                              
    'HCI LE Read Advertising Channel Tx Power'      : b'\x07',                                     
    'HCI LE Set Advertising Data'                   : b'\x08',                        
    'HCI LE Set Scan Response Data '                : b'\x09',                           
    'HCI LE Set Advertise Enable'                   : b'\x0A',                        
    'HCI LE Set Scan Parameters'                    : b'\x0B',                       
    'HCI LE Set Scan Enable'                        : b'\x0C',                   
    'HCI LE Create Connection'                      : b'\x0D',                     
    'HCI LE Create Connection Cancel'               : b'\x0E',                            
    'HCI LE Read White List Size'                   : b'\x0F',                        
    'HCI LE Clear White List'                       : b'\x10',                    
    'HCI LE Add Device to White List'               : b'\x11',                            
    'HCI LE Remove Device from White List'          : b'\x12',                                 
    'HCI LE Connection Update'                      : b'\x13',                     
    'HCI LE Set Host Channel Classification'        : b'\x14',                                   
    'HCI LE Read Channel Map'                       : b'\x15',                    
    'HCI LE Read Remote Used Features'              : b'\x16',                             
    'HCI LE Encrypt'                                : b'\x17',           
    'HCI LE Rand'                                   : b'\x18',        
    'HCI LE Start Encryption'                       : b'\x19',                    
    'HCI LE Long Term Key Request Reply'            : b'\x1A',                               
    'HCI LE Long Term Key Request Negative Reply'   : b'\x1B',                                        
    'HCI LE Read Supported States'                  : b'\x1C',                         
    'HCI LE Receiver Test'                          : b'\x1D',                 
    'HCI LE Transmitter Test'                       : b'\x1E',                    
    'HCI LE Test End'                               : b'\x1F',            
}

smp_command_set = {
    'SMP Configure Security'                        : b'\x01',              
    'SMP Initiate Security'                         : b'\x02',             
    'SMP PassKey Reply'                             : b'\x03',         
    'SMP OOB Data Reply'                            : b'\x04',          
}

tci_command_set = {
'TCI Activate Remote DUT'                           : b'\x02',                     
'TCI Control Remote DUT'                            : b'\x03',                   
'TCI Increase Remote Power'                         : b'\x04',                     
'TCI Write Local Hop Frequencies'                   : b'\x05',
'TCI Read Local Hardware Version'                   : b'\x06',                             
'TCI Decrease Remote Power'                         : b'\x07',                       
'TCI Increase Local Volume'                         : b'\x08',                       
'TCI Decrease Local Volume'                         : b'\x09',                       
'TCI Write Local Native Clock'                      : b'\x0A',                          
'TCI Read Local Native Clock'                       : b'\x0B',                         
'TCI Read Local Relative Mips'                      : b'\x0C',                          
'TCI Type Approval Tester Control'                  : b'\x0D',                              
'TCI Increment Local Failed Attempts Counter'       : b'\x0E',                                         
'TCI Clear Local Failed Attempts Counter'           : b'\x0F',                                     
'TCI Read Local Default Packet Type'                : b'\x10',                                
'TCI Write Local Default Packet Type'               : b'\x11',                                 
'TCI Write Local SyncWord'                          : b'\x12',                      
'TCI Write Local Hopping Mode'                      : b'\x13',                          
'TCI Read Local Hopping Mode'                       : b'\x14',                         
'TCI Write Local Whitening Enable'                  : b'\x15',                              
'TCI Read Local Whitening Enable'                   : b'\x16',                             
'TCI Write Local Radio Power'                       : b'\x17',                         
'TCI Read Local Radio Power'                        : b'\x18',                        
'TCI Write Local Am Addr'                           : b'\x19',                     
'TCI Write Local Device Address'                    : b'\x1A',                            
'TCI Write Local Link Key Type'                     : b'\x1B',                           
'TCI Read Local Link Key Type'                      : b'\x1C',                          
'TCI Read Local Extended Features'                  : b'\x1D',                              
'TCI Write Local Features'                          : b'\x1E',                      
'TCI Write Local Extended Features'                 : b'\x1F',                               
'TCI Read Local Timing Information'                 : b'\x2A',                               
'TCI Write Local Timing Information'                : b'\x2B',                                
'TCI Read Remote Timing Information'                : b'\x2C',                                
'TCI Write Local Hardware Register'                 : b'\x2D',                               
'TCI Reset Local Baseband Monitors'                 : b'\x2E',                               
'TCI Update Manufacturing Information'              : b'\x2F',                                 
'TCI Write Local Radio Register'                    : b'\x30',                           
'TCI Read Local Radio Register'                     : b'\x31',                          
'TCI Change Radio Modulation'                       : b'\x32',                        
'TCI Read Radio Modulation'                         : b'\x33',                      
'TCI Write UART Baud Rate'                          : b'\x34',                     
'TCI Reset Local Pump Monitors'                     : b'\x3A',                          
'TCI Read Local Pump Monitors'                      : b'\x3B',                         
'TCI Write Local Encryption Key Length'             : b'\x3C',                                  
'TCI Read Local Encryption Key Length'              : b'\x3D',                                 
'TCI Read Local Hop Frequencies'                    : b'\x3E',                           
'TCI Read Local Baseband Monitors'                  : b'\x3F',                             
'TCI Disable Low Power Mode'                        : b'\x40',                       
'TCI Enable Low Power Mode'                         : b'\x41',                      
'TCI Read Minimum Search Window'                    : b'\x42',                           
'TCI Write Minimum Search Window'                   : b'\x43',                            
'TCI Disable SCO/eSCO Via HCI'                      : b'\x44',                         
'TCI Enable SCO/eSCO Via HCI'                       : b'\x45',                        
'TCI Write eSCO Retransmission Mode'                : b'\x46',                               
'TCI Read eSCO Retransmission Mode'                 : b'\x47',                              
'TCI Write Enhanced Power Control Mode'             : b'\x48',                                  
'TCI Write PTA Mode'                                : b'\x49',               
'TCI Write Park Parameters'                         : b'\x50',                      
'TCI Read Unused Stack Size'                        : b'\x51',                       
'TCI Write AFH Control'                             : b'\x60',                  
'TCI Read Raw RSSI'                                 : b'\x61',              
'TCI Read BER'                                      : b'\x62',         
'TCI Read PER'                                      : b'\x63',         
'TCI Read Raw RSSI PER BER'                         : b'\x64',                      
'TCI Override ARQN With NAK'                        : b'\x65',                       
'TCI LE Set Transmit Window Params'                 : b'\x6A',                              
'TCI LE Set Direct Advertising Timeout'             : b'\x6B',                                  
'TCI LE Set TIFS Tx Adjustment'                     : b'\x6C',                          
'TCI LE Set Search Window Delay'                    : b'\x6D',                           
'TCI LE Auto Advertising After Disconnect Of Slave' : b'\x70',                                              
'TCI LE Auto Initiate After Disconnect Of Master'   : b'\x71',                                            
'TCI LE Read Advertising Parameters'                : b'\x72',                               
'TCI LE Write Advertising Delta'                    : b'\x73',                           
'TCI LE Write Num Packets Per CE'                   : b'\x74',                            
'TCI LE Echo Transmit Window Size and Offset'       : b'\x75',                                        
'TCI LE Get Device States'                          : b'\x76',                     
'TCI LE Read Scan Backoff Info'                     : b'\x77',                          
'TCI LE Write Scan Frequencies'                     : b'\x78',                          
'TCI LE Read Scan Frequencies'                      : b'\x79',                         
'TCI LE Write Initiating Frequencies'               : b'\x7A',                                
'TCI LE Read Initiating Frequencies'                : b'\x7B',                               
'TCI LE Num Times Master Doesnt Tx In 1st Win'      : b'\x7C',                                         
'TCI LE Slave Listen Outside Latency'               : b'\x7D',                                
'TCI LE Read Peer SCA'                              : b'\x7E',                 
'TCI LE Read Session Key'                           : b'\x7F',                    
'TCI LE Read Hop Increment'                         : b'\x80',                      
'TCI LE Read Access Address'                        : b'\x81',                       
'TCI LE Whitening'                                  : b'\x82',             
'TCI LE Scan Backoff Control'                       : b'\x83',                        
'TCI LE PreConfigure Hop Increment'                 : b'\x84',                              
'TCI LE PreConfigure Access Address'                : b'\x85',                               
'TCI LE Direct Advertising Timeout'                 : b'\x86',                              
'TCI LE Read Scan Parameters'                       : b'\x87',                        
'TCI LE Set Trace Level'                            : b'\x88',                                                  
}

packet_type_set = {
	'Command'          : b'\x01',   
	'Asynchronous Data': b'\x02',             
	'Synchronous Data' : b'\x03',            
	'Event'            : b'\x04', 
}

opcode_group_field_set = {
	'link_control_command_set'             : b'\x01',            
	'policy_command_set'                   : b'\x02',      
	'host_control_and_baseband_command_set': b'\x03',                         
	'informational_command_set'            : b'\x04',             
	'status_command_set'                   : b'\x05',      
	'test_command_set'                     : b'\x06',    
	'le_command_set'                       : b'\x08',  
	'smp_command_set'                      : b'\x09',   
	'tci_command_set'                      : b'\x3F',   
}

def description_command(command_data):
    #if parameter is string ==> command string
    #if parameter is opcode ==> byte'\xNN\xNN' (byteorder = 'little'
    find_it, target_group, target_command = find_command(command_data)

    if find_it is True:
        command_number =  int.from_bytes(find_command_number(target_command),byteorder='big')
        command_number_string= '(0x'+''.join("{:02X} ".format(command_number))+')'

        target_group_number = int.from_bytes(opcode_group_field_set.get(target_group), byteorder='big')
        target_group_number_string = '(0x'+''.join("{:02X} ".format(target_group_number))+')'

        if isinstance(command_data,str):
            opcode_number_little = opcode_combine(target_group_number,command_number)
        else:
            opcode_number_little = command_data
        #opcode_number_big = struct.pack('<1h', *struct.unpack('>1h',opcode_number_little))
        opcode_number = int.from_bytes(opcode_number_little,byteorder='little')
        opcode_number_string=  '(0x'+''.join("{:04X} ".format(opcode_number)) +')'

    else:
        command_number_string = '(None)'
        target_group_number_string = '(None)'
        opcode_number_string = '(None)'
    print(slogo.decode('+--------------------------------------------------------------------------%'))
    print(slogo.decode('|'),' CMD: ',target_command, command_number_string)
    print(slogo.decode('|'),' GROUP: ',target_group,target_group_number_string)
    print(slogo.decode('|'),' OPCODE: ',opcode_number_string)
    print(slogo.decode('|'),str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
    print(slogo.decode('p--------------------------------------------------------------------------q'))

def opcode_combine(ogf_data,ocf_data):
    if isinstance(ogf_data,str) and isinstance(ogf_data,str):
        opcode_group_field = int.from_bytes(opcode_group_field_set.get(ogf_data),byteorder='big')
        opcode_command_field = int.from_bytes(eval(ogf_data)[ocf_data],byteorder='big')

    else : #isinstance(ogf_data,int) and isinstance(ogf_data,int):
        opcode_group_field = ogf_data
        opcode_command_field = ocf_data

    #we need the step to converse data to integer ocf_data
    opcode_high_byte = opcode_group_field << 10

    #this will make the opcode to byte adding
    #opcode = int.to_bytes(opcode_group_field << 10 + opcode_command_field,length=2,byteorder='big')
    opcode = int.to_bytes(opcode_high_byte + opcode_command_field,length=2,byteorder='little')
    return opcode


#find command has two searching rule
#    by command string
#    by opcode (byte type '\xNN\xNN'
def find_command(command_data):
    find_it = False
    target_group=None
    target_command=None
    if isinstance(command_data, str):
        for command_set in opcode_group_field_set:
            value = eval(command_set).get(command_data)
            if value is not None:
                find_it = True
                target_group = command_set
                target_command = command_data
                break
    else:
        opcode_int = int.from_bytes(command_data,byteorder='little')
        target_group_number = opcode_int >> 10
        target_command_number = opcode_int & 0x3ff

        for command_set in opcode_group_field_set:

            if int.from_bytes(opcode_group_field_set[command_set],byteorder='big') == target_group_number:
                for single_command in  eval(command_set):
                    if int.from_bytes(eval(command_set).get(single_command),byteorder='big') == target_command_number:
                        find_it = True
                        target_group = command_set
                        target_command = single_command
                        break
    return find_it,target_group,target_command

def find_command_number(str1):
    command_number  = None
    for command_set in opcode_group_field_set:
        value = eval(command_set).get(str1)
        if value is not None:
            command_number = value
            break
    return command_number

def find_parameter_length(str1):
    find_it, target_group, target_command = find_command(str1)
    if find_it is not None:
        group_index = list(opcode_group_field_set.keys()).index(target_group)
        command_index = list(eval(target_group).keys()).index(str1)
        length_data = command_parameter_length_set[group_index][command_index]
        return find_it,length_data
    else:
        return None

def append_packet_type(str1,buffer):
    return packet_type_set.get(str1) + buffer

def append_length_parameter(str1,previous_buffer):
    find_it, length_data = find_parameter_length(str1)
    if find_it is not None:
        if length_data == 0:
            return previous_buffer + int.to_bytes(length_data,length=1,byteorder='big')
        else:
            print('Need update the code!!')
    else:
        logging.error("Cannot find the parameter-length: "+ str1)
        return False

def generate_command(str1):
    find_it, target_group, target_command = find_command(str1)
    if find_it is True:
        target_opcode = opcode_combine(target_group,str1)
        data_with_command_type = append_packet_type('Command', target_opcode)
        send_data = append_length_parameter(str1,data_with_command_type)
        return send_data

'''
def main():
    packet1 = opcode_combine('link_control_command_set','HCI Inquiry')
    packet2 = opcode_combine('informational_command_set', 'HCI Read Local Supported Features')
    #print(find_command('HCI Inquiry'))
    print(append_packet_type('Command',packet1))
    print(append_packet_type('Command',packet2))
    print(append_length_parameter('HCI Inquiry',append_packet_type('Command', packet1)))
    print(append_length_parameter('HCI Read Local Supported Features',append_packet_type('Command', packet2)))


if __name__ == '__main__':
    main()
'''


