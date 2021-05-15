import json
file = open("C:\\Users\\lenovo\\Documents\\GitHub\\WindowsServerQuickDoc\\NetConfigDocumentation\\dummy\\net_conf.json")
data = json.load(file)
htmlString = '<head><style>table, th, td {border: 1px solid black;}</style></head><table><tr><td>Ip</td><td>'+str(data["Ip"])+'</td></tr><tr><td>Subnet Mask</td><td>'+str(data["SubnetMask"])+'</td></tr></table>'
f = open("test.html","w")
f.write(htmlString)