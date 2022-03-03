class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        # 0 <= x <= 2^31 - 1
        ans = (x // 2) + (x & 1)

        # binary search
        while left < right - 1:
            ans = (left + right) // 2
            if ans * ans > x:
                right = ans
                ans = (left + ans) // 2
            else:
                left = ans
                ans = (ans + right) // 2
        return ans


sol = Solution()
num = (2 << 30) - 1
ans = sol.mySqrt(num)
print(ans)
