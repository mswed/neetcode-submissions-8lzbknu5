import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1

        res = heapq.nlargest(k, [(count, n) for n, count in frequency.items()])

        return [x[1] for x in res]


s = Solution()
s.topKFrequent([1, 2, 2, 3, 3, 3], k=2)
