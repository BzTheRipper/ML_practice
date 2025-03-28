# Define log file path
$logFile = "git_setup_log.txt"

# Start logging
Write-Host "Starting Git setup..." | Tee-Object -FilePath $logFile

# Set up Git global username and email
Write-Host "Configuring Git username and email..." | Tee-Object -FilePath $logFile -Append
git config --global user.name "BzTheRipper" | Tee-Object -FilePath $logFile -Append
git config --global user.email "bayzid.baytur.redwan87@gmail.com" | Tee-Object -FilePath $logFile -Append

# Finish logging
Write-Host "Git configuration completed." | Tee-Object -FilePath $logFile -Append