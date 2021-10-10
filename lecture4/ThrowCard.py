class ThrowCard:
    """
    Rule: take first to res. move next card to bottom card. while retain 1 card.
    INPUT:
    N size number card inorder, END with 0 card
    OUTPUT: the card number in the order take and last card
    """
    def process(self, n):
        arr_card = [i for i in range(1, n + 1)]
        res = []
        while len(arr_card) > 1:
            res.append(arr_card.pop(0))
            arr_card.append(arr_card.pop(0))
        return res, arr_card[0]


if __name__ == "__main__":
    playCard = ThrowCard()
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        res = playCard.process(n)
        if len(res[0]) > 0:
            print("Discarded cards: {}".format(", ".join(map(str, res[0]))))
        else:
            print("Discarded cards:")
        print("Remaining card: {}".format(res[1]))

