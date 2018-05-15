command_parameters_set = {
    #LINK CONTROL COMMANDS                                           
    'HCI_Inquiry'                                           : ['LAP','Inquiry_Length','Num_Responses'],
    'HCI_Inquiry_Cancel'                                    : [None],
    'HCI_Periodic_Inquiry_Mode'                             : ['Max_Period_Length','Min_Period_Length','LAP','Inquiry_Length','Num_Responses'],
    'HCI_Exit_Periodic_Inquiry_Mode'                        : [None],
    'HCI_Create_Connection'                                 : ['BD_ADDR','Packet_Type','Page_Scan_Repetition_Mode','Reserved','Clock_Offset','Allow_Role_Switch'],
    'HCI_Disconnect'                                        : ['Connection_Handle','Reason'],
    #'HCI Add SCO Connection'                                : ['Connection_Handle','Packet_Type'],    #DEPRECATED \x07
    'HCI_Create_Connection_Cancel'                          : ['BD_ADDR'],
    'HCI_Accept_Connection_Request'                         : ['BD_ADDR','Role'],
    'HCI_Reject_Connection_Request'                         : ['BD_ADDR','Reason'],
    'HCI_Link_Key_Request_Reply'                            : ['BD_ADDR','Link_Key'],
    'HCI_Link_Key_Request_Negative_Reply'                   : ['BD_ADDR'],
    'HCI_PIN_Code_Request_Reply'                            : ['BD_ADDR','PIN_Code_Length','PIN_Code'],
    'HCI_PIN_Code_Request_Negative_Reply'                   : ['BD_ADDR'],
    'HCI_Change_Connection_Packet_Type'                     : ['Connection_Handle','Packet_Type'],
    'HCI_Authentication_Requested'                          : ['Connection_Handle'],
    'HCI_Set_Connection_Encryption'                         : ['Connection_Handle','Encryption_Enable'],
    'HCI_Change_Connection_Link_Key'                        : ['Connection_Handle'],
    'HCI_Master_Link_Key'                                   : ['Key_Flag'],
    'HCI_Remote_Name_Request'                               : ['BD_ADDR','Page_Scan_Repetition_Mode','Reserved','Clock_Offset'],
    'HCI_Remote_Name_Request_Cancel'                        : ['BD_ADDR'],
    'HCI_Read_Remote_Supported_Features'                    : ['Connection_Handle'],
    'HCI_Read_Remote_Extended_Features'                     : ['Connection_Handle','Page_Number'],
    'HCI_Read_Remote_Version_Information'                   : ['Connection_Handle'],
    'HCI_Read_Clock_Offset'                                 : ['Connection_Handle'],
    'HCI_Read_LMP_Handle'                                   : ['Connection_Handle'],
    #'HCI Exchange Fixed Info'                               : [],
    #'HCI Exchange Alias Info'                               : [],
    #'HCI Private Pairing Request Reply'                     : [],
    #'HCI Private Pairing Request Negative Reply'            : [],
    #'HCI Generated Alias'                                   : [],
    #'HCI Alias Address Request Reply'                       : [],
    #'HCI Alias Address Request Negative Reply'              : [],
    'HCI_Setup_Synchronous_Connection'                      : ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Max_Latency','Voice_Setting','Retransmission_Effort','Packet_Type'],
    'HCI_Accept_Synchronous_Connection_Request'             : ['BD_ADDR','Transmit_Bandwidth','Receive_Bandwidth','Max_Latency','Voice_Setting','Retransmission_Effort','Packet_Type'],
    'HCI_Reject_Synchronous_Connection_Request'             : ['BD_ADDR','Reason'],
    'HCI_IO_Capability_Request_Reply'                       : ['BD_ADDR','IO_Capability','OOB_Data_Present','Authentication_Requirements'],
    'HCI_User_Confirmation_Request_Reply'                   : ['BD_ADDR'],
    'HCI_User_Confirmation_Request_Negative_Reply'          : ['BD_ADDR'],
    'HCI_User_Passkey_Request_Reply'                        : ['BD_ADDR','Numeric_Value'],
    'HCI_User_Passkey_Request_Negative_Reply'               : ['BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Reply'                     : ['BD_ADDR','C','R'],
    'HCI_Remote_OOB_Data_Request_Negative_Reply'            : ['BD_ADDR'],
    'HCI_IO_Capability_Request_Negative_Reply'              : ['BD_ADDR','Reason'],
    'HCI_Create_Physical_Link'                              : ['Physical_Link_Handle','Dedicated_AMP_Key_Length','Dedicated_AMP_Key_Type','Dedicated_AMP_Key'], #first
    'HCI_Accept_Physical_Link'                              : ['Physical_Link_Handle','Dedicated_AMP_Key_Length','Dedicated_AMP_Key_Type','Dedicated_AMP_Key'], #first
    'HCI_Disconnect_Physical_Link'                          : ['Physical_Link_Handle','Reason'],
    'HCI_Create_Logical_Link'                               : ['Physical_Link_Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Accept_Logical_Link'                               : ['Physical_Link_Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Disconnect_Logical_Link'                           : ['Physical_Link_Handle'],
    'HCI_Logical_Link_Cancel'                               : ['Physical_Link_Handle','Tx_Flow_Spec_ID'],
    'HCI_Flow_Spec_Modify'                                  : ['Handle','Tx_Flow_Spec','Rx_Flow_Spec'],
    'HCI_Enhanced_Setup_Synchronous_Connection'             : ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Transmit_Coding_Format','Receive_Coding_Format','Transmit_Codec_Frame_Size','Receive_Codec_Frame_Size','Input_Bandwidth','Output_Bandwidth','Input_Coding_Format','Output_Coding_Format','Input_Coded_Data_Size','Output_Coded_Data_Size','Input_PCM_Data_Format','Output_PCM_Data_Format','Input_PCM_Sample_Payload_MSB_Position','Output_PCM_Sample_Payload_MSB_Position','Input_Data_Path','Output_Data_Path','Input_Transport_Unit_Size','Output_Transport_Unit_Size','Max_Latency','Packet_Type','Retransmission_Effort'],
    'HCI_Enhanced_Accept_Synchronous_Connection_Request'    : ['Connection_Handle','Transmit_Bandwidth','Receive_Bandwidth','Transmit_Coding_Format','Receive_Coding_Format','Transmit_Codec_Frame_Size','Receive_Codec_Frame_Size','Input_Bandwidth','Output_Bandwidth','Input_Coding_Format','Output_Coding_Format','Input_Coded_Data_Size','Output_Coded_Data_Size','Input_PCM_Data_Format','Output_PCM_Data_Format','Input_PCM_Sample_Payload_MSB_Position','Output_PCM_Sample_Payload_MSB_Position','Input_Data_Path','Output_Data_Path','Input_Transport_Unit_Size','Output_Transport_Unit_Size','Max_Latency','Packet_Type','Retransmission_Effort'],
    'HCI_Truncated_Page'                                    : ['BD_ADDR','Page_Scan_Repetition_Mode','Clock_Offset'],
    'HCI_Truncated_Page_Cancel'                             : ['BD_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast'                : ['Enable','LT_ADDR','LPO_Allowed','Packet_Type','Interval_Min','Interval_Max','CSB_supervisionTO'],
    'HCI_Set_Connectionless_Slave_Broadcast_Receive'        : ['Enable','BD_ADDR','LT_ADDR','Interval','Clock_Offset','Next_Connectionless_Slave_Broadcast_Clock','CSB_supervisionTO','Remote_Timing_Accuracy','Skip','Packet_Type','AFH_Channel_Map'],
    'HCI_Start_Synchronization_Train'                       : [None],
    'HCI_ Receive_Synchronization_Train'                    : ['BD_ADDR','synchronization_scanTO','Sync_Scan_Window','Sync_Scan_Interval'],
    'HCI_Remote_OOB_Extended_Data_Request_Reply'            : ['BD_ADDR','C_192','R_192','C_256','R_256'],
    #LINK POLICY COMMANDS                                        
    'HCI_Hold_Mode'                                         : ['Connection_Handle','Hold_Mode_Max_Interval','Hold_Mode_Min_Interval'],
    'HCI_Sniff_Mode'                                        : ['Connection_Handle','Sniff_Max_Interval','Sniff_Min_Interval','Sniff_Attempt','Sniff_Timeout'],
    'HCI_Exit_Sniff_Mode'                                   : ['Connection_Handle'],
    #'HCI Park State'                                        : [],
    #'HCI Exit Park State'                                   : [],
    'HCI_QoS_Setup'                                         : ['Connection_Handle','Flags','Service_Type','Token_Rate','Peak_Bandwidth','Latency','Delay_Variation'],
    'HCI_Role_Discovery'                                    : ['Connection_Handle'],
    'HCI_Switch_Role'                                       : ['BD_ADDR','Role'],
    'HCI_Read_Link_Policy_Settings'                         : ['Connection_Handle'],
    'HCI_Write_Link_Policy_Settings'                        : ['Connection_Handle','Link_Policy_Settings'],
    'HCI_Read_Default_Link_Policy_Settings'                 : [None],
    'HCI_Write_Default_Link_Policy_Settings'                : ['Default_Link_Policy_Settings'],
    'HCI_Flow_Specification'                                : ['Connection_Handle','Flags','Flow_direction','Service_Type','Token_Rate','Token_Bucket_Size','Peak_Bandwidth','Access Latency'],
    'HCI_Sniff_Subrating'                                   : ['Connection_Handle','Maximum_Latency','Minimum_Remote_Timeout','Minimum_Local_Timeout'],
    #CONTROLLER & BASEBAND COMMANDS                                
    'HCI_Set_Event_Mask'                                    : ['Event_Mask'],
    'HCI_Reset'                                             : [None],
    'HCI_Set_Event_Filter'                                  : ['Filter_Type','Filter_Condition_Type','Condition'],
    'HCI_Flush'                                             : ['Connection_Handle'],
    'HCI_Read_PIN_Type'                                     : [None],
    'HCI_Write_PIN_Type'                                    : ['PIN_Type'],
    'HCI_Create_New_Unit_Key'                               : [None],
    'HCI_Read_Stored_Link_Key'                              : ['BD_ADDR','Read_All_Flag'],
    'HCI_Write_Stored_Link_Key'                             : ['Num_Keys_To_Write','BD_ADDR_i','Link_Key_i'],
    'HCI_Delete_Stored_Link_Key'                            : ['BD_ADDR','Delete_All_Flag'],
    'HCI_Write_Local_Name'                                  : ['Local_Name'],
    'HCI_Read_Local_Name'                                   : [None],
    'HCI_Read_Connection_Accept_Timeout'                    : [None],
    'HCI_Write_Connection_Accept_Timeout'                   : ['Conn_Accept_Timeout'],
    'HCI_Read_Page_Timeout'                                 : [None],
    'HCI_Write_Page_Timeout'                                : ['Page_Timeout'],
    'HCI_Read_Scan_Enable'                                  : [None],
    'HCI_Write_Scan_Enable'                                 : ['Scan_Enable'],
    'HCI_Read_Page_Scan_Activity'                           : [None],
    'HCI_Write_Page_Scan_Activity'                          : ['Page_Scan_Interval','Page_Scan_Window'],
    'HCI_Read_Inquiry_Scan_Activity'                        : [None],
    'HCI_Write_Inquiry_Scan_Activity'                       : ['Inquiry_Scan_Interval','Inquiry_Scan_Window'],
    'HCI_Read_Authentication_Enable'                        : [None],
    'HCI_Write_Authentication_Enable'                       : ['Authentication_Enable'],
    #'HCI Read Encryption Mode'                              : [],
    #'HCI Write Encryption Mode'                             : [],
    'HCI_Read_Class_of_Device'                              : [None],
    'HCI_Write_Class_of_Device'                             : ['Class_of_Device'],
    'HCI_Read_Voice_Setting'                                : [None],
    'HCI_Write_Voice_Setting'                               : ['Voice_Setting'],
    'HCI_Read_Automatic_Flush_Timeout'                      : ['Connection_Handle'],
    'HCI_Write_Automatic_Flush_Timeout'                     : ['Connection_Handle','Flush_Timeout'],
    'HCI_Read_Num_Broadcast_Retransmissions'                : [None],
    'HCI_Write_Num_Broadcast_Retransmissions'               : ['Num_Broadcast_Retransmissions'],
    'HCI_Read_Hold_Mode_Activity'                           : [None],
    'HCI_Write_Hold_Mode_Activity'                          : ['Hold_Mode_Activity'],
    'HCI_Read_Transmit_Power_Level'                         : ['Connection_Handle','Type'],
    'HCI_Read_Synchronous_Flow_Control_Enable'              : [None],
    'HCI_Write_Synchronous_Flow_Control_Enable'             : ['Synchronous_Flow_Control_Enable'],
    'HCI_Set_Controller_To_Host_Flow_Control'               : ['Flow_Control_Enable'],
    'HCI_Host_Buffer_Size'                                  : ['Host_ACL_Data_Packet_Length','Host_Synchronous_Data_Packet_Length','Host_Total_Num_ACL_Data_Packets','Host_Total_Num_Synchronous_Data_Packets'],
    'HCI_Host_Number_Of_Completed_Packets'                  : ['Number_Of_Handles','Connection_Handle_i','Host_Num_Of_Completed_Packets_i'],
    'HCI_Read_Link_Supervision_Timeout'                     : ['Handle'],
    'HCI_Write_Link_Supervision_Timeout'                    : ['Handle','Link_Supervision_Timeout'],
    'HCI_Read_Number_Of_Supported_IAC'                      : [None],
    'HCI_Read_Current_IAC_LAP'                              : [None],
    'HCI_Write_Current_IAC_LAP'                             : ['Num_Current_IAC','IAC_LAP_i'],
    #'HCI_Read_Page_Scan_Period_Mode'                        : [None],
    #'HCI_Write_Page_Scan_Period_Mode'                       : ['Page_Scan_Period_Mode'],
    #'HCI_Read_Page_Scan_Mode'                               : [None],    #\x3D
    #'HCI_Write_Page_Scan_Mode'                              : ['Page_Scan_Mode'],
    'Set_AFH_Host_Channel_Classification'                   : ['AFH_Host_Channel_Classification'],  #7.3.46 \x3F
    'HCI_Read_Inquiry_Scan_Type'                            : [None],              #\x42 
    'HCI_Write_Inquiry_Scan_Type'                           : ['Scan_Type'],
    'HCI_Read_Inquiry_Mode'                                 : [None],              #\x44
    'HCI_Write_Inquiry_Mode'                                : ['Inquiry_Mode'],
    'HCI_Read_Page_Scan_Type'                               : [None],
    'HCI_Write_Page_Scan_Type'                              : ['Page_Scan_Type'],
    'Read_AFH_Channel_Assessment_Mode'                      : [None],
    'Write_AFH_Channel_Assessment_Mode'                     : ['AFH_Channel_Assessment_Mode'],
    #'HCI Read Anonymity Mode'                               : [],
    #'HCI Write Anonymity Mode'                              : [],
    #'HCI Read Alias Authentication Enable'                  : [],
    #'HCI Write Alias Authentication Enable'                 : [],
    #'HCI Read Anonymous Address Change Parameters'          : [],
    #'HCI Write Anonymous Address Change Parameters'         : [],
    #'HCI Reset Fixed Address Attempts Counter'              : [],
    'HCI_Read_Extended_Inquiry_Response'                    : [None], #\x51
    'HCI_Write_Extended_Inquiry_Response'                   : ['FEC_Required','Extended_Inquiry_Response'],
    'HCI_Refresh_Encryption_Key'                            : ['Connection_Handle'],     #\x53
    'HCI_Read_Simple_Pairing_Mode'                          : [None], #\x55
    'HCI_Write_Simple_Pairing_Mode'                         : ['Simple_Pairing_Mode'],
    'HCI_Read_Local_OOB_Data'                               : [None],
    'HCI_Read_Inquiry_Response_Transmit_Power_Level'        : [None],
    'HCI_Write_Inquiry_Transmit_Power_Level'                : ['TX_Power'],
    'HCI_Read_Default_Erroneous_Data_Reporting'             : [None],
    'HCI_Write_Default_Erroneous_Data_Reporting'            : ['Erroneous_Data_Reporting'],
    'HCI_Enhanced_Flush'                                    : ['Handle','Packet_Type'],
    'HCI_Send_Keypress_Notification'                        : ['BD_ADDR','Notification_Type'],
    'HCI_Read_Logical_Link_Accept_Timeout'                  : [None],  #\x61
    'HCI_Write_Logical_Link_Accept_Timeout'                 : ['Logical_Link_Accept_Timeout'],
    'HCI_Set_Event_Mask_Page_2'                             : ['Event_Mask_Page_2'],
    'HCI_Read_Location_Data'                                : [None],
    'HCI_Write_Location_Data'                               : ['Location_Domain_Aware','Location_Domain','Location_Domain_Options','Location_Options'],
    'HCI_Read_Flow_Control_Mode'                            : [None],
    'HCI_Write_Flow_Control_Mode'                           : ['Flow_Control_Mode'],
    'HCI_Read_Enhanced_Transmit_Power_Level'                : ['Connection_Handle','Type'],
    'HCI_Read_Best_Effort_Flush_Timeout'                    : ['Logical_Link_Handle'],
    'HCI_Write_Best_Effort_Flush_Timeout'                   : ['Logical_Link_Handle','Best_Effort_Flush_Timeout'],
    'HCI_Short_Range_Mode'                                  : ['Physical_Link_Handle','Short_Range_Mode'],
    'HCI_Read_LE_Host_Support'                              : [None],
    'HCI_Write_LE_Host_Support'                             : ['LE_Supported_Host','Simultaneous_LE_Host'],
    'HCI_Set_MWS_Channel_Parameters'                        : ['MWS_Channel_Enable','MWS_RX_Center_Frequency','MWS_TX_Center_Frequency','MWS_RX_Channel_Bandwidth','MWS_TX_Channel_Bandwidth','MWS_Channel_Type'],
    'HCI_Set_External_Frame_Configuration'                  : ['Ext_Frame_Duration','Ext_Frame_Sync_Assert_Offset','Ext_Frame_Sync_Assert_Jitter','Ext_Num_Periods','Period_Duration_i','Period_Type_i'],
    'HCI_Set_MWS_Signaling'                                 : ['MWS_RX_Assert_Offset','MWS_RX_Assert_Jitter','MWS_RX_Deassert_Offset','MWS_RX_Deassert_Jitter','MWS_TX_Assert_Offset','MWS_TX_Assert_Jitter','MWS_TX_Deassert_Offset','MWS_TX_Deassert_Jitter','MWS_Pattern_Assert_Offset','MWS_Pattern_Assert_Jitter','MWS_Inactivity_Duration_Assert_Offset','MWS_Inactivity_Duration_Assert_Jitter','MWS_Scan_Frequency_Assert_Offset','MWS_Scan_Frequency_Assert_Jitter','MWS_Priority_Assert_Offset_Request'],
    'HCI_Set_MWS_Transport_Layer'                           : ['Transport_Layer','To_MWS_Baud_Rate','From_MWS_Baud_Rate'],
    'HCI_Set_MWS_Scan_Frequency_Table'                      : ['Num_Scan_Frequencies','Scan_Frequency_Low_i','Scan_Frequency_High_i'],
    'HCI_Set_MWS_PATTERN_Configuration'                     : ['MWS_PATTERN_Index','MWS_PATTERN_NumIntervals','MWS_PATTERN_IntervalDuration_i','MWS_PATTERN_IntervalType_i'],
    'HCI_Set_Reserved_LT_ADDR'                              : ['LT_ADDR'],
    'HCI_Delete_Reserved_LT_ADDR'                           : ['LT_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast_Data'           : ['LT_ADDR','Fragment','Data_Length','Data'],
    'HCI_Read_Synchronization_Train_Parameters'             : [None],
    'HCI_Write_Synchronization_Train_Parameters'            : ['Interval_Min','Interval_Max','synchronization_trainTO','Service_Data'],
    'HCI_Read_Secure_Connections_Host_Support'              : [None],
    'HCI_Write_Secure_Connections_Host_Support'             : ['Secure_Connections_Host_Support'],
    'HCI_Read_Authenticated_Payload_Timeout'                : ['Connection_Handle'],
    'HCI_Write_Authenticated_Payload_Timeout'               : ['Connection_Handle','Authenticated_Payload_Timeout'],
    'HCI_Read_Local_OOB_Extended_Data'                      : [None],
    'HCI_Read_Extended_Page_Timeout'                        : [None],
    'HCI_Write_Extended_Page_Timeout'                       : ['Extended_Page_Timeout'],
    'HCI_Read_Extended_Inquiry_Length'                      : [None],
    'HCI_Write_Extended_Inquiry_Length'                     : ['Extended_Inquiry_Length'],
    #INFORMATIONAL PARAMETERS                                      
    'HCI_Read_Local_Version_Information'                    : [None],
    'HCI_Read_Local_Supported_Commands'                     : [None],
    'HCI_Read_Local_Supported_Features'                     : [None],
    'HCI_Read_Local_Extended_Features'                      : ['Page_Number'],
    'HCI_Read_Buffer_Size'                                  : [None],
    #'HCI Read Country Code'                                 : [None],    #DEPRECATED\x07
    'HCI_Read_BD_ADDR'                                      : [None],
    'HCI_Read_Data_Block_Size'                              : [None],
    'HCI_Read_Local_Supported_Codecs'                       : [None],
    #STATUS PARAMETERS                                                       
    'HCI_Read_Failed_Contact_Counter'                       : ['Handle'],
    'HCI_Reset_Failed_Contact_Counter'                      : ['Handle'],
    'HCI_Read_Link_Quality'                                 : ['Handle'],
    'HCI_Read_RSSI'                                         : ['Handle'],
    'HCI_Read_AFH_Channel_Map'                              : ['Connection_Handle'],
    'HCI_Read_Clock'                                        : ['Connection_Handle','Which_Clock'],
    'HCI_Read_Encryption_Key_Size'                          : ['Connection_Handle'],
    'HCI_Read_Local_AMP_Info'                               : [None],
    'HCI_Read_Local_AMP_ASSOC'                              : ['Physical_Link_Handle','Length_So_Far','Max_Remote_AMP_ASSOC_Length'],
    'HCI_Write_Remote_AMP_ASSOC'                            : ['Physical_Link_Handle','Length_So_Far','AMP_ASSOC_Remaining_Length','AMP_ASSOC_fragment'],
    'HCI_Get_MWS_Transport_Layer_Configuration'             : [None],
    'HCI_Set_Triggered_Clock_Capture'                       : ['Connection_Handle','Enable','Which_Clock','LPO_Allowed','Num_Clock_Captures_To_Filter'],
    #7.6 TESTING COMMANDS                                          
    'HCI_Read_Loopback_Mode'                                : [None],
    'HCI_Write_Loopback_Mode'                               : ['Loopback_Mode'],
    'HCI_Enable_Device_Under_Test_Mode'                     : [None],
    'HCI_Write_Simple_Pairing_Debug_Mode'                   : ['Simple_Pairing_Debug_Mode'],
    'HCI_Enable_AMP_Receiver_Reports'                       : ['Enable','Interval'],
    'HCI_AMP_Test_End'                                      : [None],
    'HCI_AMP_Test'                                          : ['Test_Parameters'],
    'HCI_Write_Secure_Connections_Test_Mode'                : ['Connection_Handle','DM1_ACL-U_Mode','eSCO_Loopback_Mode'],
    #7.8 LE CONTROLLER COMMANDS                                   
    'HCI_LE_Set_Event_Mask'                                 : ['LE_Event_Mask'],                   
    'HCI_LE_Read_Buffer_Size'                               : [None],                     
    'HCI_LE_Read_Local_Supported_Features'                  : [None],                                  
    'HCI_LE_Set_Random_Address'                             : ['Random_Address'],                       
    'HCI_LE_Set_Advertising_Parameters'                     : ['Advertising_Interval_Min','Advertising_Interval_Max','Advertising_Type','Own_Address_Type','Peer_Address_Type','Peer_Address','Advertising_Channel_Map','Advertising_Filter_Policy'],                               
    'HCI_LE_Read_Advertising_Channel_Tx_Power'              : [None],                                      
    'HCI_LE_Set_Advertising_Data'                           : ['Advertising_Data_Length','Advertising_Data'],                         
    'HCI_LE_Set_Scan_Response_Data'                         : ['Scan_Response_Data_Length','Scan_Response_Data'],                            
    'HCI_LE_Set_Advertising_Enable'                         : ['Advertising_Enable'],                         
    'HCI_LE_Set_Scan_Parameters'                            : ['LE_Scan_Type','LE_Scan_Interval','LE_Scan_Window','Own_Address_Type','Scanning_Filter_Policy'],
    'HCI_LE_Set_Scan_Enable'                                : ['LE_Scan_Enable','Filter_Duplicates'],                    
    'HCI_LE_Create_Connection'                              : ['LE_Scan_Interval','LE_Scan_Window','Initiator_Filter_Policy','Peer_Address_Type','Peer_Address','Own_Address_Type','Conn_Interval_Min','Conn_Interval_Max','Conn_Latency','Supervision_Timeout','Minimum_CE_Length','Maximum_CE_Length'], 
    'HCI_LE_Create_Connection_Cancel'                       : [None],                             
    'HCI_LE_Read_White_List_Size'                           : [None],                         
    'HCI_LE_Clear_White_List'                               : [None],                     
    'HCI_LE_Add_Device_To_White_List'                       : ['Address_Type','Address'],                             
    'HCI_LE_Remove_Device_From_White_List'                  : ['Address_Type','Address'],                                  
    'HCI_LE_Connection_Update'                              : ['Connection_Handle','Conn_Interval_Min','Conn_Interval_Max','Conn_Latency','Supervision_Timeout','Minimum_CE_Length','Maximum_CE_Length'],
    'HCI_LE_Set_Host_Channel_Classification'                : ['Channel_Map'],                                    
    'HCI_LE_Read_Channel_Map'                               : ['Connection_Handle'],                     
    'HCI_LE_Read_Remote_Features'                           : ['Connection_Handle'],                              
    'HCI_LE_Encrypt'                                        : ['Key','Plaintext_Data'],            
    'HCI_LE_Rand'                                           : [None],         
    'HCI_LE_Start_Encryption'                               : ['Connection_Handle','Random_Number','Encrypted_Diversifier','Long_Term_Key'],                     
    'HCI_LE_Long_Term_Key_Request_Reply'                    : ['Connection_Handle','Long_Term_Key'],                                
    'HCI_LE_Long_Term_Key_Request_Negative_Reply'           : ['Connection_Handle'],                                         
    'HCI_LE_Read_Supported_States'                          : [None],                          
    'HCI_LE_Receiver_Test'                                  : ['RX_Channel'],                  
    'HCI_LE_Transmitter_Test'                               : ['TX_Channel','Length_Of_Test_Data','Packet_Payload'],                     
    'HCI_LE_Test_End'                                       : [None],
    'LE_Remote_Connection_Parameter_Request_Reply'          : ['Connection_Handle','Interval_Min','Interval_Max','Latency','Timeout','Minimum_CE_Length','Maximum_CE_Length'],
    'LE_Remote_Connection_Parameter_Request_Negative_Reply' : ['Connection_Handle','Reason'],
    'HCI_LE_Set_Data_Length'                                : ['Connection_Handle','TxOctets','TxTime'],
    'HCI_LE_Read_Suggested_Default_Data_Length'             : [None],
    'HCI_LE_Write_Suggested_Default_Data_Length'            : ['SuggestedMaxTxOctets','SuggestedMaxTxTime'],
    'HCI_LE_Read_Local_P-256_Public_Key'                    : [None],
    'HCI_LE_Generate_DHKey'                                 : ['Remote_P-256_Public_Key'],
    'HCI_LE_Add_Device_To_Resolving_List'                   : ['Peer_Identity_Address_Type','Peer_Identity_Address','Peer_IRK','Local_IRK'],
    'HCI_LE_Remove_Device_From_Resolving_List'              : ['Peer_Identity_Address_Type','Peer_Identity_Address'],
    'HCI_LE_Clear_Resolving_List'                           : [None],
    'HCI_LE_Read_Resolving_List_Size'                       : [None],
    'HCI_LE_Read_Peer_Resolvable_Address'                   : ['Peer_Identity_Address_Type','Peer_Identity_Address'],
    'HCI_LE_Read_Local_Resolvable_Address'                  : ['Peer_Identity_Address_Type','Peer_Identity_Address'],
    'HCI_LE_Set_Address_Resolution_Enable'                  : ['Address_Resolution_Enable'],
    'HCI_LE_Set_Resolvable_Private_Address_Timeout'         : ['RPA_Timeout'],
    'HCI_LE_Read_Maximum_Data_Length'                       : [None],
    'HCI_LE_Read_PHY'                                       : ['Connection_Handle'],
    'HCI_LE_Set_Default_PHY'                                : ['ALL_PHYS','TX_PHYS','RX_PHYS'],
    'HCI_LE_Set_PHY'                                        : ['Connection_Handle','ALL_PHYS','TX_PHYS','RX_PHYS','PHY_options'],
    'HCI_LE_Enhanced_Receiver_Test'                         : ['RX_Channel','PHY','Modulation_Index'],
    'HCI_LE_Enhanced_Transmitter_Test'                      : ['TX_Channel','Length_Of_Test_Data','Packet_Payload','PHY'],
    'HCI_LE_Set_Advertising_Set_Random_Address'             : ['Advertising_Handle','Random_Address'],
    'HCI_LE_Set_Extended_Advertising_Parameters'            : ['Advertising_Handle','Advertising_Event_Properties','Primary_Advertising_Interval_Min','Primary_Advertising_Interval_Max','Primary_Advertising_Channel_Map','Own_Address_Type','Peer_Address_Type','Peer_Address','Advertising_Filter_Policy','Advertising_Tx_Power','Primary_Advertising_PHY','Secondary_Advertising_Max_Skip','Secondary_Advertising_PHY','Advertising_SID','Scan_Request_Notification_Enable'],
    'HCI_LE_Set_Extended_Advertising_Data'                  : ['Advertising_Handle','Operation','Fragment_Preference','Advertising_Data_Length','Advertising_Data'],
    'HCI_LE_Set_Extended_Scan_Response_Data'                : ['Advertising_Handle','Operation','Fragment_Preference','Scan_Response_Data_Length','Scan_Response_Data'],
    'HCI_LE_Set_Extended_Advertising_Enable'                : ['Enable','Number_of_Sets','Advertising_Handle_i','Duration_i','Max_Extended_Advertising_Events_i'],
    'HCI_LE_Read_Maximum_Advertising_Data_Length'           : [None],
    'HCI_LE_Read_Number_of_Supported_Advertising_Sets'      : [None],
    'HCI_LE_Remove_Advertising_Set'                         : ['Advertising_Handle'],
    'HCI_LE_Clear_Advertising_Sets'                         : [None],
    'HCI_LE_Set_Periodic_Advertising_Parameters'            : ['Advertising_Handle','Periodic_Advertising_Interval_Min','Periodic_Advertising_Interval_Max','Periodic_Advertising_Properties'],
    'HCI_LE_Set_Periodic_Advertising_Data'                  : ['Advertising_Handle','Operation','Advertising_Data_Length','Advertising_Data'],
    'HCI_LE_Set_Periodic_Advertising_Enable'                : ['Enable','Advertising_Handle'],
    'HCI_LE_Set_Extended_Scan_Parameters'                   : ['Own_Address_Type','Scanning_Filter_Policy','Scanning_PHYs','Scan_Type_i','Scan_Interval_i','Scan_Window_i'],
    'HCI_LE_Set_Extended_Scan_Enable'                       : ['Enable','Filter_Duplicates','Duration','Period'],
    'HCI_LE_Extended_Create_Connection'                     : ['Initiator_Filter_Policy','Own_Address_Type','Peer_Address_Type','Peer_Address','Initiating_PHYs','Scan_Interval_i','Scan_Window_i','Conn_Interval_Min_i','Conn_Interval_Max_i','Conn_Latency_i','Supervision_Timeout_i','Minimum_CE_Length_i','Maximum_CE_Length_i'],
    'HCI_LE_Periodic_Advertising_Create_Sync'               : ['Filter_Policy','Advertising_SID','Advertiser_Address_Type','Advertiser_Address','Skip','Sync_Timeout','Unused'],
    'HCI_LE_Periodic_Advertising_Create_Sync_Cancel'        : [None],
    'HCI_LE_Periodic_Advertising_Terminate_Sync'            : ['Sync_Handle'],
    'HCI_LE_Add_Device_To_Periodic_Advertiser_List'         : ['Advertiser_Address_Type','Advertiser_Address','Advertising_SID'],
    'HCI_LE_Remove_Device_From_Periodic_Advertiser_List'    : ['Advertiser_Address_Type','Advertiser_Address','Advertising_SID'],
    'HCI_LE_Clear_Periodic_Advertiser_List'                 : [None],
    'HCI_LE_Read_Periodic_Advertiser_List_Size'             : [None],
    'HCI_LE_Read_Transmit_Power'                            : [None],
    'HCI_LE_Read_RF_Path_Compensation'                      : [None],
    'HCI_LE_Write_RF_Path_Compensation'                     : ['RF_Tx_Path_Compensation_Value','RF_Rx_Path_Compensation_Value'],
    'HCI_LE_Set_Privacy_Mode'                               : ['Peer_Identity_Address_Type','Peer_Identity_Address','Privacy_Mode'],
    'SMP Configure Security'                                : ['Peer_Identity_Address_Type'],
    'SMP Initiate Security'                                 : [],              
    'SMP PassKey Reply'                                     : [],          
    'SMP OOB Data Reply'                                    : [],   
}

command_return_parameters_set = {
    #LINK CONTROL COMMANDS                                          
    'HCI_Inquiry'                                           : [None],
    'HCI_Inquiry_Cancel'                                    : ['Status'],
    'HCI_Periodic_Inquiry_Mode'                             : ['Status'],
    'HCI_Exit_Periodic_Inquiry_Mode'                        : ['Status'],
    'HCI_Create_Connection'                                 : [None],
    'HCI_Disconnect'                                        : [None],
    #'HCI Add SCO Connection'                                : [None],    #DEPRECATED \x07
    'HCI_Create_Connection_Cancel'                          : ['Status','BD_ADDR'],
    'HCI_Accept_Connection_Request'                         : [None],
    'HCI_Reject_Connection_Request'                         : [None],
    'HCI_Link_Key_Request_Reply'                            : ['Status','BD_ADDR'],
    'HCI_Link_Key_Request_Negative_Reply'                   : ['Status','BD_ADDR'],
    'HCI_PIN_Code_Request_Reply'                            : ['Status','BD_ADDR'],
    'HCI_PIN_Code_Request_Negative_Reply'                   : ['Status','BD_ADDR'],
    'HCI_Change_Connection_Packet_Type'                     : [None],
    'HCI_Authentication_Requested'                          : [None],
    'HCI_Set_Connection_Encryption'                         : [None],
    'HCI_Change_Connection_Link_Key'                        : [None],
    'HCI_Master_Link_Key'                                   : [None],
    'HCI_Remote_Name_Request'                               : [None],
    'HCI_Remote_Name_Request_Cancel'                        : ['Status','BD_ADDR'],
    'HCI_Read_Remote_Supported_Features'                    : [None],
    'HCI_Read_Remote_Extended_Features'                     : [None],
    'HCI_Read_Remote_Version_Information'                   : [None],
    'HCI_Read_Clock_Offset'                                 : [None],
    'HCI_Read_LMP_Handle'                                   : ['Status','Connection_Handle','LMP_Handle','Reserved'],
    'HCI Exchange Fixed Info'                               : [],
    'HCI Exchange Alias Info'                               : [],
    'HCI Private Pairing Request Reply'                     : [],
    'HCI Private Pairing Request Negative Reply'            : [],
    'HCI Generated Alias'                                   : [],
    'HCI Alias Address Request Reply'                       : [],
    'HCI Alias Address Request Negative Reply'              : [],
    'HCI_Setup_Synchronous_Connection'                      : [None],
    'HCI_Accept_Synchronous_Connection_Request'             : [None],
    'HCI_Reject_Synchronous_Connection_Request'             : [None],
    'HCI_IO_Capability_Request_Reply'                       : ['Status','BD_ADDR'],
    'HCI_User_Confirmation_Request_Reply'                   : ['Status','BD_ADDR'],
    'HCI_User_Confirmation_Request_Negative_Reply'          : ['Status','BD_ADDR'],
    'HCI_User_Passkey_Request_Reply'                        : ['Status','BD_ADDR'],
    'HCI_User_Passkey_Request_Negative_Reply'               : ['Status','BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Reply'                     : ['Status','BD_ADDR'],
    'HCI_Remote_OOB_Data_Request_Negative_Reply'            : ['Status','BD_ADDR'],
    'HCI_IO_Capability_Request_Negative_Reply'              : ['Status','BD_ADDR'],
    'HCI_Create_Physical_Link'                              : [None],
    'HCI_Accept_Physical_Link'                              : [None],
    'HCI_Disconnect_Physical_Link'                          : [None],
    'HCI_Create_Logical_Link'                               : [None],
    'HCI_Accept_Logical_Link'                               : [None],
    'HCI_Disconnect_Logical_Link'                           : [None],
    'HCI_Logical_Link_Cancel'                               : ['Status','Physical_Link_Handle','Tx_Flow_Spec_ID'],
    'HCI_Flow_Spec_Modify'                                  : [None],
    'HCI_Enhanced_Setup_Synchronous_Connection'             : [None],
    'HCI_Enhanced_Accept_Synchronous_Connection_Request'    : [None],
    'HCI_Truncated_Page'                                    : [None],
    'HCI_Truncated_Page_Cancel'                             : ['Status','BD_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast'                : ['Status','LT_ADDR','Interval'],
    'HCI_Set_Connectionless_Slave_Broadcast_Receive'        : ['Status','BD_ADDR','LT_ADDR'],
    'HCI_Start_Synchronization_Train'                       : [None],
    'HCI_ Receive_Synchronization_Train'                    : [None],
    'HCI_Remote_OOB_Extended_Data_Request_Reply'            : ['Status','BD_ADDR'],
    #LINK POLICY COMMANDS                                      
    'HCI_Hold_Mode'                                         : [None],
    'HCI_Sniff_Mode'                                        : [None],
    'HCI_Exit_Sniff_Mode'                                   : [None],
    #'HCI Park State'                                        : [],
    #'HCI Exit Park State'                                   : [],
    'HCI_QoS_Setup'                                         : [None],
    'HCI_Role_Discovery'                                    : ['Status','Connection_Handle','Current_Role'],
    'HCI_Switch_Role'                                       : [None],
    'HCI_Read_Link_Policy_Settings'                         : ['Status','Connection_Handle','Link_Policy_Settings'],
    'HCI_Write_Link_Policy_Settings'                        : ['Status','Connection_Handle'],
    'HCI_Read_Default_Link_Policy_Settings'                 : ['Status','Default_Link_Policy_Settings'],
    'HCI_Write_Default_Link_Policy_Settings'                : ['Status'],
    'HCI_Flow_Specification'                                : [None],
    'HCI_Sniff_Subrating'                                   : ['Status','Connection_Handle'],
    #CONTROLLER & BASEBAND COMMANDS                               
    'HCI_Set_Event_Mask'                                    : ['Status'],
    'HCI_Reset'                                             : ['Status'],
    'HCI_Set_Event_Filter'                                  : ['Status'],
    'HCI_Flush'                                             : ['Status','Connection_Handle'],
    'HCI_Read_PIN_Type'                                     : ['Status','PIN_Type'],
    'HCI_Write_PIN_Type'                                    : ['Status'],
    'HCI_Create_New_Unit_Key'                               : ['Status'],
    'HCI_Read_Stored_Link_Key'                              : ['Status','Max_Num_Keys','Num_Keys_Read'],
    'HCI_Write_Stored_Link_Key'                             : ['Status','Num_Keys_Written'],
    'HCI_Delete_Stored_Link_Key'                            : ['Status','Num_Keys_Deleted'],
    'HCI_Write_Local_Name'                                  : ['Status'],
    'HCI_Read_Local_Name'                                   : ['Status','Local_Name'],
    'HCI_Read_Connection_Accept_Timeout'                    : ['Status','Conn_Accept_Timeout'],
    'HCI_Write_Connection_Accept_Timeout'                   : ['Status'],
    'HCI_Read_Page_Timeout'                                 : ['Status','Page_Timeout'],
    'HCI_Write_Page_Timeout'                                : ['Status'],
    'HCI_Read_Scan_Enable'                                  : ['Status','Scan_Enable'],
    'HCI_Write_Scan_Enable'                                 : ['Status'],
    'HCI_Read_Page_Scan_Activity'                           : ['Status','Page_Scan_Interval','Page_Scan_Window'],
    'HCI_Write_Page_Scan_Activity'                          : ['Status'],
    'HCI_Read_Inquiry_Scan_Activity'                        : ['Status','Inquiry_Scan_Interval','Inquiry_Scan_Window'],
    'HCI_Write_Inquiry_Scan_Activity'                       : ['Status'],
    'HCI_Read_Authentication_Enable'                        : ['Status','Authentication_Enable'],
    'HCI_Write_Authentication_Enable'                       : ['Status'],
    #'HCI Read Encryption Mode'                              : [],
    #'HCI Write Encryption Mode'                             : [],
    'HCI_Read_Class_of_Device'                              : ['Status','Class_of_Device'],
    'HCI_Write_Class_of_Device'                             : ['Status'],
    'HCI_Read_Voice_Setting'                                : ['Status','Voice_Setting'],
    'HCI_Write_Voice_Setting'                               : ['Status'],
    'HCI_Read_Automatic_Flush_Timeout'                      : ['Status','Connection_Handle','Flush_Timeout'],
    'HCI_Write_Automatic_Flush_Timeout'                     : ['Status','Connection_Handle'],
    'HCI_Read_Num_Broadcast_Retransmissions'                : ['Status','Num_Broadcast_Retransmissions'],
    'HCI_Write_Num_Broadcast_Retransmissions'               : ['Status'],
    'HCI_Read_Hold_Mode_Activity'                           : ['Status','Hold_Mode_Activity'],
    'HCI_Write_Hold_Mode_Activity'                          : ['Status'],
    'HCI_Read_Transmit_Power_Level'                         : ['Status','Connection_Handle','Transmit_Power_Level'],
    'HCI_Read_Synchronous_Flow_Control_Enable'              : ['Status','Synchronous_Flow_Control_Enable'],
    'HCI_Write_Synchronous_Flow_Control_Enable'             : ['Status'],
    'HCI_Set_Controller_To_Host_Flow_Control'               : ['Status'],
    'HCI_Host_Buffer_Size'                                  : ['Status'],
    'HCI_Host_Number_Of_Completed_Packets'                  : [None],
    'HCI_Read_Link_Supervision_Timeout'                     : ['Status','Handle','Link_Supervision_Timeout'],
    'HCI_Write_Link_Supervision_Timeout'                    : ['Status','Handle'],
    'HCI_Read_Number_Of_Supported_IAC'                      : ['Status','Num_Support_IAC'],
    'HCI_Read_Current_IAC_LAP'                              : ['Status','Num_Current_IAC','IAC_LAP_i'],
    'HCI_Write_Current_IAC_LAP'                             : ['Status'],     #\x3A
    #'HCI_Read_Page_Scan_Period_Mode'                        : ['Status','Page_Scan_Period_Mode'],
    #'HCI_Write_Page_Scan_Period_Mode'                       : ['Status'],
    #'HCI_Read_Page_Scan_Mode'                               : ['Status','Page_Scan_Mode'],    #\x3D
    #'HCI_Write_Page_Scan_Mode'                              : ['Status'],
    'Set_AFH_Host_Channel_Classification'                   : ['Status'],
    'HCI_Read_Inquiry_Scan_Type'                            : ['Status','Inquiry_Scan_Type'],
    'HCI_Write_Inquiry_Scan_Type'                           : ['Status'],
    'HCI_Read_Inquiry_Mode'                                 : ['Status','Inquiry_Mode'],
    'HCI_Write_Inquiry_Mode'                                : ['Status'],
    'HCI_Read_Page_Scan_Type'                               : ['Status','Page_Scan_Type'],
    'HCI_Write_Page_Scan_Type'                              : ['Status'],
    'Read_AFH_Channel_Assessment_Mode'                      : ['Status','AFH_Channel_Assessment_Mode'],
    'Write_AFH_Channel_Assessment_Mode'                     : ['Status'],
    #'HCI Read Anonymity Mode'                               : [],
    #'HCI Write Anonymity Mode'                              : [],
    #'HCI Read Alias Authentication Enable'                  : [],
    #'HCI Write Alias Authentication Enable'                 : [],
    #'HCI Read Anonymous Address Change Parameters'          : [],
    #'HCI Write Anonymous Address Change Parameters'         : [],
    #'HCI Reset Fixed Address Attempts Counter'              : [],
    'HCI_Read_Extended_Inquiry_Response'                    : ['Status','FEC_Required','Extended_Inquiry_Response'],
    'HCI_Write_Extended_Inquiry_Response'                   : ['Status'],
    'HCI_Refresh_Encryption_Key'                            : [None],
    'HCI_Read_Simple_Pairing_Mode'                          : ['Status','Simple_Pairing_Mode'],
    'HCI_Write_Simple_Pairing_Mode'                         : ['Status'],
    'HCI_Read_Local_OOB_Data'                               : ['Status','C','R'],
    'HCI_Read_Inquiry_Response_Transmit_Power_Level'        : ['Status','TX_Power'],
    'HCI_Write_Inquiry_Transmit_Power_Level'                : ['Status'],
    'HCI_Read_Default_Erroneous_Data_Reporting'             : ['Status','Erroneous_Data_Reporting'],
    'HCI_Write_Default_Erroneous_Data_Reporting'            : ['Status'],
    'HCI_Enhanced_Flush'                                    : [None],
    'HCI_Send_Keypress_Notification'                        : ['Status','BD_ADDR'],
    'HCI_Read_Logical_Link_Accept_Timeout'                  : ['Status','Logical_Link_Accept_Timeout'],  #\x61
    'HCI_Write_Logical_Link_Accept_Timeout'                 : ['Status'],
    'HCI_Set_Event_Mask_Page_2'                             : ['Status'],
    'HCI_Read_Location_Data'                                : ['Status','Location_Domain_Aware','Location_Domain','Location_Domain_Options','Location_Options'],
    'HCI_Write_Location_Data'                               : ['Status'],
    'HCI_Read_Flow_Control_Mode'                            : ['Status','Flow_Control_Mode'],
    'HCI_Write_Flow_Control_Mode'                           : ['Status'],
    'HCI_Read_Enhanced_Transmit_Power_Level'                : ['Status','Connection_Handle','Transmit_Power_Level_GFSK','Transmit_Power_Level_DQPSK','Transmit_Power_Level_8DPSK'],
    'HCI_Read_Best_Effort_Flush_Timeout'                    : ['Status','Best_Effort_Flush_Timeout'],
    'HCI_Write_Best_Effort_Flush_Timeout'                   : ['Status'],
    'HCI_Short_Range_Mode'                                  : [None],
    'HCI_Read_LE_Host_Support'                              : ['Status','LE_Supported_Host','Simultaneous_LE_Host'],
    'HCI_Write_LE_Host_Support'                             : ['Status'],
    'HCI_Set_MWS_Channel_Parameters'                        : ['Status'],
    'HCI_Set_External_Frame_Configuration'                  : ['Status'],
    'HCI_Set_MWS_Signaling'                                 : ['Status','Bluetooth_Rx_Priority_Assert_Offset','Bluetooth_Rx_Priority_Assert_Jitter','Bluetooth_Rx_Priority_Deassert_Offset','Bluetooth_Rx_Priority_Deassert_Jitter','802_Rx_Priority_Assert_Offset','802_Rx_Priority_Assert_Jitter','802_Rx_Priority_Deassert_Offset','802_Rx_Priority_Deassert_Jitter','Bluetooth_Tx_On_Assert_Offset','Bluetooth_Tx_On_Assert_Jitter','Bluetooth_Tx_On_Deassert_Offset','Bluetooth_Tx_On_Deassert_Jitter','802_Tx_On_Assert_Offset','802_Tx_On_Assert_Jitter','802_Tx_On_Deassert_Offset','802_Tx_On_Deassert_Jitter'],
    'HCI_Set_MWS_Transport_Layer'                           : ['Status'],
    'HCI_Set_MWS_Scan_Frequency_Table'                      : ['Status'],
    'HCI_Set_MWS_PATTERN_Configuration'                     : ['Status'],
    'HCI_Set_Reserved_LT_ADDR'                              : ['Status','LT_ADDR'],
    'HCI_Delete_Reserved_LT_ADDR'                           : ['Status','LT_ADDR'],
    'HCI_Set_Connectionless_Slave_Broadcast_Data'           : ['Status','LT_ADDR'],
    'HCI_Read_Synchronization_Train_Parameters'             : ['Status','Sync_Train_Interval','synchronization_trainTO','Service_Data'],
    'HCI_Write_Synchronization_Train_Parameters'            : ['Status','Sync_Train_Interval'],
    'HCI_Read_Secure_Connections_Host_Support'              : ['Status','Secure_Connections_Host_Support'],
    'HCI_Write_Secure_Connections_Host_Support'             : ['Status'],
    'HCI_Read_Authenticated_Payload_Timeout'                : ['Status','Connection_Handle','Authenticated_Payload_Timeout'],
    'HCI_Write_Authenticated_Payload_Timeout'               : ['Status','Connection_Handle'],
    'HCI_Read_Local_OOB_Extended_Data'                      : ['Status','C_192','R_192','C_256','R_256'],
    'HCI_Read_Extended_Page_Timeout'                        : ['Status','Extended_Page_Timeout'],
    'HCI_Write_Extended_Page_Timeout'                       : ['Status'],
    'HCI_Read_Extended_Inquiry_Length'                      : ['Status','Extended_Inquiry_Length'],
    'HCI_Write_Extended_Inquiry_Length'                     : ['Status'],
    #INFORMATIONAL PARAMETERS                                     
    'HCI_Read_Local_Version_Information'                    : ['Status','HCI_Version','HCI_Revision','LMP_Version','Manufacturer_Name','LMP_Subversion'],
    'HCI_Read_Local_Supported_Commands'                     : ['Status','Supported_Commands'],
    'HCI_Read_Local_Supported_Features'                     : ['Status','LMP_Features'],
    'HCI_Read_Local_Extended_Features'                      : ['Status','Page_Number','Maximum Page Number','Extended_LMP_Features'],
    'HCI_Read_Buffer_Size'                                  : ['Status','HC_ACL_Data_Packet_Length','HC_Synchronous_Data_Packet_Length','HC_Total_Num_ACL_Data_Packets','HC_Total_Num_Synchronous_Data_Packets'],
    #'HCI Read Country Code'                                 : ['Status','Country_Code'],    #DEPRECATED \x07
    'HCI_Read_BD_ADDR'                                      : ['Status','BD_ADDR'],
    'HCI_Read_Data_Block_Size'                              : ['Status','Max_ACL_Data_Packet_Length','Data_Block_Length','Total_Num_Data_Blocks'],
    'HCI_Read_Local_Supported_Codecs'                       : ['Status','Number_of_Supported_Codecs','Supported_Codecs_i','Number_of_Supported_Vendor_Specific_Codecs','Vendor_Specific_Codecs_k'],
    #STATUS PARAMETERS                                               
    'HCI_Read_Failed_Contact_Counter'                       : ['Status','Handle','Failed_Contact_Counter'],
    'HCI_Reset_Failed_Contact_Counter'                      : ['Status','Handle'],
    'HCI_Read_Link_Quality'                                 : ['Status','Handle','Link_Quality'],
    'HCI_Read_RSSI'                                         : ['Status','Handle','RSSI'],
    'HCI_Read_AFH_Channel_Map'                              : ['Status','Connection_Handle','AFH_Mode','AFH_Channel_Map'],
    'HCI_Read_Clock'                                        : ['Status','Connection_Handle','Clock','Accuracy'],
    'HCI_Read_Encryption_Key_Size'                          : ['Status','Connection_Handle','Key_Size'],
    'HCI_Read_Local_AMP_Info'                               : ['Status','AMP_Status','Total_Bandwidth','Max_Guaranteed_Bandwidth','Min_Latency','Max_PDU_Size','Controller_Type','PAL_Capabilities','Max_AMP_ASSOC_Length','Max_Flush_Timeout','Best_Effort_Flush_Timeout'],
    'HCI_Read_Local_AMP_ASSOC'                              : ['Status','Physical_Link_Handle','AMP_ASSOC_Remaining_Length','AMP_ASSOC_fragment'],
    'HCI_Write_Remote_AMP_ASSOC'                            : ['Status','Physical_Link_Handle'],
    'HCI_Get_MWS_Transport_Layer_Configuration'             : ['Status','Num_Transports','Transport_Layer_i','Num_Baud_Rates_i','To_MWS_Baud_Rate_k','From_MWS_Baud_Rate_k'],
    'HCI_Set_Triggered_Clock_Capture'                       : ['Status'],
    #7.6 TESTING COMMANDS                                        
    'HCI_Read_Loopback_Mode'                                : ['Status','Loopback_Mode'],
    'HCI_Write_Loopback_Mode'                               : ['Status'],
    'HCI_Enable_Device_Under_Test_Mode'                     : ['Status'],
    'HCI_Write_Simple_Pairing_Debug_Mode'                   : ['Status'],
    'HCI_Enable_AMP_Receiver_Reports'                       : ['Status'],
    'HCI_AMP_Test_End'                                      : ['Status'],
    'HCI_AMP_Test'                                          : ['Status'],
    'HCI_Write_Secure_Connections_Test_Mode'                : ['Status','Connection_Handle'],
    #7.8 LE CONTROLLER COMMANDS                                      
    'HCI_LE_Set_Event_Mask'                                 : ['Status'],                   
    'HCI_LE_Read_Buffer_Size'                               : ['Status','HC_LE_ACL_Data_Packet_Length','HC_Total_Num_LE_ACL_Data_Packets'],                     
    'HCI_LE_Read_Local_Supported_Features'                  : ['Status','LE_Features'],                                  
    'HCI_LE_Set_Random_Address'                             : ['Status'],                       
    'HCI_LE_Set_Advertising_Parameters'                     : ['Status'],                               
    'HCI_LE_Read_Advertising_Channel_Tx_Power'              : ['Status','Transmit_Power_Level'],                                      
    'HCI_LE_Set_Advertising_Data'                           : ['Status'],                         
    'HCI_LE_Set_Scan_Response_Data'                         : ['Status'],                            
    'HCI_LE_Set_Advertising_Enable'                         : ['Status'],                         
    'HCI_LE_Set_Scan_Parameters'                            : ['Status'],                        
    'HCI_LE_Set_Scan_Enable'                                : ['Status'],                    
    'HCI_LE_Create_Connection'                              : [None],                      
    'HCI_LE_Create_Connection_Cancel'                       : ['Status'],                             
    'HCI_LE_Read_White_List_Size'                           : ['Status','White_List_Size'],                         
    'HCI_LE_Clear_White_List'                               : ['Status'],                     
    'HCI_LE_Add_Device_To_White_List'                       : ['Status'],                             
    'HCI_LE_Remove_Device_From_White_List'                  : ['Status'],                                  
    'HCI_LE_Connection_Update'                              : [None],                      
    'HCI_LE_Set_Host_Channel_Classification'                : ['Status'],                                    
    'HCI_LE_Read_Channel_Map'                               : ['Status','Connection_Handle','Channel_Map'],                     
    'HCI_LE_Read_Remote_Features'                           : [None],                              
    'HCI_LE_Encrypt'                                        : ['Status','Encrypted_Data'],            
    'HCI_LE_Rand'                                           : ['Status','Random_Number'],         
    'HCI_LE_Start_Encryption'                               : [None],                     
    'HCI_LE_Long_Term_Key_Request_Reply'                    : ['Status','Connection_Handle'],                                
    'HCI_LE_Long_Term_Key_Request_Negative_Reply'           : ['Status','Connection_Handle'],                                         
    'HCI_LE_Read_Supported_States'                          : ['Status','LE_States'],                          
    'HCI_LE_Receiver_Test'                                  : ['Status'],                  
    'HCI_LE_Transmitter_Test'                               : ['Status'],                     
    'HCI_LE_Test_End'                                       : ['Status','Number_Of_Packets'],
    'LE_Remote_Connection_Parameter_Request_Reply'          : ['Status','Connection_Handle'],
    'LE_Remote_Connection_Parameter_Request_Negative_Reply' : ['Status','Connection_Handle'],
    'HCI_LE_Set_Data_Length'                                : ['Status','Connection_Handle'],
    'HCI_LE_Read_Suggested_Default_Data_Length'             : ['Status','SuggestedMaxTxOctets','SuggestedMaxTxTime'],
    'HCI_LE_Write_Suggested_Default_Data_Length'            : ['Status'],
    'HCI_LE_Read_Local_P-256_Public_Key'                    : [None],
    'HCI_LE_Generate_DHKey'                                 : [None],
    'HCI_LE_Add_Device_To_Resolving_List'                   : ['Status'],
    'HCI_LE_Remove_Device_From_Resolving_List'              : ['Status'],
    'HCI_LE_Clear_Resolving_List'                           : ['Status'],
    'HCI_LE_Read_Resolving_List_Size'                       : ['Status','Resolving_List_Size'],
    'HCI_LE_Read_Peer_Resolvable_Address'                   : ['Status','Peer_Resolvable_Address'],
    'HCI_LE_Read_Local_Resolvable_Address'                  : ['Status','Local_Resolvable_Address'],
    'HCI_LE_Set_Address_Resolution_Enable'                  : ['Status'],
    'HCI_LE_Set_Resolvable_Private_Address_Timeout'         : ['Status'],
    'HCI_LE_Read_Maximum_Data_Length'                       : ['Status','supportedMaxTxOctets','supportedMaxTxTime','supportedMaxRxOctets','supportedMaxRxTime'],
    'HCI_LE_Read_PHY'                                       : ['Status','Connection_Handle','TX_PHY','RX_PHY'],
    'HCI_LE_Set_Default_PHY'                                : ['Status'],
    'HCI_LE_Set_PHY'                                        : [None],
    'HCI_LE_Enhanced_Receiver_Test'                         : ['Status'],
    'HCI_LE_Enhanced_Transmitter_Test'                      : ['Status'],
    'HCI_LE_Set_Advertising_Set_Random_Address'             : ['Status'],
    'HCI_LE_Set_Extended_Advertising_Parameters'            : ['Status','Selected_Tx_Power'],
    'HCI_LE_Set_Extended_Advertising_Data'                  : ['Status'],
    'HCI_LE_Set_Extended_Scan_Response_Data'                : ['Status'],
    'HCI_LE_Set_Extended_Advertising_Enable'                : ['Status'],
    'HCI_LE_Read_Maximum_Advertising_Data_Length'           : ['Status','Maximum_Advertising_Data_Length'],
    'HCI_LE_Read_Number_of_Supported_Advertising_Sets'      : ['Status','Num_Supported_Advertising_Sets'],
    'HCI_LE_Remove_Advertising_Set'                         : ['Status'],
    'HCI_LE_Clear_Advertising_Sets'                         : ['Status'],
    'HCI_LE_Set_Periodic_Advertising_Parameters'            : ['Status'],
    'HCI_LE_Set_Periodic_Advertising_Data'                  : ['Status'],
    'HCI_LE_Set_Periodic_Advertising_Enable'                : ['Status'],
    'HCI_LE_Set_Extended_Scan_Parameters'                   : ['Status'],
    'HCI_LE_Set_Extended_Scan_Enable'                       : ['Status'],
    'HCI_LE_Extended_Create_Connection'                     : [None],
    'HCI_LE_Periodic_Advertising_Create_Sync'               : [None],
    'HCI_LE_Periodic_Advertising_Create_Sync_Cancel'        : ['Status'],
    'HCI_LE_Periodic_Advertising_Terminate_Sync'            : ['Status'],
    'HCI_LE_Add_Device_To_Periodic_Advertiser_List'         : ['Status'],
    'HCI_LE_Remove_Device_From_Periodic_Advertiser_List'    : ['Status'],
    'HCI_LE_Clear_Periodic_Advertiser_List'                 : ['Status'],
    'HCI_LE_Read_Periodic_Advertiser_List_Size'             : ['Status','Periodic_Advertiser_List_Size'],
    'HCI_LE_Read_Transmit_Power'                            : ['Status','Min_Tx_Power','Max_Tx_Power'],
    'HCI_LE_Read_RF_Path_Compensation'                      : ['Status','RF_Tx_Path_Compensation_Value','RF_Rx_Path_Compensation_Value'],
    'HCI_LE_Write_RF_Path_Compensation'                     : ['Status'],
    'HCI_LE_Set_Privacy_Mode'                               : ['Status'],
    'SMP Configure Security'                                : [],
    'SMP Initiate Security'                                 : [],              
    'SMP PassKey Reply'                                     : [],          
    'SMP OOB Data Reply'                                    : [],  
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