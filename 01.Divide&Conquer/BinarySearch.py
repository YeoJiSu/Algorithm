# Recursive code 
class BinarySearch: # 클래스 명은 대문자로 시작
    def __init__(self, ex_list, value):
        self.ex_list = ex_list 
        self.value = value
        self.low = 0
        self.high = len(ex_list)-1
        
    def recursiveCode(self, low = None, high = None): # 함수명은 소문자로 시작
        if low == None:
            low = self.low
        if high == None:
            high = self.high
            
        mid = int((low+high)/2) 
        if low>high:
            return "not found"
        elif self.ex_list[mid] == self.value:
            return mid
        elif self.ex_list[mid] < self.value:
            low = mid+1
            return self.recursiveCode(low, high)
        elif self.ex_list[mid] > self.value:
            high = mid-1
            return self.recursiveCode(low, high)
    
    def iterativeCode(self):
        low = self.low
        high = self.high
        mid = (low+high)//2 
        while low<=high:
            if self.ex_list[mid] == self.value:
                return mid
            elif self.ex_list[mid] > self.value:
                high-=1
            else:
                low += 1
            mid = (low+high)//2 
        return "not found"
        
    
ex_list = [2,5,8,12,16,23,38,56,72,91]
value= 23
bs = BinarySearch(ex_list,value)
print("Recursive result:",bs.recursiveCode())
print("Iterative result:",bs.iterativeCode())

