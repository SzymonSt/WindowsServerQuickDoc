import json
file = open("C:\\Users\\lenovo\\Documents\\GitHub\\WindowsServerQuickDoc\\UsersDocumentation\\dummy\\users_conf.json")
data = json.load(file)
htmlStrings = []
htmlBeggining = '<head><style>table, th, td {border: 1px solid black;}</style></head><table>'
htmlEnding = '</table>'
for dta in data:
    tmpStr  = '<tr><td>'+dta+'</td><td>'+str(data[dta])+'</td></tr>'
    htmlBeggining += tmpStr
htmlBeggining+=htmlEnding
f = open("test.html","w")
f.write(htmlBeggining)