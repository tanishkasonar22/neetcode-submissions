class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range (len(nums)):
            h[nums[i]] = i #replace the index with the recent one
        #search for the target element by substracting the known from the remain
        for i in range (len(nums)): #same nums array 
            y = target - nums[i]
#here the i is the index pf the num and the h is value and the h[] is the key or the index in the hash maps 
            if y in h and i != h[y]:
                return [i,h[y]]

        

        




        