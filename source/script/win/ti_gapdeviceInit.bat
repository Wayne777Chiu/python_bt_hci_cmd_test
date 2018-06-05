@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto gapdevini


:gapdevini
echo -Type           : 0x01 (Command)
echo -OpCode         : 0xFE00 (GAP_DeviceInit)
echo -Data Length    : 0x26 (38) byte(s)
echo  ProfileRole    : 0x04 (4) (Peripheral)
echo  MaxScanRsps    : 0x05 (5)
echo  IRK            : 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
echo  CSRK           : 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
echo  SignCounter    : 0x00000001 (1)

%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 00 FE 26 04 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 --delay 2


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit
