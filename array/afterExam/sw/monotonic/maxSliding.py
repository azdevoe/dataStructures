from collections import deque
def maxInSlidingWindow(arr,size):
    queue= deque()
    result = []
    start=0
    for end in range(len(arr)):
        if end-start>=size:
            if queue[0]<start:
                queue.popleft()
            
            while queue and arr[end]>arr[queue[len(queue)-1]]:
                queue.pop()
                
            queue.append(end)
                    
            result.append(arr[queue[0]])
    return result

print(maxInSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7],3))
