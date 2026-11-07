from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = Counter(s1)
        freq2 = {}
        left = 0
        for right in range(len(s2)):
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1
            while right - left + 1> len(s1):
                if s2[left] in freq2:
                    freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq2 == freq1:
                    return True
        return False