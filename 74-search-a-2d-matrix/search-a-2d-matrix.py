class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        if n == 1 and m == 1:
            if matrix[n-1][m-1] == target:
                return True
            else:
                return False

        serchq = 0

        for col in range(n):
            if target <= matrix[col][m-1] and target >= matrix[col][0]:
                serchq = col

        l = 0
        r = m-1
        finq = matrix[serchq]

        while (l <= r):
            mid = (l + r)//2
            if finq[mid] == target:
                return True
            elif finq[mid] > target:
                r = mid - 1
            elif finq[mid] < target:
                l = mid + 1
        
        return False
        
