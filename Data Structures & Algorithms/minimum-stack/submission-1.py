#correct logic wrong code 
class MinStack:

    def __init__(self):
        self.s1 = []
        self.res = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        
        if not self.res or val <= self.res[-1]:
            self.res.append(val)

    def pop(self) -> None:
        val = self.s1.pop()
        if val == self.res[-1]:
            self.res.pop()
        

    def top(self) -> int:
        return self.s1[-1]
            
        
    def getMin(self) -> int:
        return self.res[-1]

        
        
        
