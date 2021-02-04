
name= "aniil"
char_list = []

for char in name:
    if char.isalpha():
        if char in char_list:
            print("Not an Isogram")
            char_list.append(char)
        else:
            print("Isogram")







