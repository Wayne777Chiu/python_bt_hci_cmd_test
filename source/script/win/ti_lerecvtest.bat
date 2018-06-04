@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto lerecvt 
rem lerecvt ==> HCI_LEReceiverTest

:lerecvt
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x201D (HCI_LEReceiverTest)
echo -Data Length    : 0x01 (1) byte(s)
echo  RX Channel     : 0x00 (0)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 1D 20 01 00 -d


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit