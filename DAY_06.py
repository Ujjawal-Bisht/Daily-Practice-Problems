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

for i in range(1000,3001,1):
    if even(i):
        print(i, end=',')