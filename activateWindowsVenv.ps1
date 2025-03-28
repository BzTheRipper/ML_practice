#Allow script execution
Write-Host "Allowing script execution..."
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Activate the new virtual environment
Write-Host "Activating the new virtual environment..."
.\windowsVenv\Scripts\Activate.ps1