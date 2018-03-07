import csv

#change the csv file name to your observation csv file name 
csvFile = 'Observation.csv'
#change the output xml file name to what you want to call xml file
xmlFile = 'Observation.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<observation>' + "\n")

#header
xmlData.write('<header>' + "\n")
xmlData.write('<filetype>rwis-observation</filetype>' + "\n")
xmlData.write('<version>1.0</version>' + '\n')
xmlData.write('<road-station>oaa</road-station>' + '\n')
xmlData.write('</header>'+'\n')

xmlData.write('<measure-list>'+'\n')

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<measure>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</measure>' + "\n")
            
    rowNum +=1

xmlData.write('</measure-list>'+'\n')
xmlData.write('</observation>' + "\n")
xmlData.close()
