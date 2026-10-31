class Solution:
    def isValid(self, s: str) -> bool:
        o_map = {"(": ")", "{": "}", "[": "]"}
        c_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for p in s:
            if len(stack) == 0 and p in c_map:
                return False

            if p in o_map:
                stack.append(p)
            else:
                if c_map[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
