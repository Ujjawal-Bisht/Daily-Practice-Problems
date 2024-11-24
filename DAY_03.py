"""
Question 06: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24
"""
# q = sqrt((2*c*d)/h)

import math
c = 50
h = 30
q = list()
d = input("Enter numbers:- ").split(',')
for i in d:
    q.append(str(int(math.sqrt((2*c*int(i))/h))))
print(','.join(q))      #Join function will work only for list of strings
#So, convert list of int into list of strings

"""
Question 07: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
x = int(input("Enter number:- "))
y = int(input("Enter number:- "))
l = list()
for i in range(x):
    sub_l = list()
    for j in range(y):
        sub_l.append(i*j)
    l.append(sub_l)
print(l)