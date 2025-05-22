class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x:x[0])
        avaliable = []
        count = 0
        assigned = []
        k=0
        for time in range(len(nums)):
            while assigned and assigned[0]<time:
                heapq.heappop(assigned)
            while k < len(queries) and queries[k][0] <= time :
                heapq.heappush(avaliable, -queries[k][1])
                k+=1
            while len(assigned) < nums[time] and avaliable and -avaliable[0]>=time:
                heapq.heappush(assigned,-heapq.heappop(avaliable))
                count+=1
            if len(assigned) < nums[time]:
                return -1
        return len(queries) - count