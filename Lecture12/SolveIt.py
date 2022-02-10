"""
Solve It
Source: UVa   Time Limit: 1000ms   Memory Limit: 512MB
"""
import math

if __name__ == "__main__":
    while True:
        try:
            p,q,r,s,t,u = map(int, input().split())
            minValue, maxValue = 0, 1
            x = 0
            valueMax = p * math.e ** -x + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u
            x = 1
            valueMin = p * math.e ** -x + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u
            if valueMin * valueMax > 0:
                print("No solution")
                continue
            while True:
                x = minValue + (maxValue - minValue)/2
                value = p * math.e ** -x + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u
                if 0 <= value <= 10 ** -9:
                    print("{:.4f}".format(x))
                    break
                if value < 0:
                    minValue, maxValue = minValue, x
                else:
                    minValue, maxValue = x, maxValue
        except EOFError:
            exit(0)
