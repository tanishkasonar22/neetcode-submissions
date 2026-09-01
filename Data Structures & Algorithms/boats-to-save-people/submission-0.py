class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            # If the lightest and heaviest person can share a boat
            if people[i] + people[j] <= limit:
                i += 1  # Light person gets on the boat too
            
            j -= 1      # Heaviest person always gets on a boat
            res += 1    # Count the boat
            
        return res