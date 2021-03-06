import dataset.showlogo as slogo
import dataset.bt_hci_parameter
import dataset.bt_event_parameter
import dataset.bt_command_parameter

LE_EVENT_CODE = 0x3E

event_code_set={
    'Inquiry Complete'                                  : b'\x01',         
    'Inquiry Result'                                    : b'\x02',       
    'Connection Complete'                               : b'\x03',            
    'Connection Request'                                : b'\x04',           
    'Disconnection Complete'                            : b'\x05',               
    'Authentication Complete'                           : b'\x06',                
    'Remote Name Request Complete'                      : b'\x07',                     
    'Encryption Change'                                 : b'\x08',          
    'Change Connection Link Key Complete'               : b'\x09',                            
    'Master Link Key Complete'                          : b'\x0A',                 
    'Read Remote Supported Features Complete'           : b'\x0B',                                
    'Read Remote Version Information Complete'          : b'\x0C',                                 
    'QoS Setup Complete'                                : b'\x0D',           
    'Command Complete'                                  : b'\x0E',         
    'Command Status'                                    : b'\x0F',       
    'Hardware Error'                                    : b'\x10',       
    'Flush Occurred'                                    : b'\x11',       
    'Role Change'                                       : b'\x12',    
    'Number Of Completed Packets'                       : b'\x13',                    
    'Mode Change'                                       : b'\x14',    
    'Return Link Keys'                                  : b'\x15',         
    'PIN Code Request'                                  : b'\x16',         
    'Link Key Request'                                  : b'\x17',         
    'Link Key Notification'                             : b'\x18',              
    'Loopback Command'                                  : b'\x19',         
    'Data Buffer Overflow'                              : b'\x1A',             
    'Max Slots Change'                                  : b'\x1B',         
    'Read Clock Offset Complete'                        : b'\x1C',                   
    'Connection Packet Type Changed'                    : b'\x1D',                       
    'QoS Violation'                                     : b'\x1E',      
    'Page Scan Mode Change'                             : b'\x1F',              
    'Page Scan Repetition Mode Change'                  : b'\x20',                         
    'Flow Specification Complete'                       : b'\x21',                    
    'Inquiry Result with RSSI'                          : b'\x22',                 
    'Read Remote Extended Features Complete'            : b'\x23',                               
    'Synchronous Connection Complete'                   : b'\x2C',                        
    'Synchronous Connection Changed'                    : b'\x2D',                       
    'Sniff Subrating'                                   : b'\x2E',        
    'Extended Inquiry Result'                           : b'\x2F',                
    'Encryption Key Refresh Complete'                   : b'\x30',                        
    'IO Capability Request'                             : b'\x31',              
    'IO Capability Response'                            : b'\x32',               
    'User Confirmation Request'                         : b'\x33',                  
    'User Passkey Request'                              : b'\x34',             
    'Remote OOB Data Request'                           : b'\x35',                
    'Simple Pairing Complete'                           : b'\x36',                
    'Link Supervision Timeout Changed'                  : b'\x38',                         
    'Enhanced Flush Complete'                           : b'\x39',                
    'User Passkey Notification'                         : b'\x3B',                  
    'Keypress Notification'                             : b'\x3C',              
    'Remote Host Supported Features Notification'       : b'\x3D',                                    
    'Physical Link Complete'                            : b'\x40',               
    'Channel Selected'                                  : b'\x41',         
    'Disconnection Physical Link Complete'              : b'\x42',                             
    'Physical Link Loss Early Warning'                  : b'\x43',                         
    'Physical Link Recovery'                            : b'\x44',               
    'Logical Link Complete'                             : b'\x45',              
    'Disconnection Logical Link Complete'               : b'\x46',                            
    'Flow Spec Modify Complete'                         : b'\x47',                  
    'Number Of Completed Data Blocks'                   : b'\x48',                        
    'AMP Start Test'                                    : b'\x49',       
    'AMP Test End'                                      : b'\x4A',     
    'AMP Receiver Report'                               : b'\x4B',            
    'Short Range Mode Change Complete'                  : b'\x4C',    
    'AMP Status Change'                                 : b'\x4D',   
    'LE Connection Complete'                            : b'\x3E',               
    'LE Advertising Report'                             : b'\x3E',              
    'LE Connection Update Complete'                     : b'\x3E',                      
    'LE Read Remote Features Complete'                  : b'\x3E',                         
    'LE Long Term Key Request'                          : b'\x3E',                 
    'LE Remote Connection Parameter Request'            : b'\x3E',                               
    'LE Data Length Change'                             : b'\x3E',              
    'LE Read Local P-256 Public Key Complete'           : b'\x3E',      
    'LE Generate DHKey Complete'                        : b'\x3E',                   
    'LE Enhanced Connection Complete'                   : b'\x3E',                        
    'LE Directed Advertising Report'                    : b'\x3E',                       
    'LE PHY Update Complete'                            : b'\x3E',               
    'LE Extended Advertising Report'                    : b'\x3E',                       
    'LE Periodic Advertising Sync Established'          : b'\x3E',                                 
    'LE Periodic Advertising Report'                    : b'\x3E',                       
    'LE Periodic Advertising Sync Lost'                 : b'\x3E',                          
    'LE Scan Timeout'                                   : b'\x3E',        
    'LE Advertising Set Terminated'                     : b'\x3E',                      
    'LE Scan Request Received'                          : b'\x3E',                 
    'LE Channel Selection Algorithm Event'              : b'\x3E',                             
    'Triggered Clock Capture'                           : b'\x4E',                
    'Synchronization Train Complete'                    : b'\x4F',                       
    'Synchronization Train Received'                    : b'\x50',                       
    'Connectionless Slave Broadcast Receive'            : b'\x51',                               
    'Connectionless Slave Broadcast Timeout'            : b'\x52',                               
    'Truncated Page Complete'                           : b'\x53',                
    'Slave Page Response Timeout'                       : b'\x54',                    
    'Connectionless Slave Broadcast Channel Map Change' : b'\x55',                                          
    'Inquiry Response Notification'                     : b'\x56',                      
    'Authenticated Payload Timeout Expired'             : b'\x57',                              
    'SAMStatusChange'                                   : b'\x58',                                       
}

sub_event_code_set = {
    'LE Connection Complete'                   : b'\x01',          
    'LE Advertising Report'                    : b'\x02',         
    'LE Connection Update Complete'            : b'\x03',                 
    'LE Read Remote Features Complete'         : b'\x04',                    
    'LE Long Term Key Request'                 : b'\x05',            
    'LE Remote Connection Parameter Request'   : b'\x06',                          
    'LE Data Length Change'                    : b'\x07',         
    'LE Read Local P-256 Public Key Complete'  : b'\x08',                           
    'LE Generate DHKey Complete'               : b'\x09',              
    'LE Enhanced Connection Complete'          : b'\x0A',                   
    'LE Directed Advertising Report'           : b'\x0B',                  
    'LE PHY Update Complete'                   : b'\x0C',          
    'LE Extended Advertising Report'           : b'\x0D',                  
    'LE Periodic Advertising Sync Established' : b'\x0E',                            
    'LE Periodic Advertising Report'           : b'\x0F',                  
    'LE Periodic Advertising Sync Lost'        : b'\x10',                     
    'LE Scan Timeout'                          : b'\x11',   
    'LE Advertising Set Terminated'            : b'\x12',                 
    'LE Scan Request Received'                 : b'\x13',            
    'LE Channel Selection Algorithm Event'     : b'\x14',                        
}

def check_sub_event_string(event_code):
    if event_code == LE_EVENT_CODE:
        return True
    else:
        return False

def get_event_string(e_code,dig_code):
    find_event = False
    event_string = None
    sub_event_string = 'N/A'
    for key, value in event_code_set.items():
        if int.from_bytes(value, byteorder='big') == e_code:
            find_event = True
            event_string = key
            break
    if find_event is True:
        find_sub_event = check_sub_event_string(e_code)
        if find_sub_event is True:
            for key, value in sub_event_code_set.items():
                if int.from_bytes(value, byteorder='big') == e_code:
                    sub_event_string = key
                    break

    return find_event,event_string,sub_event_string

def description_event(pdu_array):
    find_event, event_string, sub_event_string = get_event_string(pdu_array[1],pdu_array[2])
    find_sub_event = False
    index = 0
    parameter_list = []
    parameter_length = []
    parameter_value_string = []

    if find_event is True:
        if sub_event_string == 'N/A':
            find_sub_event = False
        else:
            sub_event_string = True

        temp_parameter_list =  dataset.bt_event_parameter.event_parameters_set.get(event_string)
        return_parameter_list = dataset.bt_command_parameter.command_return_parameters_set.get(dataset.bt_hci_parameter.command_for_return_parameter)

        if temp_parameter_list[0] is not None:
            for item in temp_parameter_list:
                if item == 'Return_Parameters':
                    for return_item in return_parameter_list:
                        if return_item is None:
                            parameter_list.append('TEMP_ITEM')
                            parameter_length.append(1)
                        else:
                            parameter_list.append(return_item)
                            parameter_length.append(dataset.bt_hci_parameter.parameters_configuration_set.get(return_item)[0])
                else:
                    parameter_length.append(dataset.bt_hci_parameter.parameters_configuration_set.get(item)[0])
                    parameter_list.append(item)
        else:
            parameter_length.append(0)

        parameter_limit = 0
        parameter_index = 0
        parameter_update = True
        temp_data_string=''

        if find_sub_event is True:
            parameter_start_index = 4
        else:
            parameter_start_index = 3

        for byte in pdu_array:
            if index == 0:
                packet_type = byte
            elif index == parameter_start_index -1:
                    parameter_total_length = byte
                    parameter_limit = parameter_length[parameter_index] + index
            elif index >= parameter_start_index and index <= parameter_limit:
                if parameter_update is True:
                    temp_data_string = ''.join("{:02X}".format(byte))
                    parameter_update = False
                else:
                    temp_data_string = ''.join("{:02X}".format(byte)) + temp_data_string

                if index == parameter_limit:
                    parameter_value_string.append(temp_data_string)
                    parameter_update = True
                    if parameter_index < parameter_length.__len__() - 1:
                        parameter_index += 1
                        parameter_limit = parameter_length[parameter_index] + index
            index += 1

        print(slogo.decode('+--------------------------------------------------------------------------%'))
        print(slogo.decode('|'), ' Event: ', event_string, '(0x' + ''.join("{:02X} ".format(pdu_array[1])) + ')')
        print(slogo.decode('|'), ' SUB-Event: ', sub_event_string, '(', sub_event_string, ')')
        print(slogo.decode('|'), ' Parameter Length: ', pdu_array[2], '                       ')
        print(slogo.decode('|'), ' Parameter: ',
              'Parameter (0x' + ' 0x'.join("{:02X}".format(b) for b in pdu_array[3:]) + ')')
        if not parameter_length:
            print('No  such Event ')
            quit(1)
        if parameter_length[0] == 0:
            print(slogo.decode('|'), ' No Parameter ')
        else:
            index = 0
            for item in parameter_list:

                if parameter_value_string.__len__() <= index:
                    print(slogo.decode('| '), '(Size:', parameter_length[index], ' Octet(s))', item, ' : ',
                          '( No Parameter Value )')
                else:
                    print(slogo.decode('| '), '(Size:', parameter_length[index], ' Octet(s))', item, ' : ',
                      '(0x' + parameter_value_string[index], ')')
                index += 1
        print(slogo.decode('p--------------------------------------------------------------------------q'))


