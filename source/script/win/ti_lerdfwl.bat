@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto leredefwl 
rem leredefwl ==> HCI_LERemoveDeviceFromWhiteList

:leredefwl
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x2012 (HCI_LERemoveDeviceFromWhiteList)
echo -Data Length    : 0x07 (7) byte(s)
echo  AddressType    : 0x00 (0) (Public Device Address)
echo  DeviceAddr     : 00:00:00:00:00:00
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 12 20 07 00 00 00 00 00 00 00 -d

if %1a==1a  goto schedulelist

goto gotoexit

:schedulelist
cd data
ti_schedule.bat 1 %2 %3

:gotoexit
echo exit