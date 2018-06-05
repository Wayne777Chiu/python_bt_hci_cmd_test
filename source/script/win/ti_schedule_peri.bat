@echo off
rem this is for TI Dongle CC2540
::cls
rem %1 means init or not 1: needs init 0: not init 

if %1a==a  goto init
if %1a==1a goto init
if %1a==0a goto starttest

:init
cd data
ti_schedule_init.bat 1 1 3 ti_schedule_peri

:starttest
if %2a==a   goto init_var
if %2a==%2a goto gototest

:init_var
SET /a two_pos   = 1
SET /a three_pos = 3
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


:step1
ti_gapdeviceInit.bat 0 %tmpnum% %three_pos% %FILE_IN%

:step2
ti_gapuadvda.bat 0 %tmpnum% %three_pos% %FILE_IN%

:step3
ti_gapmkdiv.bat 0 %tmpnum% %three_pos% %FILE_IN%

:gotoexit
echo exit
