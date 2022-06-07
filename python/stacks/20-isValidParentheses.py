
""" 20. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

* Input: "()"
* Output: true

* Input: "([)]"
* Output: false """

# TODO: Approach: Using Stack           [O(N) & O(1)]

class Solution:
    def isValid(self, s: str) -> bool:
        #? The stack to keep track of opening brackets.
        stack = []

        #? Hash map for keeping track of mappings. This keeps the code very clean.
        #? Also makes adding more types of parenthesis easier
        # NOTE: closing parenthesis is a key
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            #? If the character is an closing bracket
            if char in mapping:
                #? Pop the topmost element from the stack, if it is non empty
                #? Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                #? The mapping for the opening bracket in our hash and the top
                #? element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                #? We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        #? In the end, if the stack is empty, then we have a valid expression.
        #? The stack won't be empty for cases like ((()
        return not stack


if __name__ == "__main__":
    input = "([)]"        #? Output: False
    # input = "[()(){}]"    #? Output: True

    s = Solution()
    result = s.isValid(input)

    print(result)
