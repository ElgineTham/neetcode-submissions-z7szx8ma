class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = nums2, nums1

        l, r = 0, len(a) - 1
        while True:
            m_a = (l + r) // 2
            m_b = half - m_a - 2
            
            if m_a >= 0:
                left_a = a[m_a]
            else:
                left_a = float("-inf")
            
            if m_a + 1 < len(a):
                right_a = a[m_a + 1]
            else:
                right_a = float("inf")
            
            if m_b >= 0:
                left_b = b[m_b]
            else:
                left_b = float("-inf")
            
            if m_b + 1 < len(b):
                right_b = b[m_b + 1]
            else:
                right_b = float("inf")
            
            if left_a <= right_b and left_b <= right_a:
                if total % 2 == 0:
                    return (max(left_a, left_b) + 
                    min(right_a, right_b)) / 2
                else:
                    return min(right_a, right_b)
            elif left_a > right_b:
                r = m_a - 1
            else:
                l = m_a + 1
                


            


