@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto scan

::cd data
::ti_init.bat 1
:scan
echo -OpCode         : 0xFE04 (GAP_DeviceDiscoveryRequest)
echo -Data Length    : 0x03 (3) byte(s)
echo  Mode           : 0x03 (3) (All)
echo  ActiveScan     : 0x01 (1) (Enable)
echo  WhiteList      : 0x00 (0) (Disable)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 4 fe 3 3 1 0 --delay 10