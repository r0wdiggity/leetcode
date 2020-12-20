class Solution():
    def lengthOfLongestSubstring(self, s):
        '''
        Return the length of the longest substring of
        non-repeating characters for a given string.
        '''
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        maxlen = 0
        hashset = set()
        start = 0
        i = 0
        while i < (len(s)):
            if s[i] not in hashset:
                hashset.add(s[i])
                maxlen = max(maxlen, (i - start) + 1)
                i += 1
            else:
                hashset.remove(s[start])
                start += 1 
        return maxlen


if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLongestSubstring(" "))