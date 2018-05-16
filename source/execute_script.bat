rem this is for TI Dongle CC2540
bt_hci_cmd_test_wc.py --raw 1 0 fe 26 08 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
bt_hci_cmd_test_wc.py --raw 1 31 fe 1 15
bt_hci_cmd_test_wc.py --raw 1 31 fe 1 16
bt_hci_cmd_test_wc.py --raw 1 31 fe 1 1A
bt_hci_cmd_test_wc.py --raw 1 31 fe 1 19
bt_hci_cmd_test_wc.py --raw 1 4 fe 3 3 1 0 --time 30

rem this for initialize for normal
rem HCI_Read_Local_Supported_Features
bt_hci_cmd_test_wc.py -d --raw 1 3 10 0
rem HCI_LE_Set_Event_Mask
bt_hci_cmd_test_wc.py -d --raw 1 1 20 8 1f 0 0 0 0 0 0 0
rem HCI_LE_Read_Buffer_Size
bt_hci_cmd_test_wc.py -d --raw 1 2 20 0
rem HCI_Read_Buffer_Size
bt_hci_cmd_test_wc.py -d --raw 1 5 10 0
rem HCI_LE_Read_Local_Supported_Features
bt_hci_cmd_test_wc.py -d --raw 1 3 20 0 
rem HCI_Read_BD_ADDR
bt_hci_cmd_test_wc.py -d --raw 1 9 10 0 
rem HCI_Read_Local_Name
bt_hci_cmd_test_wc.py -d --raw 1 14 c 0 
rem HCI_Read_Local_Version_Information
bt_hci_cmd_test_wc.py -d --raw 1 1 10 0 
rem HCI_Inquiry
bt_hci_cmd_test_wc.py --raw 1 1 4 5 33 8b 9e 30 0 
rem HCI_Inquiry_Cancel
bt_hci_cmd_test_wc.py -d --raw 1 2 4 0 