"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the
new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known
to the caller as well.
"""


class Solution:
    def removeDuplicates(self, nums: list):
        """

        :param nums: list[int]
        :return: int - len of new list
        """

        len_ = 1

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ += 1

        return len_
