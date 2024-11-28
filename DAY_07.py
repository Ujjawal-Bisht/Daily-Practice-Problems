#   28-11-24

"""
Question 14: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
"""

str = input("Enter string:- ")
u = 0
l = 0
for i in str:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
print("UPPER CASE", u)
print("LOWER CASE", l)


"""
Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
"""
n = input("Enter number:- ")
sum = 0
for i in range (1,5):
    sum += int(n*i)
print(sum)