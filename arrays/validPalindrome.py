class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        VALID = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        alphanum = ""
        for i in s.upper():
            if i in VALID:
                alphanum += i
        start = 0
        end = len(alphanum) - 1
        while start <= end:
            if alphanum[start] == alphanum[end]:
                start += 1
                end -= 1
            else:
                return False
        return True