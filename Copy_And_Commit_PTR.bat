xcopy "C:\Users\LockwoodE\workspace\Python Test Runner\src\build\exe.win32-3.4" "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner" /S /Y
xcopy "C:\Users\LockwoodE\workspace\Python Test Runner\src" "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner Source" /S /Y
svn add --force "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner\*"
svn add --force "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner Source\*"
svn commit -m --force-log "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner"
svn commit -m --force-log "C:\FirmwareVerification\TestTools\Trunk\APPS\Python Test Runner\Python Test Runner Source"
pause