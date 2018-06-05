@echo off
rem this is for TI Dongle CC2540
::cls
rem %1 means init or not 1: needs init 0: not init 
rem check other %2 means current_num, %3 means last_num, %4 means file_namefor nextexecute.

if %1a==a  goto init
if %1a==1a goto init
if %1a==0a goto starttest

:init
cd data
ti_schedule_init.bat 1 1 6 ti_schedule_xxtest

:starttest
if %2a==a   goto init_var
if %2a==%2a goto gototest

:init_var
SET /a two_pos   = 1
SET /a three_pos = 6
goto gotoschedule

:gototest
SET /a two_pos = %2
SET /a three_pos = %3

:gotoschedule
SET FILE_IN=ti_schedule_peri
SET /a tmpnum = %two_pos% + 1
SET /a endnum = %three_pos% + 1

if %two_pos% == %endnum% goto gotoexit

if %two_pos% == 1 goto step1
if %two_pos% == 2 goto step2
if %two_pos% == 3 goto step3
if %two_pos% == 4 goto step4
if %two_pos% == 5 goto step5
if %two_pos% == 6 goto step6

:step1
ti_scan.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step2
ti_letrantest.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step3
ti_lerecvtest.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step4
ti_readbda.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step5
ti_readleLSF.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step6
ti_readlewls.bat 0 %tmpnum% %three_pos% %FILE_IN%


:step6
ti_readLSF.bat 0 %tmpnum% %three_pos% %FILE_IN%

:gotoexit
echo exit