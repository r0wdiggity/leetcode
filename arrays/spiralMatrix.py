class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        start = [0, 0]
        right_max = len(matrix[0]) - 1
        down_max = len(matrix) - 1
        up_max = 0
        left_max = 0
        ans = []
        # False is going across, True is going down
        updown = False
        # Down and Right are False, Up and Left are True
        reverse = False
        while len(ans) < (len(matrix[0]) * len(matrix)):
            ans.append(matrix[start[0]][start[1]])
            if updown:
                if reverse:
                    if start[0] == up_max:
                        start[1] += 1
                        updown = False
                        reverse = False
                        left_max += 1
                    else:
                        start[0] -= 1
                else:
                    if start[0] == down_max:
                        start[1] -= 1
                        updown = False
                        reverse = True
                        right_max -= 1
                    else:
                        start[0] += 1
            else:
                if reverse:
                    if start[1] == left_max:
                        start[0] -= 1
                        updown = True
                        down_max -= 1
                    else:
                        start[1] -= 1
                else:
                    if start[1] == right_max:
                        start[0] += 1
                        updown = True
                        up_max += 1
                    else:
                        start[1] += 1
        return ans