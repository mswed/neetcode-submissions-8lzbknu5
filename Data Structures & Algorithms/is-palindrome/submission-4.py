import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r"[\W_]+")
        clean = pattern.sub("", s).lower()
        print(repr(clean))

        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1

        return True
