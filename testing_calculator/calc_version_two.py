import math

class Functions:

    def find_sqrt(self,num):
        return int(math.sqrt(num))
    
    def find_ceil(self,num):
        return math.ceil(num)

a = Functions()

print(a.find_sqrt(9))
print(a.find_ceil(99.78967))