Get-NetIpConfiguration;
$netInterface= Read-Host -Prompt "Choose Interface Index";
$netConfRaw = Get-NetIpConfiguration -InterfaceIndex $netInterface
$name = $netConfRaw.InterfaceAlias;
$ip = $netConfRaw.IPv4Address.IPAddress;
$subnetMask = $netConfRaw.IPv4Address.PrefixLength;
$defaultGate = $netConfRaw.IPv4DefaultGateway.NextHop;
$compName = $netConfRaw.ComputerName;
$dnsSrv = $netConfRaw.DNSServer;
$dnsSrv = $dnsSrv | Where-Object -Property AddressFamily -eq 2;
$dnsSrvAddresses = $dnsSrv | Select-Object -Property ServerAddresses;
$netConfDta = [PSCustomObject]@{
    Ip = $ip;
    InterfaceName= $name;
    SubnetMask = $subnetMask;
    DefaultGateway = $defaultGate;
    DnsServers = $dnsSrvAddresses;
    #Domain= "";
    ComputerName= $compName;
    #Admins= 
}

$netConfDta | ConvertTo-Json