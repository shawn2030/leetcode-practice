class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        we will use a stack to solve this problem. every integer will be pushed into the stack.
        initialize operations list where it includes + - * / operations.
        if the token is an integer, push it into the stack.
        if the token is an operation, pop the last two elements from the stack and apply the operation.
        push the result back to the stack.
        finally, return the last element of the stack.
        """

        mystack = []
        operations = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operations:
                mystack.append(int(token))
            else:
                if token == '+':
                    a = mystack.pop()
                    b = mystack.pop()
                    new_val = b + a
                    mystack.append(new_val)
                elif token == '-':
                    a = mystack.pop()
                    b = mystack.pop()
                    new_val = b - a
                    mystack.append(new_val)
                elif token == '*':
                    a = mystack.pop()
                    b = mystack.pop()
                    new_val = b * a
                    mystack.append(new_val)
                else:
                    a = mystack.pop()
                    b = mystack.pop()
                    new_val = int(b / a)
                    mystack.append(new_val)

        return mystack[-1]
    
# Time complexity: O(n)
# Space complexity: O(n)