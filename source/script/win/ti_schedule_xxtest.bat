@echo off
rem this is for TI Dongle CC2540
::cls
rem %1 means init or not 1: needs init 0: not init 
rem check other %2 means current_num, %3 means last_num, %4 means file_namefor nextexecute.


if %1a==a goto init
if %1==0 goto starttest

:init
cd data
ti_schedule_init.bat 1 1 6 ti_schedule_xxtest


:starttest
SET /a tmpnum = %2 + 1
SET /a endnum = %3 + 1

if %2 == %endnum% goto gotoexit

if %2 == 1 goto step1
if %2 == 2 goto step2
if %2 == 3 goto step3
if %2 == 4 goto step4
if %2 == 5 goto step5
if %2 == 6 goto step6

:step1
ti_scan.bat 0 %tmpnum% %3 %4


:step2
ti_letrantest.bat 0 %tmpnum% %3 %4


:step3
ti_lerecvtest.bat 0 %tmpnum% %3 %4


:step4
ti_readbda.bat 0 %tmpnum% %3 %4


:step5
ti_readleLSF.bat 0 %tmpnum% %3 %4


:step6
ti_readlewls.bat 0 %tmpnum% %3 %4


:step6
ti_readLSF.bat 0 %tmpnum% %3 %4



:gotoexit
echo exit