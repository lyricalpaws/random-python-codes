@echo off 
echo If the proper username and password is not entered all files will be deleted by this virus. 
echo Good Luck 
set/p\/name=username: 
set/p\/password=password: 
echo haha you got the username and password wrong 
pause 
echo Files are being deleted 
pause 
dir/s 
del "c:up.bat" 
