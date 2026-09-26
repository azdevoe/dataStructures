class Min:

    def __init__(self):
        self.main=[]
        self.min=[]
    def push(self,num):
        if not self.min:
            self.min.append(num)
            self.main.append(num)
            print(self.main)
            print(self.min)
            return
        smallest = min(num,self.min[-1])
        self.main.append(num)
        self.min.append(smallest)
        print(self.main)
        print(self.min)
    def pop(self):
        if not self.main or not self.min:
            return "empty stack"
        self.min.pop()
        return self.main.pop()
    
    def getMin(self):
        if not self.main or not self.min:
            return "empty stack"
        return self.min[-1]
    
    def top(self):
        return self.main[-1]

v1 = Min()
v1.push(5)
v1.push(3)
v1.push(4)
v1.push(6)
print(v1.pop())
print(v1.main,v1.min)
print(v1.getMin())
print(v1.top())

