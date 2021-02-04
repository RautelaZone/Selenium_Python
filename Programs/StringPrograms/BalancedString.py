s = "1234006"
Leftsum = 0
Rightsum = 0

for i in range(0, int(len(s) / 2)):
    Leftsum = Leftsum + int(s[i])
    Rightsum = (Rightsum + int(s[len(s) - 1 - i]))

print("Sum of Left:",Leftsum)
print("Sum of Right", Rightsum)

if (Leftsum == Rightsum):
    print("Balanced", end='\n')
else:
    print("Not Balanced", end='\n')






