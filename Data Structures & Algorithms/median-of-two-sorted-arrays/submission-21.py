class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        mid = total_length // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = nums2, nums1
        
        l, r = 0, len(A) - 1

        while True:
            midA = (l + r) // 2
            midB = mid - midA - 2

            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if midA + 1 < len(A) else float("inf")

            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if midB + 1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total_length % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1