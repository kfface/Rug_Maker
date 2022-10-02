
# Original solution
from operator import length_hint


def main():
    Pattern = input("Provide me with a pattern for your rug.\n")
    Length = int(input("How long should I make your rug?\n"))
    makeRug(Pattern, Length)

def makeRug(Pattern, Length):
#    pattern_length = len(Pattern)
#    for i in range(Length):
#        if i % pattern_length == 0:
#            print(Pattern)
#        else:
#            x = (Pattern[i % pattern_length : pattern_length])
#            x += Pattern[0 : (i % pattern_length)]
#            print(x)


#alt solution

    Length = Pattern
    rug_length = int(Length)
    pattern_length = len(Length)
    long_enough_pattern = "".join([Length] * (rug_length + 1))
    i = 0
    while i < rug_length:
        print(long_enough_pattern[i : i + pattern_length])
        i += 1

if __name__ == '__main__':
    main()