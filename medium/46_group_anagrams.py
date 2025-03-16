class Solution:
    def groupAanagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        ["eat","tea","tan","ate","nat","bat"]
        hashmap = {aet: [eat, tea, ate],
                    ant: [tan, nat],
                    abt: [bat]}
        '''
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)
        return list(hashmap.values())
# Time complexity: O(n)
# Space complexity: O(n)