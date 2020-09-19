#NAME : REMOVE DUPLICATED FROM SORTED ARRAY
#CATEGORY : ARRAYS
#DIFFICULTY : EASY
#LINK : https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
nums = [0,0,1,1,1,2,2,3,3,4]
temp = []
dubs = []
for i in nums:
    if(i in temp):
        dubs.append(i)
    else:
        temp.append(i)
for i in dubs:
    nums.remove(i)
print(len(nums))