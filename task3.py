def is_brackets_closed(input_string):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack:
                return False
            elif stack[-1] == brackets_map[char]:
                stack.pop()
            else:
                return False

    return not stack

print(is_brackets_closed("( ){[ 1 ]( 1 + 3 )( ){ }}")) #Симетрично
print(is_brackets_closed("( 23 ( 2 - 3)")) #Несиметрично
print(is_brackets_closed("( 11 }")) #Несиметрично
