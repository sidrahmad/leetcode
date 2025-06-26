class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1 
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if value + power <= k:
                    value += power
                    count += 1
            power *= 2
            if power > k:
                break
        for j in range(i - 1, -1, -1):
            if s[j] == '0':
                count += 1

        return count