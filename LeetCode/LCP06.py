class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for i in coins:
            ans += (i // 2) + (i & 1)
        return ans
