No = "1234006"
Len = (len(No))
Median = int(Len/2)+1
strMedian=str(Median)
Index = No.index(strMedian)
print("length is :", Len)
print("Mid is ", Median)
print("Index of Median is ",Index)
if Len % 2 == 0:
    print("There is no middle No so Aborted....")
else:
    pass


