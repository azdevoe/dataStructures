import heapq

# lastCallEndTime:
# A call center has k agents, and all of them are free at minute 0.
# Each call is (arrival_minute, duration), and calls are sorted by arrival.
# Each call goes to the agent who is free first.
# A call starts at the later of its arrival time and that agent's free time.
# Return the minute when the very last call ends.
def lastCallEndTime(k, calls):
    heap=[0]*k
    for arrival_time, duration in calls:
            adder=max(heap[0],arrival_time)
            heapq.heappushpop(heap,adder+duration)
            print(heap)
    return max(heap)
print(lastCallEndTime(2,[(1,5),(2,3),(3,4)]))