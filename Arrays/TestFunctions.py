from Arrays.RemoveDuplicatesFromSortedArray import Solution


def test_remove_duplicates_from_sorted_array():
    nums = [1, 1, 1, 2, 3, 3]
    solution = Solution()
    len = solution.removeDuplicates(nums)
    print(len)


