@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto leconnupd 
rem leconnupd ==> HCI_LEConnectionUpdate

:leconnupd
echo -Type           : 0x01 (Command)
echo -OpCode         : 0x2013 (HCI_LEConnectionUpdate)
echo -Data Length    : 0x0E (14) byte(s)
echo  Handle         : 0x0001 (1)
echo  ConnIntervalMin: 0x0006 (6)
echo  ConnIntervalMax: 0x0006 (6)
echo  ConnLatency    : 0x0000 (0)
echo  ConnTimeout    : 0x000A (10)
echo  MinimumLength  : 0x0000 (0)
echo  MaximumLength  : 0x0000 (0)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 13 20 0E 01 00 06 00 06 00 00 00 0A 00 00 00 00 00

if %1a==1a  goto schedulelist

goto gotoexit

:schedulelist
cd data
ti_schedule.bat 1 %2 %3

:gotoexit
echo exit