class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1
        
        heap = []
        for num in hash.keys():
            heapq.heappush(heap, (hash[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
