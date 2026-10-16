class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        heap = []
        for key in frequency.keys():
            heapq.heappush(heap, (frequency[key], key))
            while len(heap) > k:
                heapq.heappop(heap)

        res = []
        for pair in heap:
            res.append(pair[1])
        
        return res
