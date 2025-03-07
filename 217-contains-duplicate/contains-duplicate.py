class Solution(object):
    def containsDuplicate(self, nums):
        thisset = set(nums)
        if len(thisset) == len(nums):
            return False
        return True