class MinStack:

    def __init__(self):
        self.stack = []

        # this stack stores the minimum value at the current stack's index
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # append the smaller value (either val or top of  
        # minStack)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
