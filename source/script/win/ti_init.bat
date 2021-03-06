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


if %1a==a goto gotoexit

:schedulelist
%4.bat 0 %2 %3 %4

:gotoexit
echo exit