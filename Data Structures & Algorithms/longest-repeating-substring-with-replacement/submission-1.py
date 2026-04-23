from collections import defaultdict
import heapq


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for char in range(len(s)):
            frequency = defaultdict(int)
            for c in range(char, len(s)):
                sub_string_length = c - char + 1
                frequency[s[c]] += 1

                highest = heapq.nlargest(
                    1, [(count, n) for n, count in frequency.items()]
                )
                count = highest[0][0]
                if sub_string_length - count <= k:
                    res = max(sub_string_length, res)

        return res
