def meetingRoom(arr:list):
    if not arr: True
    arr.sort(key=lambda x:x[0])
    former=arr[0][-1]
    for start,end in arr[1:]:
        if start<former:
            return False
        former=end
    return True
intervals = [[7, 10], [2, 4], [4, 7]]
print(meetingRoom(intervals))
print(meetingRoom([[15, 20], [0, 30], [5, 10]]))