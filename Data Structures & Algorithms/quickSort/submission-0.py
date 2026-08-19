# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def partition(self, pairs: List[Pair], l: int, r: int):
        pivot = pairs[r]

        i = l-1

        for j in range(l, r):
            if pairs[j].key < pivot.key:
                i += 1
                pairs[i], pairs[j] = pairs[j], pairs[i]

        pairs[i+1], pairs[r] = pairs[r], pairs[i+1]

        return i+1

    def quickSortHelper(self, pairs: List[Pair], l: int, r: int):
        if l < r:
            pi = self.partition(pairs, l, r)
            self.quickSortHelper(pairs, l, pi-1)
            self.quickSortHelper(pairs, pi+1, r)

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)