class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_length = 0
        left = 0
        max_count = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])
            if right - left + 1 - max_count > k:
                if s[left] in freq:
                    freq[s[left]] -= 1
                else:
                    del freq[s[left]]
                left += 1
        return right - left + 1