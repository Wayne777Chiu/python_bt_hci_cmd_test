command_parameters_set = {
    #LINK CONTROL COMMANDS
    'HCI_Inquiry'                                       : ['LAP','Inquiry_Length','Num_Responses'],
    'HCI_Inquiry_Cancel'                                : [None],
    'HCI_Periodic_Inquiry_Mode'                         : ['Max_Period_Length','Min_Period_Length','LAP','Inquiry_Length','Num_Responses'],
    'HCI_Exit_Periodic_Inquiry_Mode'                    : [None],
    'HCI_Create_Connection'                             : ['BD_ADDR','Packet_Type','Page_Scan_Repetition_Mode','Reserved','Clock_Offset','Allow_Role_Switch'],
    'HCI_Disconnect'                                    : ['Connection_Handle','Reason'],
    #'HCI Add SCO Connection'                            : [''],
    'HCI_Create_Connection_Cancel'                      : ['BD_ADDR'],
    'HCI_Accept_Connection_Request'                     : ['BD_ADDR','Role'],
    'HCI_Reject_Connection_Request'                     : ['BD_ADDR','Reason'],
    'HCI_Link_Key_Request_Reply'                        : ['BD_ADDR','Link_Key'],
    'HCI_Link_Key_Request_Negative_Reply'               : ['BD_ADDR'],
    'HCI_PIN_Code_Request_Reply'                        : ['BD_ADDR','PIN_Code_Length','PIN_Code'],
    'HCI_PIN_Code_Request_Negative_Reply'               : ['BD_ADDR'],
    'HCI_Change_Connection_Packet_Type'                 : ['Connection_Handle','Packet_Type'],
    'HCI_Authentication_Requested'                      : ['Connection_Handle'],
    'HCI_Set_Connection_Encryption'                     : ['Connection_Handle','Encryption_Enable'],
    'HCI_Change_Connection_Link_Key'                    : ['Connection_Handle'],
    'HCI_Master_Link_Key'                               : ['Key_Flag'],
    'HCI_Remote_Name_Request'                           : ['BD_ADDR','Page_Scan_Repetition_Mode','Reserved','Clock_Offset'],
    'HCI_Remote_Name_Request_Cancel'                    : ['BD_ADDR'],
    'HCI_Read_Remote_Supported_Features'                : ['Connection_Handle'],
    'HCI_Read_Remote_Extended_Features'                 : ['Connection_Handle','Page Number'],
    'HCI_Read_Remote_Version_Information'               : ['Connection_Handle'],
    'HCI_Read_Clock_Offset'                             : ['Connection_Handle'],
    'HCI_Read_LMP_Handle'                               : ['Connection_Handle'],
    #'HCI Exchange Fixed Info'                           : [],
    #'HCI Exchange Alias Info'                           : [],
    #'HCI Private Pairing Request Reply'                 : [],
    #'HCI Private Pairing Request Negative Reply'        : [],
    #'HCI Generated Alias'                               : [],
    #'HCI Alias Address Request Reply'                   : [],
    #'HCI Alias Address Request Negative Reply'          : [],
    'HCI_Setup_Synchronous_Connection'                  : ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Max_Latency','Voice_Setting','Retransmission_Effort','Packet Type'],
    'HCI_Accept_Synchronous_Connection_Request'         : ['BD_ADDR','Transmit_Bandwidth','Receive_Bandwidth','Max_Latency','Voice_Setting','Retransmission_Effort','Packet Type'],
    'HCI_Reject_Synchronous_Connection_Request'         : ['BD_ADDR','Reason'],
    'HCI_IO_Capability_Request_Reply'                   : ['BD_ADDR','IO_Capability','OOB_Data_Present','Authentication_Requirements'],
    'HCI_User_Confirmation_Request_Reply'               : ['BD_ADDR'],
    'HCI_User_Confirmation_Request_Negative_Reply'      : ['BD_ADDR'],
    'HCI_User_Passkey_Request_Reply'                    : ['BD_ADDR','Numeric_Value'],
    'HCI_User_Passkey_Request_Negative_Reply'           : ['BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Reply'                 : ['BD_ADDR','C','R'],
    'HCI_Remote_OOB_Data_Request_Negative_Reply'        : ['BD_ADDR'],
    'HCI_IO_Capability_Request_Negative_Reply'          : ['BD_ADDR','Reason'],
    'HCI_Create_Physical_Link'                          : ['Physical_Link_Handle','Dedicated_AMP_Key_Length','Dedicated_AMP_Key_Type','Dedicated_AMP_Key'], #first
    'HCI_Accept_Physical_Link'                          : ['Physical_Link_Handle','Dedicated_AMP_Key_Length','Dedicated_AMP_Key_Type','Dedicated_AMP_Key'], #first
    'HCI_Disconnect_Physical_Link'                      : ['Physical_Link_Handle','Reason'],
    'HCI_Create_Logical_Link'                           : ['Physical_Link_Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Accept_Logical_Link'                           : ['Physical_Link_Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Disconnect_Logical_Link'                       : ['Physical_Link_Handle'],
    'HCI_Logical_Link_Cancel'                           : ['Physical_Link_Handle','Tx_Flow_Spec_ID'],
    'HCI_Flow_Spec_Modify'                              : ['Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Enhanced_Setup_Synchronous_Connection'         : ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Transmit_Coding_Format','Receive_Coding_Format','Transmit_Codec_Frame_Size','Receive_Codec_Frame_Size','Input_Bandwidth','Output_Bandwidth','Input_Coding_Format','Output_Coding_Format','Input_Coded_Data_Size','Output_Coded_Data_Size','Input_PCM_Data_Format','Output_PCM_Data_Format','Input_PCM_Sample_Payload_MSB_Position','Output_PCM_Sample_Payload_MSB_Position','Input_Data_Path','Output_Data_Path','Input_Transport_Unit_Size','Output_Transport_Unit_Size','Max_Latency','Packet_Type','Retransmission_Effort'],
    'HCI_Enhanced_Accept_Synchronous_Connection_Request': ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Transmit_Coding_Format','Receive_Coding_Format','Transmit_Codec_Frame_Size','Receive_Codec_Frame_Size','Input_Bandwidth','Output_Bandwidth','Input_Coding_Format','Output_Coding_Format','Input_Coded_Data_Size','Output_Coded_Data_Size','Input_PCM_Data_Format','Output_PCM_Data_Format','Input_PCM_Sample_Payload_MSB_Position','Output_PCM_Sample_Payload_MSB_Position','Input_Data_Path','Output_Data_Path','Input_Transport_Unit_Size','Output_Transport_Unit_Size','Max_Latency','Packet_Type','Retransmission_Effort'],
    'HCI_Truncated_Page'                                : ['BD_ADDR','Page_Scan_Repetition_Mode','Clock_Offset'],
    'HCI_Truncated_Page_Cancel'                         : ['BD_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast'            : ['Enable','LT_ADDR','LPO_Allowed','Packet_Type','Interval_Min','Interval_Max','CSB_supervisionTO'],
    'HCI_Set_Connectionless_Slave_Broadcast_Receive'    : ['Enable','BD_ADDR','LT_ADDR','Interval','Clock_Offset','Next_Connectionless_Slave_Broadcast_Clock','CSB_supervisionTO','Remote_Timing_Accuracy','Skip','Packet_Type','AFH_Channel_Map'],
    'HCI_Start_Synchronization_Train'                   : [None],
    'HCI_ Receive_Synchronization_Train'                : ['BD_ADDR','synchronization_scanTO','Sync_Scan_Window','Sync_Scan_Interval'],
    'HCI_Remote_OOB_Extended_Data_Request_Reply'        : ['BD_ADDR','C_192','R_192','C_256','R_256'],
    #LINK POLICY COMMANDS
    'HCI_Hold_Mode'                                     : ['Connection_Handle','Hold_Mode_Max_Interval','Hold_Mode_Min_Interval'],
    'HCI_Sniff_Mode'                                    : ['Connection_Handle','Sniff_Max_Interval','Sniff_Min_Interval','Sniff_Attempt','Sniff_Timeout'],
    'HCI_Exit_Sniff_Mode'                               : ['Connection_Handle'],
    #'HCI Park State'                                    : [],
    #'HCI Exit Park State'                               : [],
    'HCI_QoS_Setup'                                     : ['Connection_Handle','Flags','Service_Type','Token_Rate','Peak_Bandwidth','Latency','Delay_Variation'],
    'HCI_Role_Discovery'                                : ['Connection_Handle'],
    'HCI_Switch_Role'                                   : ['BD_ADDR','Role'],
    'HCI_Read_Link_Policy_Settings'                     : ['Connection_Handle'],
    'HCI_Write_Link_Policy_Settings'                    : ['Connection_Handle','Link_Policy_Settings'],
    'HCI_Read_Default_Link_Policy_Settings'             : [None],
    'HCI_Write_Default_Link_Policy_Settings'            : ['Default_Link_Policy_Settings'],
    'HCI_Flow_Specification'                            : ['Connection_Handle','Flags','Flow_direction','Service_Type','Token_Rate','Token_Bucket_Size','Peak_Bandwidth','Access Latency'],
    'HCI_Sniff_Subrating'                               : ['Connection_Handle','Maximum_Latency','Minimum_Remote_Timeout','Minimum_Local_Timeout'],
    #CONTROLLER & BASEBAND COMMANDS
    'HCI_Set_Event_Mask'                                : ['Evnet_Mask'],
    'HCI_Reset'                                         : [None],
    'HCI_Set_Event_Filter'                              : ['Filter_Type','Filter_Condition_Type','Condition'],
    'HCI_Flush'                                         : ['Connection_Handle'],
    'HCI_Read_PIN_Type'                                 : [None],
    'HCI_Write_PIN_Type'                                : ['PIN_Type'],
    'HCI_Create_New_Unit_Key'                           : [None],
    'HCI_Read_Stored_Link_Key'                          : ['BD_ADDR','Read_All_Flag'],
    'HCI_Write_Stored_Link_Key'                         : ['Num_Keys_To_Write','BD_ADDR_i','Link_Key_i'],
    'HCI_Delete_Stored_Link_Key'                        : ['BD_ADDR','Delete_All_Flag'],
    'HCI_Write_Local_Name'                              : ['Local Name'],
    'HCI_Read_Local_Name'                               : [None],
    'HCI_Read_Connection_Accept_Timeout'                : [None],
    'HCI_Write_Connection_Accept_Timeout'               : ['Conn_Accept_Timeout'],
    'HCI_Read_Page_Timeout'                             : [None],
    'HCI_Write_Page_Timeout'                            : ['Page_Timeout'],
    'HCI_Read_Scan_Enable'                              : [None],
    'HCI_Write_Scan_Enable'                             : ['Scan_Enable'],
    'HCI_Read_Page_Scan_Activity'                       : [None],
    'HCI_Write_Page_Scan_Activity'                      : ['Page_Scan_Interval','Page_Scan_Window'],
    'HCI_Read_Inquiry_Scan_Activity'                    : [None],
    'HCI_Write_Inquiry_Scan_Activity'                   : ['Inquiry_Scan_Interval','Inquiry_Scan_Window'],
    'HCI_Read_Authentication_Enable'                    : [None],
    'HCI_Write_Authentication_Enable'                   : ['Authentication_Enable'],
    #'HCI Read Encryption Mode'                          : [],
    #'HCI Write Encryption Mode'                         : [],
    'HCI_Read_Class_of_Device'                          : [None],
    'HCI_Write_Class_of_Device'                         : ['Class_of_Device'],
    'HCI_Read_Voice_Setting'                            : [None],
    'HCI_Write_Voice_Setting'                           : ['Voice_Setting'],
    'HCI_Read_Automatic_Flush_Timeout'                  : ['Connection_Handle'],
    'HCI_Write_Automatic_Flush_Timeout'                 : ['Connection_Handle','Flush_Tomeout'],
    'HCI_Read_Num_Broadcast_Retransmissions'            : [None],
    'HCI_Write_Num_Broadcast_Retransmissions'           : ['Num_Broadcast_Retransmissions'],
    'HCI_Read_Hold_Mode_Activity'                       : [None],
    'HCI_Write_Hold_Mode_Activity'                      : ['Hold_Mode_Activity'],
    'HCI_Read_Transmit_Power_Level'                     : ['Connection_Handle','Type'],
    'HCI_Read_Synchronous_Flow_Control_Enable'          : [None],
    'HCI_Write_Synchronous_Flow_Control_Enable'         : ['Synchronous_Flow_Control_Enable'],
    'HCI_Set_Controller_To_Host_Flow_Control'           : ['Flow_Control_Enable'],
    'HCI_Host_Buffer_Size'                              : ['Host_ACL_Data_Packet_Length','Host_Synchronous_Data_Packet_Length','Host_Total_Num_ACL_Data_Packets','Host_Total_Num_Synchronous_Data_Packets'],
    'HCI_Host_Number_Of_Completed_Packets'              : ['Number_Of_Handles','Connection_Handle_i','Host_Num_Of_Completed_Packets_i'],
    'HCI_Read_Link_Supervision_Timeout'                 : ['Handle'],
    'HCI_Write_Link_Supervision_Timeout'                : ['Handle','Link_Supervision_Timeout'],
    'HCI_Read_Number_Of_Supported_IAC'                  : [None],
    'HCI_Read_Current_IAC_LAP'                          : [None],
    'HCI_Write_Current_IAC_LAP'                         : ['Num_Current_IAC','IAC_LAP_i'],
    #'HCI Read Page Scan Period Mode'                    : [],
    #'HCI Write Page Scan Period Mode'                   : [],
    #'HCI Read Page Scan Mode'                           : [],
    #'HCI Write Page Scan Mode'                          : [],
    'Set_AFH_Host_Channel_Classification'               : ['AFH_Host_Channel_Classification'],
    'HCI Read Inquiry Scan Type'                        : [],
    'HCI Write Inquiry Scan Type'                       : [],
    'HCI Read Inquiry Mode'                             : [],
    'HCI Write Inquiry Mode'                            : [],
    'HCI Read Page Scan Type'                           : [],
    'HCI Write Page Scan Type'                          : [],
    'HCI Read AFH Channel Assessment Mode'              : [],
    'HCI Write AFH Channel Assessment Mode'             : [],
    'HCI Read Anonymity Mode'                           : [],
    'HCI Write Anonymity Mode'                          : [],
    'HCI Read Alias Authentication Enable'              : [],
    'HCI Write Alias Authentication Enable'             : [],
    'HCI Read Anonymous Address Change Parameters'      : [],
    'HCI Write Anonymous Address Change Parameters'     : [],
    'HCI Reset Fixed Address Attempts Counter'          : [],
    'HCI Read Extended Inquiry Response'                : [],
    'HCI Write Extended Inquiry Response'               : [],
    'HCI Refresh Encryption Key'                        : [],
    'HCI Read SSP Mode'                                 : [],
    'HCI Write SSP Mode'                                : [],
    'HCI Read Local OOB Data Command'                   : [],
    'HCI Read Inquiry Response Transmit Power Level'    : [],
    'HCI Write Inquiry Transmit Power Level'            : [],
    'HCI Read Default Erroneous Data Reporting'         : [],
    'HCI Write Default Erroneous Data Reporting'        : [],
    'HCI Enhanced Flush Command'                        : [],
    'HCI Send KeyPress Notification Command'            : [],
    'HCI Read Enhanced Transmit Power Level'            : [],
    'HCI Read Local Version Information'                : [],
    'HCI Read Local Supported Commands'                 : [],
    'HCI Read Local Supported Features'                 : [],
    'HCI Read Local Extended Features'                  : [],
    'HCI Read Buffer Size'                              : [],
    'HCI Read Country Code'                             : [],
    'HCI Read BD_ADDR'                                  : [],
    'HCI Read Failed Contact Counter'                   : [],
    'HCI Reset Failed Contact Counter'                  : [],
    'HCI Read Link Quality'                             : [],
    'HCI Read RSSI'                                     : [],
    'HCI Read AFH Channel Map'                          : [],
    'HCI Read Clock'                                    : [],
    'HCI Read Encryption Key Size'                      : [],
    'HCI LE Set Event Mask'                             : [],                   
    'HCI LE Read Buffer Size'                           : [],                     
    'HCI LE Read Local Supported Features'              : [],                                  
    'HCI LE Set Random Address'                         : [],                       
    'HCI LE Set Advertising Parameters'                 : [],                               
    'HCI LE Read Advertising Channel Tx Power'          : [],                                      
    'HCI LE Set Advertising Data'                       : [],                         
    'HCI LE Set Scan Response Data '                    : [],                            
    'HCI LE Set Advertise Enable'                       : [],                         
    'HCI LE Set Scan Parameters'                        : [],                        
    'HCI LE Set Scan Enable'                            : [],                    
    'HCI LE Create Connection'                          : [],                      
    'HCI LE Create Connection Cancel'                   : [],                             
    'HCI LE Read White List Size'                       : [],                         
    'HCI LE Clear White List'                           : [],                     
    'HCI LE Add Device to White List'                   : [],                             
    'HCI LE Remove Device from White List'              : [],                                  
    'HCI LE Connection Update'                          : [],                      
    'HCI LE Set Host Channel Classification'            : [],                                    
    'HCI LE Read Channel Map'                           : [],                     
    'HCI LE Read Remote Used Features'                  : [],                              
    'HCI LE Encrypt'                                    : [],            
    'HCI LE Rand'                                       : [],         
    'HCI LE Start Encryption'                           : [],                     
    'HCI LE Long Term Key Request Reply'                : [],                                
    'HCI LE Long Term Key Request Negative Reply'       : [],                                         
    'HCI LE Read Supported States'                      : [],                          
    'HCI LE Receiver Test'                              : [],                  
    'HCI LE Transmitter Test'                           : [],                     
    'HCI LE Test End'                                   : [],  
    'SMP Configure Security'                            : [],               
    'SMP Initiate Security'                             : [],              
    'SMP PassKey Reply'                                 : [],          
    'SMP OOB Data Reply'                                : [],   
}

command_return_parameters_set = {
    'HCI_Inquiry'                                       : [None],
    'HCI_Inquiry_Cancel'                                : ['Status'],
    'HCI_Periodic_Inquiry_Mode'                         : ['Status'],
    'HCI_Exit_Periodic_Inquiry_Mode'                    : ['Status'],
    'HCI_Create_Connection'                             : [None],
    'HCI_Disconnect'                                    : [None],
    #'HCI Add SCO Connection'                            : [],
    'HCI_Create_Connection_Cancel'                      : ['Status','BD_ADDR'],
    'HCI_Accept_Connection_Request'                     : [None],
    'HCI_Reject_Connection_Request'                     : [None],
    'HCI_Link_Key_Request_Reply'                        : ['Status','BD_ADDR'],
    'HCI_Link_Key_Request_Negative_Reply'               : ['Status','BD_ADDR'],
    'HCI_PIN_Code_Request_Reply'                        : ['Status','BD_ADDR'],
    'HCI_PIN_Code_Request_Negative_Reply'               : ['Status','BD_ADDR'],
    'HCI_Change_Connection_Packet_Type'                 : [None],
    'HCI_Authentication_Requested'                      : [None],
    'HCI_Set_Connection_Encryption'                     : [None],
    'HCI_Change_Connection_Link_Key'                    : [None],
    'HCI_Master_Link_Key'                               : [None],
    'HCI_Remote_Name_Request'                           : [None],
    'HCI_Remote_Name_Request_Cancel'                    : ['Status','BD_ADDR'],
    'HCI_Read_Remote_Supported_Features'                : [None],
    'HCI_Read_Remote_Extended_Features'                 : [None],
    'HCI_Read_Remote_Version_Information'               : [None],
    'HCI_Read_Clock_Offset'                             : [None],
    'HCI_Read_LMP_Handle'                               : ['Status','Connection_Handle','LMP_Handle','Reserved'],
    'HCI Exchange Fixed Info'                           : [],
    'HCI Exchange Alias Info'                           : [],
    'HCI Private Pairing Request Reply'                 : [],
    'HCI Private Pairing Request Negative Reply'        : [],
    'HCI Generated Alias'                               : [],
    'HCI Alias Address Request Reply'                   : [],
    'HCI Alias Address Request Negative Reply'          : [],
    'HCI_Setup_Synchronous_Connection'                  : [None],
    'HCI_Accept_Synchronous_Connection_Request'         : [None],
    'HCI_Reject_Synchronous_Connection_Request'         : [None],
    'HCI_IO_Capability_Request_Reply'                   : ['Status','BD_ADDR'],
    'HCI_User_Confirmation_Request_Reply'               : ['Status','BD_ADDR'],
    'HCI_User_Confirmation_Request_Negative_Reply'      : ['Status','BD_ADDR'],
    'HCI_User_Passkey_Request_Reply'                    : ['Status','BD_ADDR'],
    'HCI_User_Passkey_Request_Negative_Reply'           : ['Status','BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Reply'                 : ['Status','BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Negative_Reply'        : ['Status','BD_ADDR'],
    'HCI_IO_Capability_Request_Negative_Reply'          : ['Status','BD_ADDR'],
    'HCI_Create_Physical_Link'                          : [None],
    'HCI_Accept_Physical_Link'                          : [None],
    'HCI_Disconnect_Physical_Link'                      : [None],
    'HCI_Create_Logical_Link'                           : [None],
    'HCI_Accept_Logical_Link'                           : [None],
    'HCI_Disconnect_Logical_Link'                       : [None],
    'HCI_Logical_Link_Cancel'                           : ['Status','Physical_Link_Handle','Tx_Flow_Spec_ID'],
    'HCI_Flow_Spec_Modify'                              : [None],
    'HCI_Enhanced_Setup_Synchronous_Connection'         : [None],
    'HCI_Enhanced_Accept_Synchronous_Connection_Request': [None],
    'HCI_Truncated_Page'                                : [None],
    'HCI_Truncated_Page_Cancel'                         : ['Status','BD_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast'            : ['Status','LT_ADDR','Interval'],
    'HCI_Set_Connectionless_Slave_Broadcast_Receive'    : ['Status','BD_ADDR','LT_ADDR'],
    'HCI_Start_Synchronization_Train'                   : [None],
    'HCI_ Receive_Synchronization_Train'                : [None],
    'HCI_Remote_OOB_Extended_Data_Request_Reply'        : ['Status','BD_ADDR'],
    #LINK POLICY COMMANDS
    'HCI_Hold_Mode'                                     : [None],
    'HCI_Sniff_Mode'                                    : [None],
    'HCI_Exit_Sniff_Mode'                               : [None],
    #'HCI Park State'                                    : [],
    #'HCI Exit Park State'                               : [],
    'HCI_QoS_Setup'                                     : [None],
    'HCI_Role_Discovery'                                : ['Status','Connection_Handle','Current_Role'],
    'HCI_Switch_Role'                                   : [None],
    'HCI_Read_Link_Policy_Settings'                     : ['Status','Connection_Handle','Link_Policy_Settings'],
    'HCI_Write_Link_Policy_Settings'                    : ['Status','Connection_Handle'],
    'HCI_Read_Default_Link_Policy_Settings'             : ['Status','Default_Link_Policy_Settings'],
    'HCI_Write_Default_Link_Policy_Settings'            : ['Status'],
    'HCI_Flow_Specification'                            : [None],
    'HCI_Sniff_Subrating'                               : ['Status','Connection_Handle'],
    #CONTROLLER & BASEBAND COMMANDS
    'HCI_Set_Event_Mask'                                : ['Status'],
    'HCI_Reset'                                         : ['Status'],
    'HCI_Set_Event_Filter'                              : ['Status'],
    'HCI_Flush'                                         : ['Status','Connection_Handle'],
    'HCI_Read_PIN_Type'                                 : ['Status','PIN_Type'],
    'HCI_Write_PIN_Type'                                : ['Status'],
    'HCI_Create_New_Unit_Key'                           : ['Status'],
    'HCI_Read_Stored_Link_Key'                          : ['Status','Max_Num_Keys','Num_Keys_Read'],
    'HCI_Write_Stored_Link_Key'                         : ['Status','Num_Keys_Written'],
    'HCI_Delete_Stored_Link_Key'                        : ['Status','Num_Keys_Deleted'],
    'HCI_Write_Local_Name'                              : ['Status'],
    'HCI_Read_Local_Name'                               : ['Status','Local_Name'],
    'HCI_Read_Connection_Accept_Timeout'                : ['Status','Conn_Accept_Timeout'],
    'HCI_Write_Connection_Accept_Timeout'               : ['Status'],
    'HCI_Read_Page_Timeout'                             : ['Status','Page_Timeout'],
    'HCI_Write_Page_Timeout'                            : ['Status'],
    'HCI_Read_Scan_Enable'                              : ['Status','Scan_Enable'],
    'HCI_Write_Scan_Enable'                             : ['Status'],
    'HCI_Read_Page_Scan_Activity'                       : ['Status','Page_Scan_Interval','Page_Scan_Window'],
    'HCI_Write_Page_Scan_Activity'                      : ['Status'],
    'HCI_Read_Inquiry_Scan_Activity'                    : ['Status','Inquiry_Scan_Interval','Inquiry_Scan_Window'],
    'HCI_Write_Inquiry_Scan_Activity'                   : ['Status'],
    'HCI_Read_Authentication_Enable'                    : ['Status','Authentication_Enable'],
    'HCI_Write_Authentication_Enable'                   : ['Status'],
    #'HCI Read Encryption Mode'                          : [],
    #'HCI Write Encryption Mode'                         : [],
    'HCI_Read_Class_of_Device'                          : ['Status','Class_of_Device'],
    'HCI_Write_Class_of_Device'                         : ['Status'],
    'HCI_Read_Voice_Setting'                            : ['Status','Voice_Setting'],
    'HCI_Write_Voice_Setting'                           : ['Status'],
    'HCI_Read_Automatic_Flush_Timeout'                  : ['Status','Connection_Handle','Flush_Tomeout'],
    'HCI_Write_Automatic_Flush_Timeout'                 : ['Status','Connection_Handle'],
    'HCI_Read_Num_Broadcast_Retransmissions'            : ['Status','Num_Broadcast_Retransmissions'],
    'HCI_Write_Num_Broadcast_Retransmissions'           : ['Status'],
    'HCI_Read_Hold_Mode_Activity'                       : ['Status','Hold_Mode_Activity'],
    'HCI_Write_Hold_Mode_Activity'                      : ['Status'],
    'HCI_Read_Transmit_Power_Level'                     : ['Status','Connection_Handle','Transmit_Power_Level'],
    'HCI_Read_Synchronous_Flow_Control_Enable'          : ['Status','Synchronous_Flow_Control_Enable'],
    'HCI_Write_Synchronous_Flow_Control_Enable'         : ['Status'],
    'HCI_Set_Controller_To_Host_Flow_Control'           : ['Status'],
    'HCI_Host_Buffer_Size'                              : ['Status'],
    'HCI_Host_Number_Of_Completed_Packets'              : [None],
    'HCI_Read_Link_Supervision_Timeout'                 : ['Status','Handle','Link_Supervision_Timeout'],
    'HCI_Write_Link_Supervision_Timeout'                : ['Status','Handle'],
    'HCI_Read_Number_Of_Supported_IAC'                  : ['Status','Num_Support_IAC'],
    'HCI_Read_Current_IAC_LAP'                          : ['Status','Num_Current_IAC','IAC_LAP_i'],
    'HCI_Write_Current_IAC_LAP'                         : ['Status'],
    #'HCI Read Page Scan Period Mode'                    : [],
    #'HCI Write Page Scan Period Mode'                   : [],
    #'HCI Read Page Scan Mode'                           : [],
    #'HCI Write Page Scan Mode'                          : [],
    'Set_AFH_Host_Channel_Classification'               : ['Status'],
    'HCI Read Inquiry Scan Type'                        : [],
    'HCI Write Inquiry Scan Type'                       : [],
    'HCI Read Inquiry Mode'                             : [],
    'HCI Write Inquiry Mode'                            : [],
    'HCI Read Page Scan Type'                           : [],
    'HCI Write Page Scan Type'                          : [],
    'HCI Read AFH Channel Assessment Mode'              : [],
    'HCI Write AFH Channel Assessment Mode'             : [],
    'HCI Read Anonymity Mode'                           : [],
    'HCI Write Anonymity Mode'                          : [],
    'HCI Read Alias Authentication Enable'              : [],
    'HCI Write Alias Authentication Enable'             : [],
    'HCI Read Anonymous Address Change Parameters'      : [],
    'HCI Write Anonymous Address Change Parameters'     : [],
    'HCI Reset Fixed Address Attempts Counter'          : [],
    'HCI Read Extended Inquiry Response'                : [],
    'HCI Write Extended Inquiry Response'               : [],
    'HCI Refresh Encryption Key'                        : [],
    'HCI Read SSP Mode'                                 : [],
    'HCI Write SSP Mode'                                : [],
    'HCI Read Local OOB Data Command'                   : [],
    'HCI Read Inquiry Response Transmit Power Level'    : [],
    'HCI Write Inquiry Transmit Power Level'            : [],
    'HCI Read Default Erroneous Data Reporting'         : [],
    'HCI Write Default Erroneous Data Reporting'        : [],
    'HCI Enhanced Flush Command'                        : [],
    'HCI Send KeyPress Notification Command'            : [],
    'HCI Read Enhanced Transmit Power Level'            : [],
    'HCI Read Local Version Information'                : [],
    'HCI Read Local Supported Commands'                 : [],
    'HCI Read Local Supported Features'                 : [],
    'HCI Read Local Extended Features'                  : [],
    'HCI Read Buffer Size'                              : [],
    'HCI Read Country Code'                             : [],
    'HCI Read BD_ADDR'                                  : [],
    'HCI Read Failed Contact Counter'                   : [],
    'HCI Reset Failed Contact Counter'                  : [],
    'HCI Read Link Quality'                             : [],
    'HCI Read RSSI'                                     : [],
    'HCI Read AFH Channel Map'                          : [],
    'HCI Read Clock'                                    : [],
    'HCI Read Encryption Key Size'                      : [],
    'HCI Read Failed Contact Counter'                   : [],
    'HCI Reset Failed Contact Counter'                  : [],
    'HCI Read Link Quality'                             : [],
    'HCI Read RSSI'                                     : [],
    'HCI Read AFH Channel Map'                          : [],
    'HCI Read Clock'                                    : [],
    'HCI Read Encryption Key Size'                      : [],
    'HCI LE Set Event Mask'                             : [],                   
    'HCI LE Read Buffer Size'                           : [],                     
    'HCI LE Read Local Supported Features'              : [],                                  
    'HCI LE Set Random Address'                         : [],                       
    'HCI LE Set Advertising Parameters'                 : [],                               
    'HCI LE Read Advertising Channel Tx Power'          : [],                                      
    'HCI LE Set Advertising Data'                       : [],                         
    'HCI LE Set Scan Response Data '                    : [],                            
    'HCI LE Set Advertise Enable'                       : [],                         
    'HCI LE Set Scan Parameters'                        : [],                        
    'HCI LE Set Scan Enable'                            : [],                    
    'HCI LE Create Connection'                          : [],                      
    'HCI LE Create Connection Cancel'                   : [],                             
    'HCI LE Read White List Size'                       : [],                         
    'HCI LE Clear White List'                           : [],                     
    'HCI LE Add Device to White List'                   : [],                             
    'HCI LE Remove Device from White List'              : [],                                  
    'HCI LE Connection Update'                          : [],                      
    'HCI LE Set Host Channel Classification'            : [],                                    
    'HCI LE Read Channel Map'                           : [],                     
    'HCI LE Read Remote Used Features'                  : [],                              
    'HCI LE Encrypt'                                    : [],            
    'HCI LE Rand'                                       : [],         
    'HCI LE Start Encryption'                           : [],                     
    'HCI LE Long Term Key Request Reply'                : [],                                
    'HCI LE Long Term Key Request Negative Reply'       : [],                                         
    'HCI LE Read Supported States'                      : [],                          
    'HCI LE Receiver Test'                              : [],                  
    'HCI LE Transmitter Test'                           : [],                     
    'HCI LE Test End'                                   : [],  
    'SMP Configure Security'                            : [],               
    'SMP Initiate Security'                             : [],              
    'SMP PassKey Reply'                                 : [],          
    'SMP OOB Data Reply'                                : [],  
}

command_parameter_length_set = (
[      #link_control_command
    3, #'HCI Inquiry'
    0, #'HCI Inquiry Cancel'                        
    5, #'HCI Periodic Inquiry Mode'                 
    0, #'HCI Exit Periodic Inquiry Mode'            
    6, #'HCI Create Connection'                     
    2, #'HCI Disconnect'                            
    2, #'HCI Add SCO Connection'                    
    1, #'HCI Create Connection Cancel'              
    2, #'HCI Accept Connection Request'             
    2, #'HCI Reject Connection Request'             
    2, #'HCI Link Key Request Reply'                
    1, #'HCI Link Key Request Negative Reply'       
    3, #'HCI PIN Code Request Reply'                
    1, #'HCI PIN Code Request Negative Reply'       
    2, #'HCI Change Connection Packet Type'         
    1, #'HCI Authentication Requested'              
    2, #'HCI Set Connection Encryption'             
    1, #'HCI Change Connection Link Key'            
    1, #'HCI Master Link Key'                       
    4, #'HCI Remote Name Request'                   
    1, #'HCI Remote Name Request Cancel'            
    1, #'HCI Read Remote Supported Features'        
    2, #'HCI Read Remote Extended Features'         
    1, #'HCI Read Remote Version Information'       
    1, #'HCI Read Clock Offset'                     
    1, #'HCI Read LMP Handle'                       
    1, #'HCI Exchange Fixed Info'                   
    2, #'HCI Exchange Alias Info'                   
    1, #'HCI Private Pairing Request Reply'         
    1, #'HCI Private Pairing Request Negative Reply'
    2, #'HCI Generated Alias'                       
    2, #'HCI Alias Address Request Reply'           
    1, #'HCI Alias Address Request Negative Reply'  
    7, #'HCI Setup Synchronous Connection'          
    7, #'HCI Accept Synchronous Connection Request' 
    2, #'HCI Reject Synchronous Connection Request' 
    4, #'HCI IO Capability Request Reply'           
    1, #'HCI User Confirmation Reqest Reply'        
    1, #'HCI User Confirmation Reqest Negative Reply'
    2, #'HCI User Passkey Request Reply'            
    1, #'HCI User Passkey Request Negative Reply'   
    3, #'HCI Remote OOB Data Request Reply'         
    1, #'HCI Remote OOB Data Request Negative Reply'
    2, #'HCI IO Capability Request Negative Reply'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
],
[
    3, #'HCI Hold Mode'                         
    5, #'HCI Sniff Mode'                        
    1, #'HCI Exit Sniff Mode'                   
    3, #'HCI Park State'                        
    1, #'HCI Exit Park State'                   
    7, #'HCI QoS Setup'                         
    1, #'HCI Role Discovery'                    
    2, #'HCI Switch Role'                       
    1, #'HCI Read Link Policy Settings'         
    2, #'HCI Write Link Policy Settings'        
    0, #'HCI Read Default Link Policy Settings' 
    1, #'HCI Write Default Link Policy Settings'
    8, #'HCI Flow Specification'                
    4, #'HCI Sniff Subrating'                   
],
[      #host_control_and_baseband_command
    1, #'HCI Set Event Mask'                           
    0, #'HCI Reset'                                    
    0, #'HCI Set Event Filter'                         
    1, #'HCI Flush'                                    
    0, #'HCI Read PIN Type'                            
    1, #'HCI Write PIN Type'                           
    0, #'HCI Create New Unit Key'                      
    2, #'HCI Read Stored Link Key'                     
    0, #'HCI Write Stored Link Key'                    
    2, #'HCI Delete Stored Link Key'                   
    1, #'HCI Write Local Name'                         
    0, #'HCI Read Local Name'                          
    0, #'HCI Read Connection Accept Timeout'           
    1, #'HCI Write Connection Accept Timeout'          
    0, #'HCI Read Page Timeout'                        
    1, #'HCI Write Page Timeout'                       
    0, #'HCI Read Scan Enable'                         
    1, #'HCI Write Scan Enable'                        
    0, #'HCI Read Page Scan Activity'                  
    2, #'HCI Write Page Scan Activity'                 
    0, #'HCI Read Inquiry Scan Activity'               
    2, #'HCI Write Inquiry Scan Activity'              
    0, #'HCI Read Authentication Enable'               
    1, #'HCI Write Authentication Enable'              
    0, #'HCI Read Encryption Mode'                     
    1, #'HCI Write Encryption Mode'                    
    0, #'HCI Read Class of Device'                     
    1, #'HCI Write Class of Device'                    
    0, #'HCI Read Voice Setting'                       
    1, #'HCI Write Voice Setting'                      
    1, #'HCI Read Automatic Flush Timeout'             
    2, #'HCI Write Automatic Flush Timeout'            
    0, #'HCI Read Num Broadcast Retransmissions'       
    1, #'HCI Write Num Broadcast Retransmissions'      
    0, #'HCI Read Hold Mode Activity'                  
    1, #'HCI Write Hold Mode Activity'                 
    2, #'HCI Read Transmit Power Level'                
    0, #'HCI Read Synchronous Flow Control Enable'     
    1, #'HCI Write Synchronous Flow Control Enable'    
    1, #'HCI Set Controller to Host Flow Control'      
    4, #'HCI Host Buffer Size'                         
    0, #'HCI Host Number Of Completed Packets'         
    1, #'HCI Read Link Supervision Timeout'            
    2, #'HCI Write Link Supervision Timeout'           
    0, #'HCI Read Number of Supported IAC'             
    0, #'HCI Read Current IAC LAP'                     
    0, #'HCI Write Current IAC LAP'                    
    0, #'HCI Read Page Scan Period Mode'               
    1, #'HCI Write Page Scan Period Mode'              
    0, #'HCI Read Page Scan Mode'                      
    1, #'HCI Write Page Scan Mode'                     
    1, #'HCI Set AFH Host Channel Classification'      
    0, #'HCI Read Inquiry Scan Type'                   
    1, #'HCI Write Inquiry Scan Type'                  
    0, #'HCI Read Inquiry Mode'                        
    1, #'HCI Write Inquiry Mode'                       
    0, #'HCI Read Page Scan Type'                      
    1, #'HCI Write Page Scan Type'                     
    0, #'HCI Read AFH Channel Assessment Mode'         
    1, #'HCI Write AFH Channel Assessment Mode'        
    0, #'HCI Read Anonymity Mode'                      
    1, #'HCI Write Anonymity Mode'                     
    0, #'HCI Read Alias Authentication Enable'         
    1, #'HCI Write Alias Authentication Enable'        
    0, #'HCI Read Anonymous Address Change Parameters' 
    2, #'HCI Write Anonymous Address Change Parameters'
    1, #'HCI Reset Fixed Address Attempts Counter'     
    0, #'HCI Read Extended Inquiry Response'           
    2, #'HCI Write Extended Inquiry Response'          
    1, #'HCI Refresh Encryption Key'                   
    0, #'HCI Read SSP Mode'                            
    1, #'HCI Write SSP Mode'                           
    0, #'HCI Read Local OOB Data Command'              
    0, #'HCI Read Inquiry Response Transmit Power Level'
    1, #'HCI Write Inquiry Transmit Power Level'       
    0, #'HCI Read Default Erroneous Data Reporting'    
    1, #'HCI Write Default Erroneous Data Reporting'   
    2, #'HCI Enhanced Flush Command'                   
    2, #'HCI Send KeyPress Notification Command'       
    2, #'HCI Read Enhanced Transmit Power Level'       
],
[      #informational_command
    0, #'HCI Read Local Version Information'
    0, #'HCI Read Local Supported Commands' 
    0, #'HCI Read Local Supported Features'
    1, #'HCI Read Local Extended Features'  
    0, #'HCI Read Buffer Size'              
    0, #'HCI Read Country Code'             
    0, #'HCI Read BD_ADDR'                  
],
[      #status_command
    1, #'HCI Read Failed Contact Counter' 
    1, #'HCI Reset Failed Contact Counter'
    1, #'HCI Read Link Quality'           
    1, #'HCI Read RSSI'                   
    1, #'HCI Read AFH Channel Map'        
    2, #'HCI Read Clock'                  
    1, #'HCI Read Encryption Key Size'    
],
[      #test_command
    0, #'HCI Read Loopback Mode'           
    1, #'HCI Write Loopback Mode'          
    0, #'HCI Enable Device Under Test Mode'
    1, #'HCI Write SSP Debug Mode'         
],
[      #le_command
    1, #'HCI LE Set Event Mask'                      
    0, #'HCI LE Read Buffer Size'                    
    0, #'HCI LE Read Local Supported Features'       
    1, #'HCI LE Set Random Address'                  
    8, #'HCI LE Set Advertising Parameters'          
    0, #'HCI LE Read Advertising Channel Tx Power'   
    2, #'HCI LE Set Advertising Data'                
    2, #'HCI LE Set Scan Response Data '             
    1, #'HCI LE Set Advertise Enable'                
    5, #'HCI LE Set Scan Parameters'                 
    2, #'HCI LE Set Scan Enable'                     
   12, #'HCI LE Create Connection'                   
    0, #'HCI LE Create Connection Cancel'            
    0, #'HCI LE Read White List Size'                
    0, #'HCI LE Clear White List'                    
    2, #'HCI LE Add Device to White List'            
    2, #'HCI LE Remove Device from White List'       
    7, #'HCI LE Connection Update'                   
    1, #'HCI LE Set Host Channel Classification'     
    0, #'HCI LE Read Channel Map'                    
    1, #'HCI LE Read Remote Used Features'           
    2, #'HCI LE Encrypt'                             
    0, #'HCI LE Rand'                                
    4, #'HCI LE Start Encryption'                    
    2, #'HCI LE Long Term Key Request Reply'         
    1, #'HCI LE Long Term Key Request Negative Reply'
    0, #'HCI LE Read Supported States'               
    1, #'HCI LE Receiver Test'                       
    3, #'HCI LE Transmitter Test'                    
    0, #'HCI LE Test End'                            
],
[      #smp_command
    7, #'SMP Configure Security'
    2, #'SMP Initiate Security' 
    2, #'SMP PassKey Reply'     
    2, #'SMP OOB Data Reply'    
],
[      #tci_command
    1, #'TCI Activate Remote DUT'                          
    1, #'TCI Control Remote DUT'                           
    1, #'TCI Increase Remote Power'                        
    1, #'TCI Write Local Hop Frequencies'                  
    1, #'TCI Read Local Hardware Version'                  
    1, #'TCI Decrease Remote Power'                        
    1, #'TCI Increase Local Volume'                        
    1, #'TCI Decrease Local Volume'                        
    1, #'TCI Write Local Native Clock'                     
    1, #'TCI Read Local Native Clock'                      
    1, #'TCI Read Local Relative Mips'                     
    1, #'TCI Type Approval Tester Control'                 
    1, #'TCI Increment Local Failed Attempts Counter'      
    1, #'TCI Clear Local Failed Attempts Counter'          
    1, #'TCI Read Local Default Packet Type'               
    1, #'TCI Write Local Default Packet Type'              
    1, #'TCI Write Local SyncWord'                         
    1, #'TCI Write Local Hopping Mode'                     
    1, #'TCI Read Local Hopping Mode'                      
    1, #'TCI Write Local Whitening Enable'                 
    1, #'TCI Read Local Whitening Enable'                  
    1, #'TCI Write Local Radio Power'                      
    1, #'TCI Read Local Radio Power'                       
    1, #'TCI Write Local Am Addr'                          
    1, #'TCI Write Local Device Address'                   
    1, #'TCI Write Local Link Key Type'                    
    1, #'TCI Read Local Link Key Type'                     
    1, #'TCI Read Local Extended Features'                 
    1, #'TCI Write Local Features'                         
    1, #'TCI Write Local Extended Features'                
    1, #'TCI Read Local Timing Information'                
    1, #'TCI Write Local Timing Information'               
    1, #'TCI Read Remote Timing Information'               
    1, #'TCI Write Local Hardware Register'                
    1, #'TCI Reset Local Baseband Monitors'                
    1, #'TCI Update Manufacturing Information'             
    1, #'TCI Write Local Radio Register'                   
    1, #'TCI Read Local Radio Register'                    
    1, #'TCI Change Radio Modulation'                      
    1, #'TCI Read Radio Modulation'                        
    1, #'TCI Write UART Baud Rate'                         
    1, #'TCI Reset Local Pump Monitors'                    
    1, #'TCI Read Local Pump Monitors'                     
    1, #'TCI Write Local Encryption Key Length'            
    1, #'TCI Read Local Encryption Key Length'             
    1, #'TCI Read Local Hop Frequencies'                   
    1, #'TCI Read Local Baseband Monitors'                 
    1, #'TCI Disable Low Power Mode'                       
    1, #'TCI Enable Low Power Mode'                        
    1, #'TCI Read Minimum Search Window'                   
    1, #'TCI Write Minimum Search Window'                  
    1, #'TCI Disable SCO/eSCO Via HCI'                     
    1, #'TCI Enable SCO/eSCO Via HCI'                      
    1, #'TCI Write eSCO Retransmission Mode'               
    1, #'TCI Read eSCO Retransmission Mode'                
    1, #'TCI Write Enhanced Power Control Mode'            
    1, #'TCI Write PTA Mode'                               
    1, #'TCI Write Park Parameters'                        
    1, #'TCI Read Unused Stack Size'                       
    1, #'TCI Write AFH Control'                            
    1, #'TCI Read Raw RSSI'                                
    1, #'TCI Read BER'                                     
    1, #'TCI Read PER'                                     
    1, #'TCI Read Raw RSSI PER BER'                        
    1, #'TCI Override ARQN With NAK'                       
    1, #'TCI LE Set Transmit Window Params'                
    1, #'TCI LE Set Direct Advertising Timeout'            
    1, #'TCI LE Set TIFS Tx Adjustment'                    
    1, #'TCI LE Set Search Window Delay'                   
    1, #'TCI LE Auto Advertising After Disconnect Of Slave'
    1, #'TCI LE Auto Initiate After Disconnect Of Master'  
    1, #'TCI LE Read Advertising Parameters'               
    1, #'TCI LE Write Advertising Delta'                   
    1, #'TCI LE Write Num Packets Per CE'                  
    1, #'TCI LE Echo Transmit Window Size and Offset'      
    1, #'TCI LE Get Device States'                         
    1, #'TCI LE Read Scan Backoff Info'                    
    1, #'TCI LE Write Scan Frequencies'                    
    1, #'TCI LE Read Scan Frequencies'                     
    1, #'TCI LE Write Initiating Frequencies'              
    1, #'TCI LE Read Initiating Frequencies'               
    1, #'TCI LE Num Times Master Doesnt Tx In 1st Win'     
    1, #'TCI LE Slave Listen Outside Latency'              
    1, #'TCI LE Read Peer SCA'                             
    1, #'TCI LE Read Session Key'                          
    1, #'TCI LE Read Hop Increment'                        
    1, #'TCI LE Read Access Address'                       
    1, #'TCI LE Whitening'                                 
    1, #'TCI LE Scan Backoff Control'                      
    1, #'TCI LE PreConfigure Hop Increment'                
    1, #'TCI LE PreConfigure Access Address'               
    1, #'TCI LE Direct Advertising Timeout'                
    1, #'TCI LE Read Scan Parameters'                      
    1, #'TCI LE Set Trace Level'                           
])      