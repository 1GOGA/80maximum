s = input()
d = len(s) // 2
print(s[:d] == s[:len(s)-d-1:-1])