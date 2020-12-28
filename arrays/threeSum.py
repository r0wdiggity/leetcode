class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        prev_out = None
        for i in range(len(nums) - 2):
            if nums[i] == prev_out:
                continue
            prev_out = nums[i]
            start = i + 1
            end = len(nums) - 1
            prev_in = None
            while start < end:
                if nums[start] == prev_in:
                    start += 1
                    continue
                test = nums[i] + nums[start] + nums[end]
                if test == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    prev_s = nums[start]
                    start += 1
                    while prev_s == nums[start] and start < len(nums) - 1:
                        start += 1
                    end = len(nums) - 1
                elif test > 0:
                    end -= 1
                else:
                    start += 1

        return ans         