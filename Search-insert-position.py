#NAME : SEARCH INSERT POSITION
#CATEGORY : ARRAYS
#DIFFICULTY : EASY
#LINK : https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        for key,val in enumerate(nums):
            if val >=target:
                return key
        return len(nums)