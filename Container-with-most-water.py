#NAME : CONTAINER WITH MOST WATER
#CATEGORY : ARRAYS
#DIFFICULTY : HARD
#LINK : https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maxArea = -1
        while i!=j:
            area = min([height[i],height[j]])*(j-i)
            if area>maxArea:
                maxArea = area
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return maxArea