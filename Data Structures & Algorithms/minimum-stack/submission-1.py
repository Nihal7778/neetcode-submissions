class MinStack:

    def __init__(self):
        self.minStack = []
        self.minStack2 = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)

        if not self.minStack2:
            self.minStack2.append(val)

        else:
            self.minStack2.append(min(val,self.minStack2[-1]))


    def pop(self) -> None:
        self.minStack.pop()
        self.minStack2.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.minStack2[-1]

        
