import codecs
import sys, os
import csv, json
from pprint import pprint

filename = os.path.abspath(sys.argv[1])
filedir = filename[:filename.rfind(os.path.sep)]
filename = filename[filename.rfind(os.path.sep)+1:]

# print filename
# print filedir

fout = open(os.path.join(filedir,filename[:filename.index('.')]+'.json'),'w',encoding="latin-1")
i = 0
jKeys = []

with open(os.path.join(filedir,filename), 'rU',encoding="latin-1") as fin:
    outCSV=(line for line in csv.reader(fin, dialect='excel'))
    for row in outCSV:
        #print (row)
        if i==0:
            jKeys = row
            i = i + 1
        elif len(row) == len(jKeys) :            
            js = {}
            for j in range(0,len(jKeys)):
                js[jKeys[j]] = row[j]
            #pprint(js)   
            fout.write(json.dumps(js))
            fout.write("\n")
            #print("Length: ", len(row), row) 
            #print "\n\n\n"
            i = i + 1
        else:
            print ("Some error with ",len(row), row)
    
fin.close()
fout.close()