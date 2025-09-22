class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            max_left1 = float('-inf') if i == 0 else nums1[i-1]
            min_right1 = float('inf') if i == m else nums1[i]

            max_left2 = float('-inf') if j == 0 else nums2[j-1]
            min_right2 = float('inf') if j == n else nums2[j]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = i - 1
            else:
                left = i + 1
