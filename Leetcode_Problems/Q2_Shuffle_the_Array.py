class Solution(object):
    def shuffle(self, nums, n):
        suppose = []
        for i in range(n):
            suppose.append(nums[i])
            suppose.append(nums[i + n])
        return suppose
