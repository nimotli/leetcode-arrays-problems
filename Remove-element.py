#NAME : REMOVE ELEMENT
#CATEGORY : ARRAYS
#DIFFICULTY : EASY
#LINK : https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val) -> int:
        while val in nums:
            nums.remove(val)
            
        return len(nums)