class Solution(object):
    def reverse(self, x):
        revnum = 0
        sign=-1 if x <0 else 1
        x=abs(x)
        while x!=0:
            lastdigit=x%10
            revnum=revnum*10+lastdigit
            x=x//10
        result = revnum*sign
        if result > 2**31 -1 or result < -(2**31): 
            return 0 
        return result