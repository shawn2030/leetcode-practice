class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myhash_s = {}
        myhash_t = {}
        for c in s:
            if c not in myhash_s:
                myhash_s[c] = 1
            else:
                myhash_s[c] +=1

        for c in t:
            if c not in myhash_t:
                myhash_t[c] = 1
            else:
                myhash_t[c] +=1

        return (myhash_s == myhash_t)
# Time complexity: O(n)
# Space complexity: O(n)