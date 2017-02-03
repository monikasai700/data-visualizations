import csv
import sys
f = open('try2.csv')
csv_f = csv.reader(f)
fi=file('out.txt','w')
for row in csv_f:
 x =float(row[0])
 y =float(row[1])
 z = (x+y)/2
 print "successfull!!"
 sys.stdout = fi
 
