from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        oppos = {"(": ")", "[": "]", "{": "}"}

        for i in range(len(s)):
            current = s[i]
            if current in ["(", "[", "{"]:
                stack.append(current)
            elif len(stack) > 0:
                last = stack.pop()
                if current != oppos[last]:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True
