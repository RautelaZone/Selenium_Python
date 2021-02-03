'''
Given a string of length N, made up of only uppercase characters 'R' and 'G',
where 'R' stands for Red and 'G' stands for Green.
Find out the minimum number of characters you need to change to make the whole string of the same colour.
'''

N=5
S="GGGGGGR"  #2
cR=0
cB=0

for i in range(len(S)):
    if S[i]=="R":
        cR=cR+1
    else:
        cB=cB+1

if cR<cB:
    print(cR)
else:
    print(cB)

print("*"*20)

