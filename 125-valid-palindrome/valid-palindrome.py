import string
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.replace(" ","")
        s=re.sub('\W+','',s)
        s=s.replace("_","")
        s=s.lower()
        str=s[::-1]
        if s==str:
            return True
        else:
            return False