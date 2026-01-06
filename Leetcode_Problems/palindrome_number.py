# class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 10:
            return False
        if x < 10:
            return True
        str_x = str(x)
        if str_x[::1] == str_x[::-1]:
            return True
        else:
            return False