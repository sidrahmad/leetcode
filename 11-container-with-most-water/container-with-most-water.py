class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        result=0
        while l<r:
            area_curr=min(height[l],height[r])*(r-l)
            result=max(result,area_curr)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return result