class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res = [-1, -1]
        min_len = float('inf')
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                length = right - left + 1
                if length < min_len:
                    res = [left, right]
                    min_len = length
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l: r+1] if min_len != float("inf") else ""