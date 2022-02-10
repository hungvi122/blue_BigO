"""
CamelCase
Source: Big-O   Time Limit: 1000ms   Memory Limit: 512MB
    # print words
    # index = 0
    # start = 0
    # print text
    # for ch in text:
    #     if 'A' <= ch <= 'Z':
    #         print(text[start: index])
    #         start = index
    #     index += 1
    # print(text[start:])
"""

if __name__ == "__main__":
    text = input()
    count = 0
    for ch in text:
        if 'A' <= ch <= 'Z':
            count += 1
    print(count + 1)