class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M"
                }
        nums = [1000, 500, 100, 50, 10, 5, 1]
        combos = [900, 400, 90, 40, 9, 4]
        final = ""
        for i in range(len(nums)):
            if num - nums[i] >= 0:
                final += roman[nums[i]] * (num // nums[i])
                num -= nums[i] * (num // nums[i])
            if i < (len(nums) - 1):
                if num - combos[i] >= 0:
                    final += roman[nums[i] - combos[i]] + roman[nums[i]]
                    num -= combos[i]
                    
        return final