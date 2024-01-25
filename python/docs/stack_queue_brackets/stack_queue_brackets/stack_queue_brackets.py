# from stack_queue_brackets.queue import Queue


def multi_bracket_validation(s):
    """Validates whether brackets in a string are balanced
    Arguments:
        s (str): String to validate
    """
    # Map of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    for char in s:
        if char in bracket_map.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_map:
            # If the character is a closing bracket and...
            # either the stack is empty or...
            # the top (first char) of the stack doesn't match the corresponding opening bracket...
            # then the brackets are not balanced
            if not stack or stack[-1] != bracket_map[char]:
                return False

            # Pop the opening bracket from the stack
            stack.pop()

    # If the stack is empty, all brackets are balanced
    return not stack
