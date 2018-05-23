# python bt hci command Test
this tools use python to send hci command and get hci event via serail port. 

## Usage for HCI Command Test
 usage: 
```graphviz= 

bt_hci_cmd_test_wc.py [-h] [-v] [--com COM_PORT] [--baudrate BAUD_RATE]
                             [--raw [RAW_DATA [RAW_DATA ...]]]
                             [--delay DELAY_DURATION] [-l] [-d]                        
```

### optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show the bt_hci_cmd_test_wc.py version.
  --com COM_PORT        COM Port
  --baudrate BAUD_RATE  Baudrate
  --raw [RAW_DATA [RAW_DATA ...]]
                        Using command with raw data.
  --delay DELAY_DURATION
                        Scan event timer
  -l, --license         Show logo
  -d, --display         Display PDU Data

### Example
```graphviz= 
//HCI_Read_Local_Supported_Features
bt_hci_cmd_test_wc.py --raw 1 3 10 0
//HCI_LE_Set_Event_Mask
bt_hci_cmd_test_wc.py --raw 1 1 20 8 1f 0 0 0 0 0 0 0
//HCI_LE_Read_Buffer_Size
bt_hci_cmd_test_wc.py --raw 1 2 20 0
//HCI_Read_Buffer_Size
bt_hci_cmd_test_wc.py --raw 1 5 10 0
//HCI_LE_Read_Local_Supported_Features
bt_hci_cmd_test_wc.py --raw 1 3 20 0
//HCI_Read_BD_ADDR
bt_hci_cmd_test_wc.py --raw 1 9 10 0
//HCI_Read_Local_Name
bt_hci_cmd_test_wc.py --raw 1 14 c 0
//HCI_Read_Local_Version_Information
bt_hci_cmd_test_wc.py --raw 1 1 10 0
//HCI_Inquiry
bt_hci_cmd_test_wc.py --raw 1 1 4 5 33 8b 9e 30 0
//HCI_Inquiry_Cancel
bt_hci_cmd_test_wc.py --raw 1 2 4 0
```


## Testing Device
- CC2540 USB Dongle
