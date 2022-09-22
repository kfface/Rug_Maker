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
        rugs.append(rug)
for rug in rugs:
    rugmaker.makeRug(rug['Pattern'], rug['Length'])
