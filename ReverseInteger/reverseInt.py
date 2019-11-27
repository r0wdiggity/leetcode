class Solution():
    def reverse(self, x):
        x = list(str(x))
        neg = ''
        if x[0] == '-':
            neg = x.pop(0)
        ans = (x[::-1])
        ans.insert(0, neg)
        ans = int(''.join(ans))
        if abs(ans) > 2147483647:
            return 0
        return ans


if __name__ == "__main__":
    test = Solution()
    ans = (test.reverse(-123))
    #ans = (test.convert("abc", 1))
    print(ans)