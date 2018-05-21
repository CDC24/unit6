#Caleb Callaway
#5/21/18
#quiz6.py - quiz program

#Caleb Callaway
#5/21/18
#quiz6.py - quiz program

file = open ("engmix.txt")


                                    #Program 1

"""    
lett = input("what letter do you want? ")

for line in file:
    if (line.strip()).count(lett) == 4:
        print (line.strip())
"""

                                    #Program 2

"""
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[0] == line[8]:
            print (line)
            break
"""

                                    #Program 3

"""
num = int(input("Enter a number: "))
lett = input("Enter a letter: ")

for line in file:
    line = line.strip()
    if len(line) == num:
        if line[0] == lett:
            print (line)
"""

                                    #Program 4

"""
words = 0
for line in file:
    line = line.strip()
    if len(line) >= 10:
        words +=1
        if words == 8000:
            print (line)
            break
"""

                                    #Program 5

"""
greatnum = 0
word = ""

def vowelcount(part):
    return (part.count("a") + part.count("e") + part.count("i") + part.count("o") + part.count("u"))
    

for line in file:
    line = line.strip()
    if vowelcount(line) > greatnum:
        greatnum == vowelcount(line)
        word = line
print(word)
"""





