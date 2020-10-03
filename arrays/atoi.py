class Solution:
    def myAtoi(self, string):
        if len(string) <= 0:
            return 0
        final = ''
        started = False
        for char in string:
            if char == ' ' and not started:
                continue
            elif (char == '-' or char == '+') and not started:
                started = True
                final += char
            elif char.isdigit():
                started = True
                final += char
            elif not char.isdigit() and started:
                break
            elif not char.isdigit() and not started:
                return 0
        if final == "-" or final == "+" or final == " " or final == "":
            return 0
        final = int(final)
        if (final) > 2147483647:
            return 2147483647
        if final < -2147483648:
            return -2147483648
        return final


if __name__ == "__main__":
    test = Solution()
    ans = (test.myAtoi("   -42"))
    ans = (test.myAtoi("4193 with words"))
    ans = (test.myAtoi("+-2"))
    print(ans)