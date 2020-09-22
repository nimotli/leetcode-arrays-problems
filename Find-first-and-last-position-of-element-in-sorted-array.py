#NAME : FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY
#CATEGORY : ARRAYS
#DIFFICULTY : MEDIUM
#LINK : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums, target):
        ret = [-1,-1]
        if target not in nums:
            return ret
        i=0;j=len(nums)-1
        filledStart = False;filledEnd = False
        while not (filledStart and filledEnd):
            if(nums[i]==target):
                ret[0]=i
                filledStart=True
            if(nums[j]==target):
                ret[1]=j
                filledEnd=True
            if nums[i]<target:
                i=i+1
            if nums[j]>target:
                j=j-1
        return ret