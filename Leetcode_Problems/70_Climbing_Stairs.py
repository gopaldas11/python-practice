class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1
        for i in range(n-1):
            think = one
            one = one + two
            two = think
        return one
        