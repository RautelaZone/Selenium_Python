
'''
1) When user intentionally wants to raise exception
2) code after raising exception wont execute
'''
i=10
j=0
if j==0:
    print("can not be 0")
    raise Exception ('Dividend cannot be zero')
    print("This line will not print")           #wont execute as its aftre raising exception

else:
    result=i/j
    print("Result is:",result)

