class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        [2,7,11,15], target = 9
        hashmap = {7: 0,
                    2: 1,
                    15: 2,
                    11: 3}
        '''
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return []
# Time complexity: O(n)
# Space complexity: O(n)