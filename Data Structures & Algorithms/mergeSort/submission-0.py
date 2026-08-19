# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr: List[Pair], l: int, mid: int, r: int):
        n1 = mid - l +1
        n2 = r - mid

        L = [0]*n1
        R = [0]*n2
        
        for i in range(n1):
            L[i] = arr[l+i]

        for j in range(n2):
            R[j] = arr[mid+1+j]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSortHelper(self, pairs:List[Pair], l:int, r:int) -> List[Pair]:
        if l < r:
            mid = l + (r-l) // 2

            self.mergeSortHelper(pairs, l, mid)
            self.mergeSortHelper(pairs,mid+1, r)
            self.merge(pairs, l, mid, r)

        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
