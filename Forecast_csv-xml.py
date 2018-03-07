import csv

#change the csv file name to your forecast csv file name 
csvFile = 'Forecast.csv'
#change the output xml file name to what you want to call xml file
xmlFile = 'Forecast.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<forecast>' + "\n")

#header
xmlData.write('<header>' + "\n")
xmlData.write('<production-date>2014-11-20T00:00Z</production-date>'+'\n')
xmlData.write('<version>1.1</version>' + '\n')
xmlData.write('<filetype>forecast</filetype>' + "\n")
xmlData.write('<station-id>ofr</station-id>' + '\n')
xmlData.write('</header>'+'\n')

xmlData.write('<prediction-list>'+'\n')

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<prediction>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</prediction>' + "\n")
            
    rowNum +=1

xmlData.write('</prediction-list>'+'\n')
xmlData.write('</forecast>' + "\n")
xmlData.close()
