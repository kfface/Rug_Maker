import sys
import csv




def makeRug(Pattern, Length):
    rug_pattern = Pattern
    rug_length = int(Length)
    pattern_length = len(rug_pattern)
    long_enough_pattern = "".join([rug_pattern] * (rug_length + 1))
    i = 0
    while i < rug_length:
        print(long_enough_pattern[i : i + pattern_length])
        i += 1

#if len(sys.argv) != 2:
#    print("usage: python rug_from_csv.py file.csv")
#    exit
rugs = []
with open(sys.argv[1], 'r', newline='\n') as file:
    rugDict = csv.DictReader(file)
    for rug in rugDict:
        rug["Length"] = int(rug["Length"])
        rugs.append(rug)
for rug in rugs:
    makeRug(rug['Pattern'], rug['Length'])
