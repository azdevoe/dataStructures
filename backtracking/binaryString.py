def binary(k):
    result=[]
    path=[]
    choices=["0","1"]
    def backTrack():
        if len(path)==k:
            result.append("".join(path))
            return
        for i in range(len(choices)):
            path.append(choices[i])
            backTrack()
            path.pop()
    backTrack()
    return result
print(binary(4))