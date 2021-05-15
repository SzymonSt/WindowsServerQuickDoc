Get-WindowsFeature | Where-Object {$_.InstallState -eq "Installed" -and $_.Depth -eq 1 -and $_.FeatureType -eq "Role"} | ConvertTo-Json -Depth 100 | Out-File "dummy/roles_conf.json";