  
    # stack = empty list
    
    # cur = empty string
    # num = 0


    # FOR each character c in s:
    

    #     IF c is a digit:
    #         num = num * 10 + integer(c)
           
                
    #     ELSE IF c == '[':
    #         PUSH (num, cur) onto stack
    #         num = 0
    #         cur = empty string

    #     ELSE IF c == ']':
            
    #         POP (repeat_count, previous_string) from stack
    #         cur = previous_string + cur repeated repeat_count times

    #     ELSE:
    #         cur = cur + c

    # RETURN cur


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '[':
                stack.append((num, cur))
                num = 0
                cur = ""

            elif c == ']':
                repeat_count, previous_string = stack.pop()
                cur = previous_string + cur * repeat_count

            else:
                cur += c

        return cur
        

        