from collections import deque
def hasPath(graph,src,dst):
    visited=set()
    queue=deque([src])
    while len(queue)>0:
        curr=queue.popleft()
        if curr in visited:continue
        visited.add(curr)
        if curr == dst:
            return True
        for neighbour in graph[curr]:
            queue.append(neighbour)
    return False

directedIslands = {
  1: [2, 3],
  2: [4],
  3: [4],
  4: [5],
  5: [],

  6: [7],
  7: [8, 9],
  8: [10],
  9: [10],
  10: [],

  11: [12],
  12: [13],
  13: [],

  14: [15],
  15: [],
}
print(hasPath(directedIslands,1,5))