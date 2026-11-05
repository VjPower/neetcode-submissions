class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix)-1)* len(matrix[0]) + len(matrix[0]) - 1

        while l<=r:
            i = (l+r)//2
            j = i//len(matrix[0])
            k = i%len(matrix[0])

            if target > matrix[j][k]:
                l = i+1
            elif target < matrix[j][k]:
                r = i-1
            else:
                return True 

        return False
