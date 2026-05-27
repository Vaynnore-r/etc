while($true) {
    Stop-Process -Name "Strażnik" -ErrorAction SilentlyContinue -Force
    Stop-Process -Name "SysLock" -ErrorAction SilentlyContinue -Force
    Start-Sleep -Milliseconds 10
}

