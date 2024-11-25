25-11-24

"""
Question 08: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world
"""
n = input("Enter string:- ").split(',')
n.sort()
print(','.join(n))


"""
Question 09: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
"""
ch = True
while ch == True:
    n = input("Enter string:- ")
    print(n.upper())
    ch = input("Do you want to continue?(True/False) ").title()
    if  ch == "False":
        ch = False
    else:
        ch = True
    