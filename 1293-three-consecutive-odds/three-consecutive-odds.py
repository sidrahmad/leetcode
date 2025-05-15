class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return '111' in ''.join(str(x & 1) for x in arr)