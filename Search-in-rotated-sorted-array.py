#NAME : NEXT PERMUTATION
#CATEGORY : ARRAYS
#DIFFICULTY : MEDIUM
#LINK : https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums, target) -> int:
        for key, val in enumerate(nums):
            if val == target:
                return key
        return -1