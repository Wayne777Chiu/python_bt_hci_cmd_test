import binascii
import logging
from dataset.bt_command_parameter import command_parameter_length_set
import dataset.showlogo as slogo
import time

#data command
link_control_command_set = {
    'HCI_Inquiry'                                           : b'\x01',          
    'HCI_Inquiry_Cancel'                                    : b'\x02',          
    'HCI_Periodic_Inquiry_Mode'                             : b'\x03',          
    'HCI_Exit_Periodic_Inquiry_Mode'                        : b'\x04',          
    'HCI_Create_Connection'                                 : b'\x05',          
    'HCI_Disconnect'                                        : b'\x06',          
    #'HCI Add SCO Connection'                                 b'\x07',          
    'HCI_Create_Connection_Cancel'                          : b'\x08',          
    'HCI_Accept_Connection_Request'                         : b'\x09',          
    'HCI_Reject_Connection_Request'                         : b'\x0A',          
    'HCI_Link_Key_Request_Reply'                            : b'\x0B',          
    'HCI_Link_Key_Request_Negative_Reply'                   : b'\x0C',          
    'HCI_PIN_Code_Request_Reply'                            : b'\x0D',          
    'HCI_PIN_Code_Request_Negative_Reply'                   : b'\x0E',          
    'HCI_Change_Connection_Packet_Type'                     : b'\x0F',          
    'HCI_Authentication_Requested'                          : b'\x11',          
    'HCI_Set_Connection_Encryption'                         : b'\x13',          
    'HCI_Change_Connection_Link_Key'                        : b'\x15',          
    'HCI_Master_Link_Key'                                   : b'\x17',          
    'HCI_Remote_Name_Request'                               : b'\x19',          
    'HCI_Remote_Name_Request_Cancel'                        : b'\x1A',          
    'HCI_Read_Remote_Supported_Features'                    : b'\x1B',          
    'HCI_Read_Remote_Extended_Features'                     : b'\x1C',          
    'HCI_Read_Remote_Version_Information'                   : b'\x1D',          
    'HCI_Read_Clock_Offset'                                 : b'\x1F',          
    'HCI_Read_LMP_Handle'                                   : b'\x20',          
    #'HCI Exchange Fixed Info'                               : b'\x21',          
    #'HCI Exchange Alias Info'                               : b'\x22',          
    #'HCI Private Pairing Request Reply'                     : b'\x23',          
    #'HCI Private Pairing Request Negative Reply'            : b'\x24',          
    #'HCI Generated Alias'                                   : b'\x25',          
    #'HCI Alias Address Request Reply'                       : b'\x26',          
    #'HCI Alias Address Request Negative Reply'              : b'\x27',          
    'HCI_Setup_Synchronous_Connection'                      : b'\x28',          
    'HCI_Accept_Synchronous_Connection_Request'             : b'\x29',          
    'HCI_Reject_Synchronous_Connection_Request'             : b'\x2A',          
    'HCI_IO_Capability_Request_Reply'                       : b'\x2B',          
    'HCI_User_Confirmation_Request_Reply'                   : b'\x2C',          
    'HCI_User_Confirmation_Request_Negative_Reply'          : b'\x2D',          
    'HCI_User_Passkey_Request_Reply'                        : b'\x2E',          
    'HCI_User_Passkey_Request_Negative_Reply'               : b'\x2F',          
    'HCI_Remote_OOB_Data_Request_Reply'                     : b'\x30',          
    'HCI_Remote_OOB_Data_Request_Negative_Reply'            : b'\x33',          
    'HCI_IO_Capability_Request_Negative_Reply'              : b'\x34',          
    'HCI_Create_Physical_Link'                              : b'\x35',    
    'HCI_Accept_Physical_Link'                              : b'\x36',    
    'HCI_Disconnect_Physical_Link'                          : b'\x37',    
    'HCI_Create_Logical_Link'                               : b'\x38',    
    'HCI_Accept_Logical_Link'                               : b'\x39',    
    'HCI_Disconnect_Logical_Link'                           : b'\x3A',    
    'HCI_Logical_Link_Cancel'                               : b'\x3B',    
    'HCI_Flow_Spec_Modify'                                  : b'\x3C',    
    'HCI_Enhanced_Setup_Synchronous_Connection'             : b'\x3D',    
    'HCI_Enhanced_Accept_Synchronous_Connection_Request'    : b'\x3E',    
    'HCI_Truncated_Page'                                    : b'\x3F',    
    'HCI_Truncated_Page_Cancel'                             : b'\x40',    
    'HCI_Set_Connectionless_Slave_Broadcast'                : b'\x41',    
    'HCI_Set_Connectionless_Slave_Broadcast_Receive'        : b'\x42',    
    'HCI_Start_Synchronization_Train'                       : b'\x43',    
    'HCI_ Receive_Synchronization_Train'                    : b'\x44',    
    'HCI_Remote_OOB_Extended_Data_Request_Reply'            : b'\x45',    
}

policy_command_set = {
    'HCI_Hold_Mode'                                         : b'\x01',
    'HCI_Sniff_Mode'                                        : b'\x03',
    'HCI_Exit_Sniff_Mode'                                   : b'\x04',
    #'HCI Park State'                                        : b'\x05',
    #'HCI Exit Park State'                                   : b'\x06',
    'HCI_QoS_Setup'                                         : b'\x07',
    'HCI_Role_Discovery'                                    : b'\x09',
    'HCI_Switch_Role'                                       : b'\x0B',
    'HCI_Read_Link_Policy_Settings'                         : b'\x0C',
    'HCI_Write_Link_Policy_Settings'                        : b'\x0D',
    'HCI_Read_Default_Link_Policy_Settings'                 : b'\x0E',
    'HCI_Write_Default_Link_Policy_Settings'                : b'\x0F',
    'HCI_Flow_Specification'                                : b'\x10',
    'HCI_Sniff_Subrating'                                   : b'\x11',
}
host_control_and_baseband_command_set = {
    'HCI_Set_Event_Mask'                                    : b'\x01',
    'HCI_Reset'                                             : b'\x03',
    'HCI_Set_Event_Filter'                                  : b'\x05',
    'HCI_Flush'                                             : b'\x08',
    'HCI_Read_PIN_Type'                                     : b'\x09',
    'HCI_Write_PIN_Type'                                    : b'\x0A',
    'HCI_Create_New_Unit_Key'                               : b'\x0B',
    'HCI_Read_Stored_Link_Key'                              : b'\x0D',
    'HCI_Write_Stored_Link_Key'                             : b'\x11',
    'HCI_Delete_Stored_Link_Key'                            : b'\x12',
    'HCI_Write_Local_Name'                                  : b'\x13',
    'HCI_Read_Local_Name'                                   : b'\x14',
    'HCI_Read_Connection_Accept_Timeout'                    : b'\x15',
    'HCI_Write_Connection_Accept_Timeout'                   : b'\x16',
    'HCI_Read_Page_Timeout'                                 : b'\x17',
    'HCI_Write_Page_Timeout'                                : b'\x18',
    'HCI_Read_Scan_Enable'                                  : b'\x19',
    'HCI_Write_Scan_Enable'                                 : b'\x1A',
    'HCI_Read_Page_Scan_Activity'                           : b'\x1B',
    'HCI_Write_Page_Scan_Activity'                          : b'\x1C',
    'HCI_Read_Inquiry_Scan_Activity'                        : b'\x1D',
    'HCI_Write_Inquiry_Scan_Activity'                       : b'\x1E',
    'HCI_Read_Authentication_Enable'                        : b'\x1F',
    'HCI_Write_Authentication_Enable'                       : b'\x20',
    #'HCI Read Encryption Mode'                              : b'\x21',
    #'HCI Write Encryption Mode'                             : b'\x22',
    'HCI_Read_Class_of_Device'                              : b'\x23',
    'HCI_Write_Class_of_Device'                             : b'\x24',
    'HCI_Read_Voice_Setting'                                : b'\x25',
    'HCI_Write_Voice_Setting'                               : b'\x26',
    'HCI_Read_Automatic_Flush_Timeout'                      : b'\x27',
    'HCI_Write_Automatic_Flush_Timeout'                     : b'\x28',
    'HCI_Read_Num_Broadcast_Retransmissions'                : b'\x29',
    'HCI_Write_Num_Broadcast_Retransmissions'               : b'\x2A',
    'HCI_Read_Hold_Mode_Activity'                           : b'\x2B',
    'HCI_Write_Hold_Mode_Activity'                          : b'\x2C',
    'HCI_Read_Transmit_Power_Level'                         : b'\x2D',
    'HCI_Read_Synchronous_Flow_Control_Enable'              : b'\x2E',
    'HCI_Write_Synchronous_Flow_Control_Enable'             : b'\x2F',
    'HCI_Set_Controller_To_Host_Flow_Control'               : b'\x31',
    'HCI_Host_Buffer_Size'                                  : b'\x33',
    'HCI_Host_Number_Of_Completed_Packets'                  : b'\x35',
    'HCI_Read_Link_Supervision_Timeout'                     : b'\x36',
    'HCI_Write_Link_Supervision_Timeout'                    : b'\x37',
    'HCI_Read_Number_Of_Supported_IAC'                      : b'\x38',
    'HCI_Read_Current_IAC_LAP'                              : b'\x39',
    'HCI_Write_Current_IAC_LAP'                             : b'\x3A',
    #'HCI_Read_Page_Scan_Period_Mode'                        : b'\x3B',
    #'HCI_Write_Page_Scan_Period_Mode'                       : b'\x3C',
    #'HCI_Read_Page_Scan_Mode'                               : b'\x3D',
    #'HCI_Write_Page_Scan_Mode'                              : b'\x3E',
    'Set_AFH_Host_Channel_Classification'                   : b'\x3F',
    'HCI_Read_Inquiry_Scan_Type'                            : b'\x42',
    'HCI_Write_Inquiry_Scan_Type'                           : b'\x43',
    'HCI_Read_Inquiry_Mode'                                 : b'\x44',
    'HCI_Write_Inquiry_Mode'                                : b'\x45',
    'HCI_Read_Page_Scan_Type'                               : b'\x46',
    'HCI_Write_Page_Scan_Type'                              : b'\x47',
    'Read_AFH_Channel_Assessment_Mode'                      : b'\x48',
    'Write_AFH_Channel_Assessment_Mode'                     : b'\x49',
    #'HCI Read Anonymity Mode'                               : b'\x4A',
    #'HCI Write Anonymity Mode'                              : b'\x4B',
    #'HCI Read Alias Authentication Enable'                  : b'\x4C',
    #'HCI Write Alias Authentication Enable'                 : b'\x4D',
    #'HCI Read Anonymous Address Change Parameters'          : b'\x4E',
    #'HCI Write Anonymous Address Change Parameters'         : b'\x4F',
    #'HCI Reset Fixed Address Attempts Counter'              : b'\x50',
    'HCI_Read_Extended_Inquiry_Response'                    : b'\x51',
    'HCI_Write_Extended_Inquiry_Response'                   : b'\x52',
    'HCI_Refresh_Encryption_Key'                            : b'\x53',
    'HCI_Read_Simple_Pairing_Mode'                          : b'\x55',
    'HCI_Write_Simple_Pairing_Mode'                         : b'\x56',
    'HCI_Read_Local_OOB_Data'                               : b'\x57',
    'HCI_Read_Inquiry_Response_Transmit_Power_Level'        : b'\x58',
    'HCI_Write_Inquiry_Transmit_Power_Level'                : b'\x59',
    'HCI_Read_Default_Erroneous_Data_Reporting'             : b'\x5A',
    'HCI_Write_Default_Erroneous_Data_Reporting'            : b'\x5B',
    'HCI_Enhanced_Flush'                                    : b'\x5F',
    'HCI_Send_Keypress_Notification'                        : b'\x60',
    'HCI_Read_Logical_Link_Accept_Timeout'                  : b'\x61',
    'HCI_Write_Logical_Link_Accept_Timeout'                 : b'\x62',
    'HCI_Set_Event_Mask_Page_2'                             : b'\x63',
    'HCI_Read_Location_Data'                                : b'\x64',
    'HCI_Write_Location_Data'                               : b'\x65',
    'HCI_Read_Flow_Control_Mode'                            : b'\x66',
    'HCI_Write_Flow_Control_Mode'                           : b'\x67',
    'HCI_Read_Enhanced_Transmit_Power_Level'                : b'\x68',
    'HCI_Read_Best_Effort_Flush_Timeout'                    : b'\x69',
    'HCI_Write_Best_Effort_Flush_Timeout'                   : b'\x6A',
    'HCI_Short_Range_Mode'                                  : b'\x6B',
    'HCI_Read_LE_Host_Support'                              : b'\x6C',
    'HCI_Write_LE_Host_Support'                             : b'\x6D',
    'HCI_Set_MWS_Channel_Parameters'                        : b'\x6E',
    'HCI_Set_External_Frame_Configuration'                  : b'\x6F',
    'HCI_Set_MWS_Signaling'                                 : b'\x70',
    'HCI_Set_MWS_Transport_Layer'                           : b'\x71',
    'HCI_Set_MWS_Scan_Frequency_Table'                      : b'\x72',
    'HCI_Set_MWS_PATTERN_Configuration'                     : b'\x73',
    'HCI_Set_Reserved_LT_ADDR'                              : b'\x74',
    'HCI_Delete_Reserved_LT_ADDR'                           : b'\x75',
    'HCI_Set_Connectionless_Slave_Broadcast_Data'           : b'\x76',
    'HCI_Read_Synchronization_Train_Parameters'             : b'\x77',
    'HCI_Write_Synchronization_Train_Parameters'            : b'\x78',
    'HCI_Read_Secure_Connections_Host_Support'              : b'\x79',
    'HCI_Write_Secure_Connections_Host_Support'             : b'\x7A',
    'HCI_Read_Authenticated_Payload_Timeout'                : b'\x7B',
    'HCI_Write_Authenticated_Payload_Timeout'               : b'\x7C',
    'HCI_Read_Local_OOB_Extended_Data'                      : b'\x7D',
    'HCI_Read_Extended_Page_Timeout'                        : b'\x7E',
    'HCI_Write_Extended_Page_Timeout'                       : b'\x7F',
    'HCI_Read_Extended_Inquiry_Length'                      : b'\x80',
    'HCI_Write_Extended_Inquiry_Length'                     : b'\x81',
}

informational_command_set = {
    'HCI_Read_Local_Version_Information'                    : b'\x01',
    'HCI_Read_Local_Supported_Commands'                     : b'\x02',
    'HCI_Read_Local_Supported_Features'                     : b'\x03',
    'HCI_Read_Local_Extended_Features'                      : b'\x04',
    'HCI_Read_Buffer_Size'                                  : b'\x05',
    #'HCI Read Country Code'                                 : b'\x07',
    'HCI_Read_BD_ADDR'                                      : b'\x09',
    'HCI_Read_Data_Block_Size'                              : b'\x0A',
    'HCI_Read_Local_Supported_Codecs'                       : b'\x0B', 
}

status_command_set = {
    'HCI_Read_Failed_Contact_Counter'                       : b'\x01',
    'HCI_Reset_Failed_Contact_Counter'                      : b'\x02',
    'HCI_Read_Link_Quality'                                 : b'\x03',
    'HCI_Read_RSSI'                                         : b'\x05',
    'HCI_Read_AFH_Channel_Map'                              : b'\x06',
    'HCI_Read_Clock'                                        : b'\x07',
    'HCI_Read_Encryption_Key_Size'                          : b'\x08',
    'HCI_Read_Local_AMP_Info'                               : b'\x09',
    'HCI_Read_Local_AMP_ASSOC'                              : b'\x0A',
    'HCI_Write_Remote_AMP_ASSOC'                            : b'\x0B',
    'HCI_Get_MWS_Transport_Layer_Configuration'             : b'\x0C',
    'HCI_Set_Triggered_Clock_Capture'                       : b'\x0D',
}

test_command_set = {
    'HCI_Read_Loopback_Mode'                                : b'\x01',
    'HCI_Write_Loopback_Mode'                               : b'\x02',
    'HCI_Enable_Device_Under_Test_Mode'                     : b'\x03',
    'HCI_Write_Simple_Pairing_Debug_Mode'                   : b'\x04',
    'HCI_Enable_AMP_Receiver_Reports'                       : b'\x07',
    'HCI_AMP_Test_End'                                      : b'\x08',
    'HCI_AMP_Test'                                          : b'\x09',
    'HCI_Write_Secure_Connections_Test_Mode'                : b'\x0A',
}

le_command_set = {
    'HCI_LE_Set_Event_Mask'                                 : b'\x01',
    'HCI_LE_Read_Buffer_Size'                               : b'\x02',
    'HCI_LE_Read_Local_Supported_Features'                  : b'\x03',
    'HCI_LE_Set_Random_Address'                             : b'\x05',
    'HCI_LE_Set_Advertising_Parameters'                     : b'\x06',
    'HCI_LE_Read_Advertising_Channel_Tx_Power'              : b'\x07',
    'HCI_LE_Set_Advertising_Data'                           : b'\x08',
    'HCI_LE_Set_Scan_Response_Data'                         : b'\x09',
    'HCI_LE_Set_Advertising_Enable'                         : b'\x0A',
    'HCI_LE_Set_Scan_Parameters'                            : b'\x0B',
    'HCI_LE_Set_Scan_Enable'                                : b'\x0C',
    'HCI_LE_Create_Connection'                              : b'\x0D',
    'HCI_LE_Create_Connection_Cancel'                       : b'\x0E',
    'HCI_LE_Read_White_List_Size'                           : b'\x0F',
    'HCI_LE_Clear_White_List'                               : b'\x10',
    'HCI_LE_Add_Device_To_White_List'                       : b'\x11',
    'HCI_LE_Remove_Device_From_White_List'                  : b'\x12',
    'HCI_LE_Connection_Update'                              : b'\x13',
    'HCI_LE_Set_Host_Channel_Classification'                : b'\x14',
    'HCI_LE_Read_Channel_Map'                               : b'\x15',
    'HCI_LE_Read_Remote_Features'                           : b'\x16',
    'HCI_LE_Encrypt'                                        : b'\x17',
    'HCI_LE_Rand'                                           : b'\x18',
    'HCI_LE_Start_Encryption'                               : b'\x19',
    'HCI_LE_Long_Term_Key_Request_Reply'                    : b'\x1A',
    'HCI_LE_Long_Term_Key_Request_Negative_Reply'           : b'\x1B',
    'HCI_LE_Read_Supported_States'                          : b'\x1C',
    'HCI_LE_Receiver_Test'                                  : b'\x1D',
    'HCI_LE_Transmitter_Test'                               : b'\x1E',
    'HCI_LE_Test_End'                                       : b'\x1F',
    'LE_Remote_Connection_Parameter_Request_Reply'          : b'\x20',
    'LE_Remote_Connection_Parameter_Request_Negative_Reply' : b'\x21',
    'HCI_LE_Set_Data_Length'                                : b'\x22',
    'HCI_LE_Read_Suggested_Default_Data_Length'             : b'\x23',
    'HCI_LE_Write_Suggested_Default_Data_Length'            : b'\x24',
    'HCI_LE_Read_Local_P-256_Public_Key'                    : b'\x25',
    'HCI_LE_Generate_DHKey'                                 : b'\x26',
    'HCI_LE_Add_Device_To_Resolving_List'                   : b'\x27',
    'HCI_LE_Remove_Device_From_Resolving_List'              : b'\x28',
    'HCI_LE_Clear_Resolving_List'                           : b'\x29',
    'HCI_LE_Read_Resolving_List_Size'                       : b'\x2A',
    'HCI_LE_Read_Peer_Resolvable_Address'                   : b'\x2B',
    'HCI_LE_Read_Local_Resolvable_Address'                  : b'\x2C',
    'HCI_LE_Set_Address_Resolution_Enable'                  : b'\x2D',
    'HCI_LE_Set_Resolvable_Private_Address_Timeout'         : b'\x2E',
    'HCI_LE_Read_Maximum_Data_Length'                       : b'\x2F',
    'HCI_LE_Read_PHY'                                       : b'\x30',
    'HCI_LE_Set_Default_PHY'                                : b'\x31',
    'HCI_LE_Enhanced_Receiver_Test'                         : b'\x33',
    'HCI_LE_Enhanced_Transmitter_Test'                      : b'\x34',
    'HCI_LE_Set_Advertising_Set_Random_Address'             : b'\x35',
    'HCI_LE_Set_Extended_Advertising_Parameters'            : b'\x36',
    'HCI_LE_Set_Extended_Advertising_Data'                  : b'\x37',
    'HCI_LE_Set_Extended_Scan_Response_Data'                : b'\x38',
    'HCI_LE_Set_Extended_Advertising_Enable'                : b'\x39',
    'HCI_LE_Read_Maximum_Advertising_Data_Length'           : b'\x3A',
    'HCI_LE_Read_Number_of_Supported_Advertising_Sets'      : b'\x3B',
    'HCI_LE_Remove_Advertising_Set'                         : b'\x3C',
    'HCI_LE_Clear_Advertising_Sets'                         : b'\x3D',
    'HCI_LE_Set_Periodic_Advertising_Parameters'            : b'\x3E',
    'HCI_LE_Set_Periodic_Advertising_Data'                  : b'\x3F',
    'HCI_LE_Set_Periodic_Advertising_Enable'                : b'\x40',
    'HCI_LE_Set_Extended_Scan_Parameters'                   : b'\x41',
    'HCI_LE_Set_Extended_Scan_Enable'                       : b'\x42',
    'HCI_LE_Extended_Create_Connection'                     : b'\x43',
    'HCI_LE_Periodic_Advertising_Create_Sync'               : b'\x44',
    'HCI_LE_Periodic_Advertising_Create_Sync_Cancel'        : b'\x45',
    'HCI_LE_Periodic_Advertising_Terminate_Sync'            : b'\x46',
    'HCI_LE_Add_Device_To_Periodic_Advertiser_List'         : b'\x47',
    'HCI_LE_Remove_Device_From_Periodic_Advertiser_List'    : b'\x48',
    'HCI_LE_Clear_Periodic_Advertiser_List'                 : b'\x49',
    'HCI_LE_Read_Periodic_Advertiser_List_Size'             : b'\x4A',
    'HCI_LE_Read_Transmit_Power'                            : b'\x4B',
    'HCI_LE_Read_RF_Path_Compensation'                      : b'\x4C',
    'HCI_LE_Write_RF_Path_Compensation'                     : b'\x4D',
    'HCI_LE_Set_Privacy_Mode'                               : b'\x4E',
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


