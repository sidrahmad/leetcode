class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        return max(
            self.diagonal(s, k, {'N', 'E'}),
            self.diagonal(s, k, {'N', 'W'}),
            self.diagonal(s, k, {'S', 'E'}),
            self.diagonal(s, k, {'S', 'W'})   )
    def diagonal(self, s: str, k: int, correct: set) -> int:
        Mdist = 0
        c = 0
        w = 0
        for move in s:
            if move in correct:
                c += 1
            else:
                c -= 1
                w += 1
            extra = 2 * min(k, w)
            Mdist = max(Mdist, c + extra)
        return Mdist