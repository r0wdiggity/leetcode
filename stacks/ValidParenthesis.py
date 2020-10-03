class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openb = ['(', '{', '[']
        closeb = {'(': ')', '{': '}', '[': ']'}
        if s[0] not in openb:
            return False
        opened = []
        for bracket in s:
            if bracket in openb:
                opened.append(bracket)
            elif len(opened) == 0 or bracket != closeb[opened.pop()]:
                return False
                    
        if len(opened) == 0:
            return True