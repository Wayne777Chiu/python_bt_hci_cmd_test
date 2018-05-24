@echo off
if %1 == 1 goto scan
if %1 == 2 goto test2
if %1 == 3 goto test3
if %1 == 4 goto test4

:scan
echo -OpCode         : 0xFE04 (GAP_DeviceDiscoveryRequest)
echo -Data Length    : 0x03 (3) byte(s)
echo  Mode           : 0x03 (3) (All)
echo  ActiveScan     : 0x01 (1) (Enable)
echo  WhiteList      : 0x00 (0) (Disable)
%2\bt_hci_cmd_test_wc.py --raw 1 4 fe 3 3 1 0 --delay 10
goto gotoexit

:test2
echo this is test2
goto gotoexit

:test3
echo this is test3
goto gotoexit

:test4
echo this is test4
goto gotoexit

:gotoexit
echo exit
cd ..
