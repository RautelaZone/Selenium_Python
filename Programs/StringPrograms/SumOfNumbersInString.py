'''
Given a string str containing alphanumeric characters.
The task is to calculate the sum of all the numbers present in the string.
'''

str1 = "1abc23tb"  #435+23+1=

temp = "0"
Sum = 0

for ch in str1:
    if (ch.isdigit()):
        temp += ch
    else:
        Sum += int(temp)
        temp = "0"

final=Sum + int(temp)
print(final)

