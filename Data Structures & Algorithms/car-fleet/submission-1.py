class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. Zip positions and speeds together so we keep them paired
        pair = [(p,s) for p,s in zip(position, speed)]

        # 2. Sort pairs by position in descending order (closest to target first)
        pair.sort(reverse = True)
        # 3. Create a stack to track fleet arrival times
        stack = []
        # 4. Loop through each car:
        for p,s in pair:
            stack.append((target - p)/s)
        #    a. Calculate arrival time: (target - pos) / spd

        #    b. Push time to stack
        #    c. Check collision: if stack has >= 2 elements and current car time <= previous car time:
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        #       - Pop current car (it merges into the fleet ahead)

        # 5. Return stack size (number of fleets)
        return len(stack)