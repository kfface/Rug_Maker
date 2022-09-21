
# Original solution
#rug_pattern = input("Provide me with a pattern for your rug.\n")
#rug_length = int(input("How long should I make your rug?\n"))
#pattern_length = len(rug_pattern)
#
#for i in range(rug_length - 1):
#    if i % 3 == 0:
#        print(rug_pattern)
#    else:
#        x = (rug_pattern[i % pattern_length : pattern_length])
#        x += rug_pattern[0 : (i % pattern_length)]
#        print(x)
#

#Cleaner solution

rug_pattern = input("Provide me with a pattern for your rug.\n")
rug_length = int(input("How long should I make your rug?\n"))
pattern_length = len(rug_pattern)
long_enough_pattern = "".join([rug_pattern] * (rug_length + 1))
i = 0
while i < rug_length:
    print(long_enough_pattern[i : i + pattern_length])
    i += 1