class Solution:
    def isValid(self, s: str) -> bool:
        """
        USE A STACK.
        create a dictionary of corresponding open and close brackets
        traverse over the string one-by-one
        if current string is closing
            if stack and stack[-1] == dict[c]--> pop
            else:
                retuyrn False
        else:
            stack.push(c)
        """
        brackets = {
                        '}' : '{',
                        ']' : '[',
                        ')' : '('
                    }
        stack = []

        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False
    
# Time Complexity = O(n)