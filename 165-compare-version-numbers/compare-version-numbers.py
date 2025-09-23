class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rv1 = version1.split('.')
        rv2 = version2.split('.')
        len1,len2 = len(rv1),len(rv2)
        max_len= max(len1,len2)
        
        for i in range (max_len):
            r1 = int(rv1[i]) if i<len1 else 0
            r2 = int(rv2[i]) if i<len2 else 0

            if r1<r2:
                return -1
            elif r1>r2:
                return 1
        
        return 0