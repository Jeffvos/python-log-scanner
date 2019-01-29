import re
import os
import csv

directory = raw_input('dir: ')
searchstring = raw_input('search for: ')

def writeCSV(line, filename):
    csvFile='csv/csvfile.csv'
    file = open(csvFile, 'a')
    splitedline=line.split()
    file.write(splitedline[2] + ',' + filename)
    file.write('\n')
    file.close()

for filename in os.listdir(directory):
    fullpath = (os.path.join(directory, filename))
    with open(fullpath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(searchstring, line):
                writeCSV(line, filename)
                print ('found in ' + fullpath)
                
print('Done')