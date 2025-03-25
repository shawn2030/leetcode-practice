class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        this is a backtracking problem using a stack to keep track of the current path
        1. we start with an empty path and openN and closeN = 0
        2. if openN < n, we can add an open parenthesis
        3. if closeN < openN, we can add a close parenthesis
        4. if openN == closeN == n, we have a valid parenthesis
        5. we backtrack and try the other possibilities
        6. we keep track of the valid parenthesis in the result
        7. we return the result
        """
        res = []
        path = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(path))
                return
            
            if openN < n:
                path.append('(')
                backtrack(openN +1, closeN)
                path.pop()

            if closeN < openN:
                path.append(')')
                backtrack(openN, closeN + 1)
                path.pop()

        backtrack(0, 0)
        return res
# Time complexity: O(2^2n)
# Space complexity: O(2n)
