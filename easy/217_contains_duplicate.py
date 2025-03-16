class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        [1,2,3,1]
        hashmap = {1: 2,
                2: 1,
                3: 1}

        for i in hashmap:
            if 2:
                retunr false
        '''

        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for key in hashmap:
            if hashmap[key] > 1:
                return True

        return False