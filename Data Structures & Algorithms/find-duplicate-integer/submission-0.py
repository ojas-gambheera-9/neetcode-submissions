class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                return i