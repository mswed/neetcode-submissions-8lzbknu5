from collections import deque
from typing import List


class Solution:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def divide(self, a, b):
        return int(a / b)

    def multiply(self, a, b):
        return a * b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operands = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            current = tokens[i]
            if current not in operands:
                stack.append(int(current))
            elif stack:
                b = stack.pop()
                a = stack.pop()
                if current == "+":
                    stack.append(self.add(a, b))
                if current == "-":
                    stack.append(self.substract(a, b))
                if current == "/":
                    stack.append(self.divide(a, b))
                if current == "*":
                    stack.append(self.multiply(a, b))
            else:
                return 0

        return int(stack.pop())
