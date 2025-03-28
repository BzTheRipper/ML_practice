# Remove the old virtual environment (if it exists)
if (Test-Path ".\windowsVenv") {
    Write-Host "Deleting the old virtual environment..."
    Remove-Item -Recurse -Force .\windowsVenv
} else {
    Write-Host "No old virtual environment found."
}

# Create a new virtual environment
Write-Host "Creating a new virtual environment..."
python -m venv windowsVenv

# Activate the new virtual environment
Write-Host "Activating the new virtual environment..."
.\windowsVenv\Scripts\Activate.ps1

# Confirm activation
Write-Host "The virtual environment has been activated."

# Upgrade pip to the latest version
Write-Host "Upgrading pip to the latest version..."
python.exe -m pip install --upgrade pip

# Install dependencies from requirements.txt (if it exists)
if (Test-Path ".\requirements.txt") {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt file found, skipping package installation."
}