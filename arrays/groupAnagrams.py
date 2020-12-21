class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        calc = {}
        
        for i in range(len(strs)):
            temp = 0
            for char in strs[i]:
                temp += ord(char)**5
            if temp in calc:
                calc[temp].append(i)
            else:
                calc[temp] = [i]
        ans = []
        for key in calc:
            ans.append([strs[x] for x in calc[key]])

        return ans