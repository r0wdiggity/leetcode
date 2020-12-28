class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = (len(nums) // 3)
        ans = set()
        holding = {}
        for i in nums:
            if i in holding:
                holding[i] += 1
                if holding[i] > count and i not in ans:
                    ans.add(i)
            else:
                if count < 1:
                    ans.add(i)
                holding[i] = 1
        return ans