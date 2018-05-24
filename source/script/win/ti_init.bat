@echo off

SET cmdpath=..\..
if %1a==a goto init

:init
echo this is for TI Dongle CC2540
echo GAP_DeviceInit
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 0 fe 26 08 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0

echo -OpCode         : 0xFE31 (GAP_GetParam)
echo -Data Length    : 0x01 (1) byte(s)
echo ParamID        : 0x15 (21) (Minimum Link Layer Connection Interval, 
echo                   When Using Connection Establishment 
echo                   Proc (mSec). TGAP_CONN_EST_INT_MIN)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 31 fe 1 15

echo -OpCode         : 0xFE31 (GAP_GetParam)
echo -Data Length    : 0x01 (1) byte(s)
echo  ParamID        : 0x16 (22) (Maximum Link Layer Connection Interval, 
echo                   When Using Connection Establishment 
echo                   Proc (mSec). TGAP_CONN_EST_INT_MAX)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 31 fe 1 16

echo -OpCode         : 0xFE31 (GAP_GetParam)
echo -Data Length    : 0x01 (1) byte(s)
echo  ParamID        : 0x1A (26) (Link Layer Connection Slave Latency, When Using 
echo                   Connection Establishment Proc (mSec) TGAP_CONN_EST_LATENCY)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 31 fe 1 1A

echo -OpCode         : 0xFE31 (GAP_GetParam)
echo -Data Length    : 0x01 (1) byte(s)
echo  ParamID        : 0x19 (25) (Link Layer Connection Supervision Timeout, 
echo                   When Using Connection Establishment 
echo                   Proc (mSec). TGAP_CONN_EST_SUPERV_TIMEOUT)
%cmdpath%\bt_hci_cmd_test_wc.py --raw 1 31 fe 1 19

goto gotoexit
if %1==1 goto scan
if %1==2 goto test2
if %1==3 goto test3
if %1==4 goto test4

:scan 
ti_schedule.bat 1 %cmdpath%

:test2
ti_schedule.bat 2 %cmdpath%

:test3
ti_schedule.bat 3 %cmdpath%

:test4
ti_schedule.bat 4 %cmdpath%

:EOF
echo Not Parameters.

:gotoexit
echo exit