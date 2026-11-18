class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows-1
        while top <= bottom:
            mid = (top+bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        l, r = 0, cols - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[mid][m] > target:
                r = m - 1
            elif matrix[mid][m] < target:
                l = m + 1
            else:
                return matrix[mid][m] == target
        return False