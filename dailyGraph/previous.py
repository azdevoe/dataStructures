import random
class store:
    def __init__(self):
        self.mapp={}
        self.arr=[]
    def insert(self,val):
        if val not in self.mapp:
            self.arr.append(val)
            self.mapp[val]=len(self.arr)-1
            return True
        return False
    def remove(self,val):
        if val not in self.mapp:
            return False
        temp=self.mapp[val]
        if temp == len(self.arr)-1:
            self.arr.pop()
            del self.mapp[val]
        else:
            last=self.arr[len(self.arr)-1]
            [self.arr[len(self.arr)-1],self.arr[temp]] = [self.arr[temp],self.arr[len(self.arr)-1]]
            self.arr.pop()
            del self.mapp[val]
            self.mapp[last]=temp
        return True
    def getInt(self):
        num=random.randint(0,len(self.arr)-1)
        return self.arr[num]

t = store()
t.insert(1)
t.insert(2)
t.insert(6)
t.remove(6)
print(t.arr, t.mapp)