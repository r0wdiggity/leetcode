class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        final = []
        la = len(nums1)
        lb = len(nums2)
        while len(final) < ((la + lb) // 2 + 1):
            if len(nums1) == 0:
                final.append(nums2.pop(0))
            elif len(nums2) == 0:
                final.append(nums1.pop(0))
            elif nums1[0] < nums2[0]:
                final.append(nums1.pop(0))
            else:
                final.append(nums2.pop(0))

        if (la + lb) % 2 != 0:
            median = final[-1]
        elif len(final) == 1:
            median = final[0]
        else:
            median = (final[-1] + final[-2]) / 2
        return median


if __name__ == "__main__":
    test = Solution()
    print(test.findMedianSortedArrays([], [1]))
