class DHoom4:
    """
    Samarpit has Key, and N key other specific
    Pass: LockKey
    Samarpit can product the newKey : key * otherKey % 100000
    mergeKey take 1 second.
    INPUT:Key, LookKey
    N + otherKey
    OUTPUT: Minimize time to Product LookKey
    """
    def __init__(self,k, lock_key, n, other_key):
        self.k = k
        self.lock_key = lock_key
        self.n = n
        self.other_key = other_key

    def process(self):
        queue = [self.k]
        visited = [False] * 100000
        path = [-1] * 100000
        visited[self.k] = True
        if self.k == self.lock_key:
            return 0
        new_orderKey = []
        if self.lock_key %2 != 0:
            for i in self.other_key:
                if i%2 != 0:
                    new_orderKey.append(i)
            if self.k %2 == 0 or len(new_orderKey) == 0:
                return -1
        else:
            if self.k %2 != 0:
                count_even = 0
                for i in self.other_key:
                    if i % 2 == 0:
                        count_even += 1
                if count_even == 0:
                    return -1
            new_orderKey = self.other_key.copy()

        while len(queue) > 0:
            u = queue.pop(0)

            for x in new_orderKey:
                new_k = u * x % 100000
                if visited[new_k] is False:
                    visited[new_k] = True
                    path[new_k] = u

                    queue.append(new_k)
                if new_k == self.lock_key:
                    break

        if path[self.lock_key] > 0:
            count = 0
            t = self.lock_key
            while t != self.k:
                t = path[t]
                count += 1
            return count
        return -1


if __name__ == "__main__":
    k, lockpad = [int(i) for i in input().split()]
    n = int(input())
    other_key = [int(i) for i in input().split()]
    dhome4 = DHoom4(k,lockpad,n, other_key)
    res = dhome4.process()
    print(res)
