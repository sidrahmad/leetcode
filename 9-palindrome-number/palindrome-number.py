class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revnum = 0
        y=x
        if x<0:
            return False
        while x>0:
            lastdigit=x%10
            revnum=revnum*10+lastdigit
            x=x//10
        if y==revnum:
            return True
        return False