"""
Tanya and Postcard
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 256MB
"""

if __name__ == "__main__":
    message,text = input(), input()
    mapCharMessage, mapCharText = {}, {}
    for ch in message:
        mapCharMessage[ch] = mapCharMessage.get(ch,0) + 1
    for ch in text:
        mapCharText[ch] = mapCharText.get(ch,0) + 1

    countYay, countWhoops = 0, 0
    for ch, cM in mapCharMessage.items():
        cT = mapCharText.get(ch, 0)
        cM, cT, countYay = (0, cT-cM, countYay + cM) if cT >= cM else (cM - cT, 0, countYay + cT)
        mapCharMessage[ch] = cM
        mapCharText[ch] = cT
    for ch, cM in mapCharMessage.items():
        CH = chr(ord(ch) + ord('A') - ord('a')) if 'a' <= ch <= 'z' else chr(ord(ch) + ord('a') - ord('A'))
        cT = mapCharText.get(CH, 0)
        if cM > 0:
            countWhoops += cM if cT >= cM else cT
    print(countYay, countWhoops)