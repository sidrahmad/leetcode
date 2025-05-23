class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base = sum(nums)     # Base sum of original values
        sum_pos = cnt_pos = 0
        min_pos = float('inf')
        best_nonpos = float('-inf')
        for x in nums:
            d = (x ^ k) - x  # Compute delta on the fly
            if d > 0:        # Positive improvement
                cnt_pos += 1
                sum_pos += d
                min_pos = min(min_pos, d)
            else:            # Non-positive (zero or negative)
                best_nonpos = max(best_nonpos, d)

        if cnt_pos % 2 == 0: # if even count of positives,
            return base + sum_pos # we can take them all

        loss = min(min_pos, -best_nonpos) # sacrifice the smaller loss
        return base + sum_pos - loss