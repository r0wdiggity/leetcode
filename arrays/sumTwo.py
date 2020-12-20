class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in d and d[target - nums[i]] != i:
                return (i, d[target - nums[i]])