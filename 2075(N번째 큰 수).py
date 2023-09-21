# from queue import PriorityQueue
#
# N = int(input())
#
# que = PriorityQueue() # 우선순위 큐 생성 (Priority Queue는 내부적으로 heap 모듈을 사용함)
# # que = PriorityQueue(maxsize=N)
# for _ in range(N):
#     arr = list(map(int, input().split()))
#     for ar in arr:
#         if que.qsize() < N:
#             que.put((-ar,ar)) # 원소 삽입
#
#
#
# for _ in range(N-1):
#     que.get()[1]
#
# print(que.get()[1])

#----------------------------------------------------
# 최소힙으로 구현
import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for num in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지(메모리를 위해)
            heapq.heappush(heap, num)
        else:
            if heap[0] < num: #현재 놈이 힙의 최소값 보다 크면
                heapq.heappop(heap) # 최소값을 제거하고
                heapq.heappush(heap, num) # 현재놈 집어넣기
print(heap[0]) # n으로 제한해뒀으니 현재 젤 작은 놈이 n번째로 작은 값