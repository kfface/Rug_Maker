import sys
import csv
import rugmaker
if len(sys.argv) != 2:
    print("usage: python rug_from_csv.py file.csv")
    exit
rugs = []
with open('rug_requests.csv', 'r', newline='\n') as file:
    rugDict = csv.DictReader(file)
    for rug in rugDict:
        rug["Length"] = int(rug["Length"])
        rug["Quantity"] = int(rug["Quantity"])
        rugs.append(rug)
        
for rug in rugs:
    count = 0
    while count < rug['Quantity']:
        rugmaker.makeRug(rug['Pattern'], rug['Length'])
        count += 1
