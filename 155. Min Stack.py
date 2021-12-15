
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.size = 0

    def push(self, x: int):
        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        temp = self.stack.pop()
        self.size -= 1
        if self.min[-1] == temp:
            self.min.pop()

    def top(self) :
        return self.stack[-1]
        

    def getMin(self) :
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()