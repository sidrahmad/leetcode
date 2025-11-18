from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        max_len = max((len(w) for w in word_set), default=0)

        @lru_cache(maxsize=None)
        def dfs(start: int) -> List[str]:
            if start == n:
                return [""]
            res = []
            for end in range(start + 1, min(n, start + max_len) + 1):
                word = s[start:end]
                if word in word_set:
                    for tail in dfs(end):
                        res.append(word if not tail else word + " " + tail)
            return res

        return dfs(0)