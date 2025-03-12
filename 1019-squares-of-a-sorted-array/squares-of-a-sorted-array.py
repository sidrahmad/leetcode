class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        res=[0]*n
        for i in range(n-1,-1,-1):
            if (abs(nums[l])<abs(nums[r])):
                res[i]=(nums[r]*nums[r])
                r-=1
            else:
                res[i]=(nums[l]*nums[l])
                l+=1
        return res
