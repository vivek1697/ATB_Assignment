def isValidString(s):
    
    # Defined Stack to keep track of expected values
    stack = []
    
    # Mapping of the Parenthesis
    bracket_mapping_dic = {'(':')', '{':'}', '[':']'}
    
    # Iterate on a string to check each char
    for char in s:
        # Check if char is present in the bracket_mapping_dic
        if char in bracket_mapping_dic:
            # If char is present push it in a stack
            # If not check for the next condition
            stack.append(bracket_mapping_dic[char])
        # Check if stack has any elment or not
        # If it has any element check the last element with the current element
        # If element present remove that element from the stack
        # Loop through next char
        elif len(stack) > 0 and char == stack[-1]:
            stack.pop()
        # If any of the condition not satisfied print result as a False
        else:
            print('False')
    # After loop through all the char in the string if length of stack is zero print True else print False
    if len(stack) == 0:
        print('True')
    else:
        print('False')




# Test case
s = "()[]{}"
isValidString(s)

# Extra Test Case
# s = ""
# s = "[[]}"
# s= "{[()[]]}"
# s = "([])"

# Time Complexity
# O(n)
# Because we just traverse each char of the string at a time

# Space Complexity
# O(n) 