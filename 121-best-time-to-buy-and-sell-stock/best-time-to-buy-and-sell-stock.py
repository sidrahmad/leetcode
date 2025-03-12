class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= prices[0]
        maxi=0
        for p in prices:
            mini=min(mini,p)
            maxi=max(maxi,p-mini)
        return maxi
            
        