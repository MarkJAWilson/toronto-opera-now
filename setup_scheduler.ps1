# PowerShell Script to register GTA Opera Daily Updater in Windows Task Scheduler

# Resolve script directory dynamically
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if ([string]::IsNullOrEmpty($ScriptDir)) {
    $ScriptDir = (Get-Item -Path ".\").FullName
}

Write-Host "Registering daily updater scheduled task..."
Write-Host "Working Directory: $ScriptDir"

# Action: Run Python to execute updater.py inside the workspace directory
$Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "updater.py" -WorkingDirectory $ScriptDir

# Trigger: Run daily at 3:00 AM
$Trigger = New-ScheduledTaskTrigger -Daily -At "3:00 AM"

# Settings: Allow execution on battery, wake up computer if needed, etc.
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Register Scheduled Task
try {
    Register-ScheduledTask -TaskName "GTA Opera Daily Updater" -Action $Action -Trigger $Trigger -Settings $Settings -Description "Scrapes and updates the GTA Opera database daily." -Force
    Write-Host "Successfully registered Scheduled Task 'GTA Opera Daily Updater'!" -ForegroundColor Green
    Write-Host "You can inspect it in Windows Task Scheduler (taskschd.msc)." -ForegroundColor Green
} catch {
    Write-Error "Failed to register scheduled task: $_"
    Write-Host "Make sure you are running PowerShell as Administrator." -ForegroundColor Red
}
