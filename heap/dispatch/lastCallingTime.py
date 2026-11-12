import heapq

# lastCallFinishTime:
# A call center has agents, each busy until a certain minute.
# Calls arrive in order and every call waits for the agent who is free first.
# Return the minute when the very last call is finished.
def lastCallFinishTime(agent_free_times, call_durations):
    heapq.heapify(agent_free_times)
    print(agent_free_times)
    for num in call_durations:
        heapq.heappushpop(agent_free_times,agent_free_times[0]+num)
    return max(agent_free_times)
    
print(lastCallFinishTime([5, 2, 9],[4, 3, 2]))
print(lastCallFinishTime([0,0],[3, 2, 4]))
print(lastCallFinishTime([1, 9, 2], []))