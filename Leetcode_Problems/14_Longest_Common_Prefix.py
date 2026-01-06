class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = ""
        for letter in range(len(strs[0])):
            for space in strs:
                if letter == len(space) or space[letter] != strs[0][letter]:
                    return result
            result += strs[0][letter]
        return result

        