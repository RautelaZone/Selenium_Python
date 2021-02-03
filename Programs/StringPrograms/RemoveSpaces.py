'''
Given a string, remove spaces from it.
Input = "geeks  for geeks"
Output: geeksforgeeks
'''

str="geeks for geeks"
str=str.split(" ")
final="".join(str)
print(final)

