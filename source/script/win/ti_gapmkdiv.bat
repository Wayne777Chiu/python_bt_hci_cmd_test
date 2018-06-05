@echo off
rem this is for TI Dongle CC2540
::cls
SET cmdpath=..\..
if %1a==a goto gmakediv


:gmakediv
echo -Type           : 0x01 (Command)
echo -OpCode         : 0xFE06 (GAP_MakeDiscoverable)
echo -Data Length    : 0x0A (10) byte(s)
echo  EventType      : 0x00 (0) (Connectable Undirect Advertisement)
echo  InitAddrType   : 0x00 (0) (Public)
echo  InitAddrs      : 00:00:00:00:00:00
echo  ChannelMap     : 0x07 (7) (Channel 37
echo                   Channel 38
echo                   Channel 39)
echo  FilterPolicy   : 0x00 (0) (Allow Scan Requests From Any, Allow 
echo                   Connect Request From Any.)

%cmdpath%\bt_hci_cmd_test_wc.py --raw 01 06 FE 0A 00 00 00 00 00 00 00 00 07 00 --delay 5


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit
