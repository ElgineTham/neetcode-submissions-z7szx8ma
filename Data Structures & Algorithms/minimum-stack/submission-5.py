class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val.append(val)
        else:
            self.stack.append(val)
            if self.min_val[-1] >= val:
                self.min_val.append(val)

    def pop(self) -> None:
        if self.min_val[-1] == self.stack[-1]:
            self.min_val.pop()
        
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
