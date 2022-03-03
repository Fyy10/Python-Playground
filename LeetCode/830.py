class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        for idx, char in enumerate(s):
            if idx == 0:
                cnt = 1
                cur_char = char
                left = idx
                continue

            if char == cur_char:
                cnt += 1
                if idx == len(s) - 1 and cnt >= 3:
                    ans.append([left, idx])
            else:
                if cnt >= 3:
                    right = idx - 1
                    ans.append([left, right])
                cnt = 1
                left = idx
                cur_char = char

        return ans
