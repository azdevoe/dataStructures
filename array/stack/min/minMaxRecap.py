class Min:
    def __init__(self):
        self.main=[]
        self.min=[]
    def add(self,num):
        if not self.main:
            self.main.append(num)
            self.min.append(num)
            return
        smallest=min(num,self.min[-1])
        self.main.append(num)
        self.min.append(smallest)
        print(self.main,self.min)
    def pop(self):
        if self.main:
            self.min.pop()
            curr =self.main.pop()
            return curr
        return 'stack empty'
v1=Min()
v1.add(5)
v1.add(4)
v1.add(2)
v1.add(3)