class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i
            
sol = Solution()
print(sol.twoSum([3,4,5,6], 7))    