from collections import deque

def is_palindrome(str: str) -> bool:
    normalized_str = str.lower().replace(" ", "")
    queue = deque(normalized_str)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    
    return True


test_string = ["radar","banana", "hannah", "pup", "nan", "lollipop", "eye", "6543456", "deed", "step on no pets"]

for item in test_string:
    print(f'{item} is palindrome - {is_palindrome(item)}')