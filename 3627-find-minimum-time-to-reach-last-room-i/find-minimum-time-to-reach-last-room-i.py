class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        #Djikstra's Algorithm
        n,m=len(moveTime),len(moveTime[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0]=0
        pq = [(0,0,0)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while pq:
            time,x,y = heapq.heappop(pq)
            if (x,y) == (n-1,m-1):
                return time
            if time > dist[x][y]:
                continue
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m :
                    wait_time = max(moveTime[nx][ny],time)+1
                    if wait_time<dist[nx][ny]:
                        dist[nx][ny] = wait_time
                        heapq.heappush(pq,(wait_time,nx,ny))


