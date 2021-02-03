'''
Given a string S, the task is to create a string with the first letter of every word in the string.
Input = "geeks for geeks"
Output: gfg
'''

str="bad is good"
str=str.split(" ")
temp=""
print(str)
for word in str:
    temp=temp+word[0]
print(temp)
