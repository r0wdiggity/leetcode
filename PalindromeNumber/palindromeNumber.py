class Solution():
    def isPalindrome(self, x):
        x_str = str(x)
        reverse = ''.join(list(str(x))[::-1])
        if x_str == reverse:
            return True
        return False


if __name__ == "__main__":
    test = Solution()
    #ans = (test.isPalindrome(121))
    ans = (test.isPalindrome(-121))
    #ans = (test.isPalindrome(10))
    print(ans)