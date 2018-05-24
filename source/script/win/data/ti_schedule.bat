@echo off
SET /a tmpnum = %2 + 1
SET /a endnum = %3 + 1
SET shortpath=..

if %2 == %endnum% goto gotoexit

cd %shortpath%
if %2 == 1 goto step1
if %2 == 2 goto step2
if %2 == 3 goto step3
if %2 == 4 goto step4
if %2 == 5 goto step5
if %2 == 6 goto step6

:step1
ti_scan.bat 1 %tmpnum% %3
goto nextstep

:step2
ti_letrantest.bat 1 %tmpnum% %3
goto nextstep

:step3
ti_lerecvtest.bat 1 %tmpnum% %3
goto nextstep

:step4
ti_readbda.bat 1 %tmpnum% %3
goto nextstep

:step5
ti_readleLSF.bat 1 %tmpnum% %3
goto nextstep

:step6
ti_readlewls.bat 1 %tmpnum% %3
goto nextstep

:step6
ti_readLSF.bat 1 %tmpnum% %3
goto nextstep

:nextstep
echo next step %tmpnum%
cd data
ti_schedule.bat 1 %tmpnum% %3

:gotoexit
echo exit
cd ..
