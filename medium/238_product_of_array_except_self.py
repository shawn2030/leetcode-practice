class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        create prefix array, postfix array and output array of same length as input
        multiply every element with itself as you are traversing in both prefix and postfix
        prefix goes forward pass and postfdix goes reverse pass
        loop over output array with index i, multiply i-1 and i+1 in prefix and postfix
        """        

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i]*prefix[i-1]


        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i]*postfix[i+1]

        
        while i < len(nums):
            if i ==0:
                output[i] = 1 * postfix[i+1]

            elif i == len(nums)-1:
                output[i] = 1 * prefix[i-1]
            
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output
    

# TIme Complexity: O(n)
# Space Complexity : O(n)

        

