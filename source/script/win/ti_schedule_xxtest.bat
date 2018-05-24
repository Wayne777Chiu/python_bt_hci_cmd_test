@echo off
rem this is for TI Dongle CC2540
::cls

if %1a==a goto teststart

:teststart
cd data
ti_schedule_init.bat 1 1 6