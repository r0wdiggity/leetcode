class Solution():
    def lengthOfLongestSubstring(self, string):
        '''
        Return the length of the longest substring of
        non-repeating characters for a given string.
        '''
        maxx = 0
        for i in range(len(string)):
            count = 1
            seen = [string[i]]
            for j in range(i+1, len(string)):
                if string[j] not in seen:
                    seen.append(string[j])
                    count += 1
                else:
                    break
            if count > maxx:
                maxx = count
        return maxx


if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLongestSubstring(" "))