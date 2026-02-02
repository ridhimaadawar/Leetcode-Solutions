class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n

        write = 2  # position to write next valid element

        for i in range(2, n):
            # keep nums[i] only if it's not the same as nums[write-2]
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1

        return write
