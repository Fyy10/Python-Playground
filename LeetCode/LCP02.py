from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        # output n / m as [n, m]
        cont.reverse()
        n = 0
        m = 1
        for num in cont:
            n += m * num
            tmp = n
            n = m
            m = tmp
        
        tmp = n
        n = m
        m = tmp

        # note: a + 1 / b must be a simplified fraction (mathematically)
        return [n, m]
