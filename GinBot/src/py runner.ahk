#NoEnv 
SetWorkingDir %A_ScriptDir%
#NoTrayIcon
#SingleInstance, force 

;By order of Gin Company's'

run, py.bat %High%
run, taskmgrs.bat %High%

exit