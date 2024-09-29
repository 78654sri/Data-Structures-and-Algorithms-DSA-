from typing import List

class Solution:
    def longSubarrWthSumDivByK(self, a: List[int], n: int, k: int) -> int:
        remmap = {}
        remmap[0] = -1
        sum_val = 0
        maxlen = 0
        for i in range(n):
            sum_val += a[i]
            rem = sum_val % k
            if rem < 0:
                rem += k
            if rem in remmap:
                length = i - remmap[rem]
                maxlen = max(maxlen, length)
            else:
                remmap[rem] = i
        return maxlen