from collections import defaultdict
from pprint import pprint


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first_str = defaultdict(int)
        for c in s1:
            first_str[c] += 1
        second_str = defaultdict(int)

        # Our initial window is the length of the first string
        l = 0
        r = 0

        while r < len(s2):
            second_str[s2[r]] += 1

            if first_str == second_str:
                return True

            r += 1
            if r - (l + 1) == len(s1) - 1:
                second_str[s2[l]] -= 1
                if second_str[s2[l]] == 0:
                    del second_str[s2[l]]

                l += 1

        return False
