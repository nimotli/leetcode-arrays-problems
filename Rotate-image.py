#NAME : ROTATE IMAGE
#CATEGORY : ARRAYS
#DIFFICULTY : MEDIUM
#LINK : https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        newMat = matrix.copy()
        newMatrix = []
        previousRow = []
        oldRow = matrix[0]
        for i in range(len(newMat)):
            newRow = []
            for key,val in enumerate(newMat):
                newRow.insert(0,val[i])
            matrix[i]=newRow
