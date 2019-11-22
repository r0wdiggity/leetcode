class Solution:
    def convert(self, string, numRows):
        final = [[""] for x in range(numRows)]
        row = 0
        col = 0
        down = True
        for c in range(len(string)):
            # down
            if down:
                if row < numRows:
                    final[row][col] = string[c]
                    row += 1
                else:
                    col += 1
                    row = max(0, row - 2)
                    down = False
            if not down:
                if row > 0:
                    [final[x].append('') for x in range(numRows)]
                    final[row][col] = string[c]
                    row -= 1
                    col += 1
                else:
                    [final[x].append('') for x in range(numRows)]
                    final[row][col] = string[c]
                    row += 1
                    down = True
        a = ''.join([''.join(final[x]) for x in range(numRows)])
        return a

if __name__ == "__main__":
    test = Solution()
    ans = (test.convert("PAYPALISHIRING", 4))
    ans = (test.convert("abc", 1))
    print(ans)