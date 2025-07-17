def Valid_Paranthesis(s):
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or bracket_map[char] != stack[-1]:
                return False
            stack.pop()
    return not stack
