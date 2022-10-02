import sys
import csv
import rugmaker

if len(sys.argv) != 2:
    print("usage: python rug_from_csv.py file.csv")
    exit
rugs = []
with open(sys.argv[1], 'r', newline='\n') as file:
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
print("Now let's combine these rugs with our own premade rug")
def rugCombinePremade(rug1, rug2):
    rugmaker.makeRug('asdfasdfasdf', rug2['Length'])
    rugmaker.makeRug(rug2['Pattern'], 20)
rugCombinePremade(rugs[1],rugs[2])
<<<<<<< HEAD

print("Now let's combine these rugs with our own premade rug")
def rugCombinePremade(rug1, rug2):
    rugmaker.makeRug('asdfasdfasdf', rug2['Length'])
    rugmaker.makeRug(rug2['Pattern'], 20)
=======
print("Now let's combine these rugs")
def rugCombine(rug1, rug2):
    rugmaker.makeRug(rug1['Pattern'], rug2['Length'])
    rugmaker.makeRug(rug2['Pattern'], rug1['Length'])
>>>>>>> mergeconflict
rugCombine(rugs[1],rugs[2])
