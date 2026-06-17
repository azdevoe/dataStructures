from collections import deque,Counter
def firstNeg(arr,size):
    curr=start=0
    queue=deque([])
    final=[]
    for end in range(len(arr)):
        if arr[end]<0:
            queue.append(end)
        curr=curr+arr[end]
        
        if end>=size-1:
            
            if len(queue) >0 and queue[0] < start:
                queue.popleft()
            if len(queue) ==0:
                final.append(0)
            else:
                final.append(arr[queue[0]])
            curr=curr-arr[start]
            start+=1
    return final
