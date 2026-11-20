def totalBusyMinutes(slots: list[list[int]]) -> int:
    # slots is a list of [start, end] meetings, in any order.
    # Return the total number of minutes where at least one meeting is running.
    # Time shared by two meetings is counted only once.
    if not slots:return 0
    arr=sorted(slots)
    final=[]
    final.append(arr[0][:])
    count=0
    for start ,end in arr:
        prev=final[-1][1]
        if start<=prev:
            final[-1][1]=max(end,prev)
        else:
            final.append([start,end])
    for stat,en in final:
        count+=(en-stat)
    return count


print(totalBusyMinutes([[9,11],[10,13],[15,16]]))  # expect 5
print(totalBusyMinutes([[1,5],[2,3]]))             # expect 4
print(totalBusyMinutes([[1,2],[2,3]]))             # expect 2
print(totalBusyMinutes([]))                        # expect 0