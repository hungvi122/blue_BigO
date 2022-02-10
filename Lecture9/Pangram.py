"""
Pangram
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    n = int(input())
    text = input()
    if n < 26:
        print("NO")
        exit(0)
    check = [1] * 26
    for ch in text:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if 'a' <= ch <= 'z':
            index = ord(ch) - ord('a')
            check[index] = 0
    if sum(check) > 0:
        print("NO")
    else:
        print("YES")