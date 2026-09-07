class Prefix:
    def __init__(self,arr):
        self.classArr=[0]*len(arr)
        self.classArr[0]=arr[0]
        for i in range(1,len(arr)):
            self.classArr[i]=self.classArr[i-1]+arr[i]
        print(self.classArr)
        
#v1=Prefix([1,2,3,4,5])

class PrefixExceptOne:
    def __init__(self,arr):
        self.classArr = [0]*len(arr)
        self.classArr[0]=arr[0]
        self.final = [0]*len(arr)
        for i in range(1,len(arr)):
            self.classArr[i]=self.classArr[i-1]+arr[i]
        for i in range(len(arr)):
            self.final[i]=self.classArr[-1] - arr[i]
        print(self.final)
#v2=PrefixExceptOne([1,2,3,4,5])


class PrefixSumWithoutMinus:
    def __init__(self,arr):
        self.prefix = [0]*len(arr)
        self.suffix=[0]*len(arr)
        self.final=[0]*len(arr)
        
        self.prefix[0]=0
        self.suffix[len(arr)-1]=0
        
        for i in range(1,len(arr)):
            self.prefix[i]=arr[i-1]+self.prefix[i-1]
            
        for i in range(len(arr)-2,-1,-1):
            self.suffix[i]=arr[i+1]+self.suffix[i+1]
            
        for i in range(len(arr)):
            self.final[i]=self.prefix[i]+self.suffix[i]
        
        print(self.prefix,self.suffix,self.final)
v3=PrefixSumWithoutMinus([1,2,3,4])

class PrefixMul:
    def __init__(self,arr):
        self.classArr=[0]*len(arr)
        self.classArr[0]=arr[0]
        for i in range(1,len(arr)):
            self.classArr[i] = self.classArr[i-1]*arr[i]
        print(self.classArr)

class PrefixMulExceptOne:
    def __init__(self,arr):
        self.classArr=self.final = [0]*len(arr)
        self.classArr[0]=arr[0]
        for i in range(1,len(arr)):
            self.classArr[i] = self.classArr[i-1]*arr[i]
        for i in range(len(arr)):
            self.final[i]=int(self.classArr[-1]/arr[i])
        print(self.final)
# v4=PrefixMul([1,2,3,4])
# v5=PrefixMulExceptOne([1,2,3,4])
