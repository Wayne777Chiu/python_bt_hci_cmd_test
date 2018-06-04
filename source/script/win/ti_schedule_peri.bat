@echo off
rem this is for TI Dongle CC2540
::cls
rem %1 means init or not 1: needs init 0: not init 


if %1a==a goto init
if %1==0 goto starttest

:init
cd data
ti_schedule_init.bat 1 1 3 ti_schedule_peri


:starttest
SET /a tmpnum = %2 + 1
SET /a endnum = %3 + 1

if %2 == %endnum% goto gotoexit

if %2 == 1 goto step1
if %2 == 2 goto step2
if %2 == 3 goto step3


:step1
ti_gapdeviceInit.bat 0 %tmpnum% %3 %4

:step2
ti_gapuadvda.bat 0 %tmpnum% %3 %4

:step3
ti_gapmkdiv.bat 0 %tmpnum% %3 %4


:gotoexit
echo exit
