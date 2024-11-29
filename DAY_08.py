#   29/11/24

"""
Question 16: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
"""

n = input("Enter sequence:- ").split(',')
n = map(int,n)
res = [i*i for i in n if i%2 != 0]
print(res)


"""
Question 17: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200
"""