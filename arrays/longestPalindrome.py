class Solution():
    def longestPalindrome(self, string):
        if len(string) == 1:
            return string
        maxx = 0
        final = []
        for i in range(len(string)):
            count = 1
            temp = [string[i]]
            if i - 1 >= 0:
                j = i - 1
            else:
                if i == 0:
                    maxx = 1
                    final.append(string[i])
                continue
            if i + 1 < len(string):
                k = i + 1
            else:
                continue
            while j >= 0 and k < len(string):
                if string[j] == string[k]:
                    temp.insert(0, string[j])
                    temp.append(string[k])
                    count += 2
                    j -= 1
                    k += 1
                else:
                    break
            if count > maxx:
                maxx = count
                final = temp

        for i in range(len(string)):
            count = 0
            temp = []
            if i - 1 >= 0:
                if string[i] != string[i-1]:
                    continue
                else:
                    count = 2
                    temp = [string[i], string[i]]
                    if count > maxx:
                        maxx = count
                        final = temp
            else:
                continue
            if i + 1 < len(string):
                k = i + 1
            else:
                continue
            if i - 2 >= 0:
                j = i - 2
            else:
                continue
            while j >= 0 and k < len(string):
                if string[j] == string[k]:
                    temp.insert(0, string[j])
                    temp.append(string[k])
                    count += 2
                    j -= 1
                    k += 1
                else:
                    break
            if count > maxx:
                maxx = count
                final = temp

        return ''.join(final)


if __name__ == "__main__":
    test = Solution()
    print(test.longestPalindrome("aaaa"))