class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        if self.length == 0:
            self.stack.append([val , val])
        else:
            self.stack.append([val, min(val, self.stack[self.length - 1][1])])
        
        self.length +=1

    def pop(self) -> None:
        self.stack.pop()
        self.length -=1

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]