#   27-11-24

"""
Question 12: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
def even(num):
    while (num > 0):
        if (num % 10) % 2 == 0:
            pass
        else:
            return False
        num = num // 10
    return True

l = []
for i in range(1000,3001,1):
    if even(i):
        l.append(str(i))
print(",".join(l))


"""
Question 13: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
"""

n = input("Enter sentence:- ")
d = 0
l = 0
sp = 0
for i in n :
    if i.isdigit():
        d += 1
    elif i.isalpha():
        l += 1
    else:
        sp += 1
print("LETTERS", l)
print("DIGITS", d)