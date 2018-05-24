@echo off
rem this is for TI Dongle CC2540
::cls

if %1a==a goto scan

:scan
cd data
ti_schedule_init.bat 1