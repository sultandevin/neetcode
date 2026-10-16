class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen, n = {}, len(numbers)

        for i in range(n):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement] + 1, i + 1]

            seen[numbers[i]] = i
        
        return []
