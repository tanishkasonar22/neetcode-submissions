class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                T,Ind = stack.pop() # this is to unpack the poped intem from stack like 30,0
                res[Ind] = i - Ind
            stack.append((t,i))
        return res


        
        