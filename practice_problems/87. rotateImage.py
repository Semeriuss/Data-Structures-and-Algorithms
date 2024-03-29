from typing import List


class Solution:    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
        
        return matrix
        
    
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(mat))


        
        