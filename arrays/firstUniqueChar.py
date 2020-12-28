class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1