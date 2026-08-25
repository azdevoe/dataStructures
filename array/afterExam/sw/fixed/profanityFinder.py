def profanityFinder(arr,k):
    final=[]
    start=0
    profanity={"fuck", "damn", "shit","shitty"}
    for end in range(arr):
        if arr[end] in profanity: final.append(arr[end])
        