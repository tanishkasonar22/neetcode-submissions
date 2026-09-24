class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.s1 = []
        for i in tokens:
            if i == '+':
                b, a = self.s1.pop(), self.s1.pop()
                self.s1.append(a + b)
            elif i == '-':
                b, a = self.s1.pop(), self.s1.pop()
                self.s1.append(a - b)
            elif i == '*':
                b, a = self.s1.pop(), self.s1.pop()
                self.s1.append(a * b)
            elif i == '/':
                b, a = self.s1.pop(), self.s1.pop()
                self.s1.append(int(a / b))
            else:
                self.s1.append(int(i))  # Fixed: removed 'return'
                
        return self.s1[-1]  # Fixed: moved outside the for loop