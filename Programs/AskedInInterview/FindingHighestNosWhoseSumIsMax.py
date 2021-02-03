'''
Finding two highest numbers whose sum is maximum
'''

nums=[7,11,15,3,25,1]
nums.sort()
print(nums)
maxNo=nums[len(nums)-1]
secondMaxNo=nums[len(nums)-2]
sum=maxNo+secondMaxNo
print("Two maximum nos are:",maxNo,"&",secondMaxNo,"and their sum is:",sum)


