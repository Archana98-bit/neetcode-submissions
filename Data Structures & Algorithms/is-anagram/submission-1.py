class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()

print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))