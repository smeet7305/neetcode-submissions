from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l = 0
        r = 0
        max_freq = 0
        longest = 0
        n = len(s)

        while r < n:

            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

            r += 1

        return longest