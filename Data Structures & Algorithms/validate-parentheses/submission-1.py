class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closePairs = { ')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in closePairs:

                # if stack is !empty and last element of stack
                # is equal to the hashmap value at key = char,
                # pop stack
                # meaning there is a valid pair
                if stack and stack[-1] == closePairs[char]:
                    stack.pop()
                # otherwise return false, meaning there isnt 
                # a valid pair
                else:
                    return False
            # if the incoming character isnt a close tag
            # append the opening tag to the stack
            else:
                stack.append(char)
        # if the parentheses are valid, the stack should 
        # be empty by the end of string stream
        return True if not stack else False
        