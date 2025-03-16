class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        [1,1,1,2,2,3]
        hashmap= {1: 3.
                    2: 2,
                    3: 1}

        max = 0
        k passes over hashmap O(n)
        current max turns to 0 as we have retrieved the kth max element from the hashmap
        """
        
        
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1



        output = []
        for _ in range(k):
            max = 0
            for key in hashmap:
                if hashmap[key] > max:
                    max  = hashmap[key]
                    out=key
                    
            output.append(out)
            hashmap[out] = 0


        return output

        
# Time complexity: O(n)
# Space complexity: O(n)
