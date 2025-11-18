class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
      
        ans = []
        wordSet = set(wordDict)  # Convert list to set for efficient lookup

        def dfs(pref: str, suff: str) -> None:
            if suff == '':
                ans.append(pref.rstrip())  # Add the valid sentence to the answer list
            else:
                for i in range(len(suff)):
                    if suff[:i+1] not in wordSet: 
                        continue
                    dfs(pref + suff[:i+1] + ' ', suff[i+1:])  # Fix slicing issue

        dfs('', s)
        return ans