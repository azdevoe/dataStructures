class Maximum:

    def __init__(self):
        self.main=[]
        self.maximum=[]
    def push(self,num):
        if not self.maximum:
            self.maximum.append(num)
            self.main.append(num)
            print(self.main)
            print(self.maximum)
            return
        largest = max(num,self.maximum[-1])
        self.main.append(num)
        self.maximum.append(largest)
        print(self.main)
        print(self.maximum)
    def pop(self):
        if not self.main or not self.maximum:
            return "empty stack"
        self.maximum.pop()
        return self.main.pop()
    
    def getmaximum(self):
        if not self.main or not self.maximum:
            return "empty stack"
        return self.maximum[-1]
    
    def top(self):
        return self.main[-1]

v1 = Maximum()
v1.push(5)
v1.push(3)
v1.push(4)
v1.push(6)
print(v1.pop())
print(v1.main,v1.maximum)
print(v1.getmaximum())
print(v1.top())

