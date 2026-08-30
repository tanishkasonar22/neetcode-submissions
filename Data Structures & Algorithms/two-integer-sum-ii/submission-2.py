class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# 1 based indeices is that we start counting from 1 not 0
        i = 0
        j = len(numbers) - 1

        while i < j:

            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            elif numbers[i] + numbers[j] < target:
                i += 1

            else:
                j -= 1