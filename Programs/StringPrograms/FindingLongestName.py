names= { "Geek", "Geeks", "Geeksfor",  "GeeksforGeek45454545", "GeeksforGeeks" }
count = 0
for word in names:
    if len(word) > count:
        count = len(word)
        final = word
print(".....Word with maximum length is :",final)


