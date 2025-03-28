class Solution:
    def daily_temps(temperatures: list[int]) -> list[int]:
       """
       first we declare a stack and a res list which stores the output. 
       if stack is empty we add the current index to the stack.
       if the current temperature is greater than the last temperature in the stack,
       we pop the last index from the stack and calculate the difference between the current index and
       the popped index.
       we keep doing until the current temperature is less than the last temperature in the stack.
       we append the differene to the res list.
       finally we return the res list.
       """
       stack = []
       res = [0] * len(temperatures)
       for i , temp in enumerate(temperatures):
           while stack and temp > temperatures[stack[-1]]:
               lastIndex = stack.pop()
               res[lastIndex] = i - lastIndex
           stack.append(i)
       return res
    
# Time complexity: O(n)
# Space complexity: O(n)