class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque()
        left = 0
        count = 0
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            if right - left + 1 > k:
                if q and q[0] == left:
                    q.popleft()
                left += 1
            else:
                count += 1
            if count == k:
                result.append(nums[q[0]])
        return result