@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto letrant 
rem letrant ==> HCI_LETransmitterTest

:letrant
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x201E (HCI_LETransmitterTest)
echo -Data Length    : 0x03 (3) byte(s)
echo  TX Channel     : 0x00 (0)
echo  TestData Length: 0x00 (0)
echo  TestData       : 00
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 1E 20 03 00 00 00 -d


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit
