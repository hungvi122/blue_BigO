"""
Printer Queue
Source: UVA   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

if __name__ == "__main__":
    iTC = int(input())
    for _ in range(iTC):
        n,m = map(int, input().split())
        params = input().split()
        priority_jobs = []
        pq = PriorityQueue()
        for i in range(n):
            job = int(params[i])
            priority_jobs.append((job, i))
            pq.put(-job)
        time = 0
        while len(priority_jobs) > 0:
            job = priority_jobs.pop(0)
            if -pq.queue[0] == job[0]:
                time += 1
                pq.get()
                if job[1] == m:
                    print(time)
                    break
            else:
                priority_jobs.append(job)
