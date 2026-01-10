class Solution(object):
    def getConcatenation(self, nums):
        for i in nums:
            nums += nums
            return nums