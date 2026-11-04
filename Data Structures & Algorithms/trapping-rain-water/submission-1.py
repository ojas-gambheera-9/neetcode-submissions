class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        left = []
        right = []
        result = []
        m = 0
        for i in range(0, len(height)):
            m = max(m, height[i])
            left.append(m)
        m = 0
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            right.append(m)
        right = right[::-1]
        for i in range(len(height)):
            result.append(min(left[i], right[i]))
        for i in range(len(height)):
            f = result[i] - height[i]
            if f > 0:
                count += f
        return count
        