class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line = [0 for i in range(len(nums)+1)]
        for l, r in queries:
            line[l]+=1
            line[r+1]-=1
        for i in range (1,len(line)):
            line[i]+=line[i-1]
        for i in range (len(nums)):
            if line[i]<nums[i]:
                return False
        return True