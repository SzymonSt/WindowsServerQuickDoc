Get-LocalGroup;
$g = Read-Host -Prompt "Choose Group Of Users with specific rights"
$AdminRights = Get-LocalGroupMember -Group $g;
$users = $AdminRights | Where-Object -Property ObjectClass -EQ "User";
$groups = $AdminRights | Where-Object -Property ObjectClass -EQ "Group";
$users.Name | ConvertTo-Json;