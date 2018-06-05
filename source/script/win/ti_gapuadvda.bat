@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto gapuavdda


:gapuavdda
echo -Type           : 0x01 (Command)
echo -OpCode         : 0xFE07 (GAP_UpdateAdvertisingData)
echo -Data Length    : 0x05 (5) byte(s)
echo  AdType         : 0x01 (1) (Advertisement Data)
echo  DataLength     : 0x03 (3)
echo  AdvertData     : 02:01:06

%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 07 FE 05 01 03 02 01 06 --delay 5


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit