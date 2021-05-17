import json
file = input("Provide input file path: ")
file = open(file)
fileOut = input("Provide output file path(if file is existing will be appended): ")
titleOfDoc = input("Provide title of your doc: ")
data = json.load(file)
htmlBeggining = '<head><style>table, th, td {border: 1px solid black;} h1{text-align:center;}</style></head><h1>'+titleOfDoc+'</h1><table>'
htmlEnding = '</table>'
for dta in data:
    tmpStr  = '<tr><td>'+dta+'</td><td>'+str(data[dta])+'</td></tr>'
    htmlBeggining += tmpStr
htmlBeggining+=htmlEnding
if(fileOut.split(".")[1]=="html"):
    f = open(fileOut,"a")
    f.write(htmlBeggining)
else:
    print("Wrong file extension")