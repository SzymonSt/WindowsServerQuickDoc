import json
file = open("C:\\Users\\lenovo\\Documents\\GitHub\\WindowsServerQuickDoc\\UsersDocumentation\\dummy\\users_conf.json")
data = json.load(file)
htmlStrings = []
# htmlString = '<head><style>table, th, td {border: 1px solid black;}</style></head><table><tr><td>Computer Name</td><td>'+str(data["ComputerName"])+'</td></tr><tr><td>Domain</td><td>'+str(data["Domain"])+'</td></tr><tr><td>Interface Name</td><td>'+str(data["InterfaceName"])+'</td></tr><tr><td>Ip</td><td>'+str(data["Ip"])+'</td></tr><tr><td>Subnet Mask</td><td>'+str(data["SubnetMask"])+'</td></tr></table>'
htmlBeggining = '<head><style>table, th, td {border: 1px solid black;}</style></head><table>'
htmlEnding = '</table>'
for dta in data:
    tmpStr  = '<tr><td>'+dta+'</td><td>'+str(data[dta])+'</td></tr>'
    htmlBeggining += tmpStr
htmlBeggining+=htmlEnding
f = open("test.html","w")
f.write(htmlBeggining)