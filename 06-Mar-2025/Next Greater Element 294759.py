# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        next_greater = defaultdict(lambda:-1)
        for i in range(len(nums2)):
            while mono_stack and mono_stack[-1] < nums2[i]:
                top = mono_stack.pop()
                next_greater[top] = nums2[i]
            mono_stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = next_greater[nums1[i]]
        return nums1