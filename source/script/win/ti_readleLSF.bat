@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto rlelsf 
rem rlelsf ==> HCI_LEReadLocalSupportedFeatures

:rlelsf
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x2003 (HCI_LEReadLocalSupportedFeatures)
echo -Data Length    : 0x00 (0) byte(s)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 03 20 00 -d

if %1a==1a  goto schedulelist

goto gotoexit

:schedulelist
cd data
ti_schedule.bat 1 %2 %3

:gotoexit
echo exit