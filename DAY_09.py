#   1/12/24

"""
Question 18: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
"""


def check_validity(password):
    u = False
    l =False
    d = False
    s = False
    if (len(password)<6 or len(password)>12):
        return False
    for i in password:
        if (i.isupper()):
            u = True
            continue
        elif (i.islower()):
            l = True
            continue
        elif (i.isnumeric()):
            d = True
            continue
        elif (i in '@#$'):
            s = True
            continue
        else:
            return False
    if (u and l and d and s):
        return True
    else:
        return False


n = input("Enter password:- ").split(",")
for i in n:
    if (check_validity(i) == True):
        print(i)
    else:
        continue