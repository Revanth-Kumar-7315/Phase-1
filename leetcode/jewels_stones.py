def numJewelsInStones(jewels, stones):
    return sum(stone in set(jewels) for stone in stones)
