@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto rlewls 
rem rlewls ==> HCI_LEReadWhiteListSize

:rlewls
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x200F (HCI_LEReadWhiteListSize)
echo -Data Length    : 0x00 (0) byte(s)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 0F 20 00 -d


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit