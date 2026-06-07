class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

nums = [1,2,3,4,5,6,7,8,9,3,6,8]

sol = Solution()
res = sol.hasDuplicate(nums)

print(res)