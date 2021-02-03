
'''
Given a string. Count the number of Camel Case characters in it.
'''

s="aniDLDJEsddd"
count=0
for c in range(0,len(s)):
    if s[c].isupper():
        count=count+1
print(count)