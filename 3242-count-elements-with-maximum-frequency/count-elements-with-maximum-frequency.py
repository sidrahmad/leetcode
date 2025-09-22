class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=dict()
        for element in nums:
            if element in d:
                d[element] +=1
            else:
                d[element] =1
        values = list(d.values())
        max_value = max(values)
        count = values.count(max_value)
        return max_value*count
        