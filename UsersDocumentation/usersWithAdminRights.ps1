$gs = Get-LocalGroup | Out-String;
Write-Host $gs;
$g = Read-Host -Prompt "Choose Group Of Users with specific rights"
$AdminRights = Get-LocalGroupMember -Group $g;
$users = $AdminRights | Where-Object -Property ObjectClass -EQ "User";
$groups = $AdminRights | Where-Object -Property ObjectClass -EQ "Group";
$netConfDta = [PSCustomObject]@{
   Users = $users.Name;
   Groups = $groups.Name;
}
$netConfDta | ConvertTo-Json;