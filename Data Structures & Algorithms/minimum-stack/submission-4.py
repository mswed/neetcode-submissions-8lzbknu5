class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.current_min = None

    def push(self, val: int) -> None:
        if self.current_min is not None:
            self.current_min = min(self.current_min, val)
        else:
            self.current_min = val

        self.stack.append(val)
        self.mins.append(self.current_min)

    def pop(self) -> None:
        self.mins.pop()
        self.current_min = self.mins[-1] if self.mins else None
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
