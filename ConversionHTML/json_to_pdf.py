import json
file = input("Provide input file path: ")
file = open(file)
fileOut = input("Provide output file path(if file is existing will be appended): ")
data = json.load(file)
htmlBeggining = '<head><style>table, th, td {border: 1px solid black;}</style></head><table>'
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