class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops_map = {
            "x": self.record,
            "+": self.record_sum,
            "D": self.record_dup,
            "C": self.invalidate,
        }
        # We initialize a stack
        self.stack = []

        for op in operations:
            real_op = op if op in ["+", "D", "C"] else "x"
            ops_map[real_op](op)

        return sum(self.stack)

    def record(self, x):
        self.stack.append(int(x))

    def record_sum(self, op):
        rec = self.stack[-1] + self.stack[-2]
        self.record(rec)

    def record_dup(self, op):
        self.record(self.stack[-1] * 2)

    def invalidate(self, op):
        self.stack.pop()
