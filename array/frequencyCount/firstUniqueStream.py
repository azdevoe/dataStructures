from collections import Counter, OrderedDict

class UniqueStream:
    def __init__(self):
        self.counter = Counter()
        self.queue = OrderedDict()

    def stream(self, char):
        # update counter
        mapp =self.counter
        queue=self.queue
        mapp[char]+=1
        # if new -> add to queue
        if char in queue:
            queue[char]+=1
        else:
            queue[char]=1
        # if now a repeat -> remove from queue
        if queue[char]>1 or queue[char]<1 or mapp[char]>1:
            del queue[char]

    def first_unique(self):
        # return front of queue, or -1 if empty
        if not self.queue: return -1
        return next(iter(self.queue))