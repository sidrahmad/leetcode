# 2. DP Top-down (Memoization)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve_memo(steps):
            if steps <= 1:
                return 1
            if steps in memo:
                return memo[steps]
            
            memo[steps] = solve_memo(steps - 1) + solve_memo(steps - 2)
            return memo[steps]
        
        return solve_memo(n)