"""
Soldier and bananas
Source: Codeforces   Time Limit: 1000ms   Memory Limit: 256MB
"""

if __name__ == "__main__":
    k,n,w = map(int, input().split())
    cost = (w * (w + 1) * k)//2 - n
    if cost < 0:
        print(0)
    else:
        print(cost)