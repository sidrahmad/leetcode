class Solution:
    def minOperations(self, a: List[int], k: int) -> int:
        a.sort()
        i = j = count = 0

        while True:
            if i < len(a) and (j >= count or a[i] <= a[j]):
                x = a[i]
                i += 1
            else:
                x = a[j]
                j += 1
            
            if x >= k:
                return count
            
            if i < len(a) and (j >= count or a[i] <= a[j]):
                y = a[i]
                i += 1
            else:
                y = a[j]
                j += 1
            
            a[count] = 2 * x + y
            count += 1
        return -1