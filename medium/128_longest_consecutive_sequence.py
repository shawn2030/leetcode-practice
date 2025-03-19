class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        we will use a set to check if certain number exists or not which is
        O(1) operation.
        traverse over the set and add 1 and chewck if the numkber exists O(1). making the whole
        operation O(n)
        for current element if num-1 exists we dont need to check that
        first condition is check if nums-1 does not exist and if satisfied move
        ahead and add 1 and check if it exists.
        this makes every element to be checked only once.
        """
        numSet = set(nums)
        longest  = 0

        for num in nums:
            if nums - 1 not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest