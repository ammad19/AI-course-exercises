class abcd():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def getstr(self):
        x = input("Enter string: ")
        return x
    def printstr(self,y):
        print(y.upper())
a1 = abcd(1,"d")
print(a1.x)
a2 = abcd(4,"d1")
z = a2.getstr()
a2.printstr(z)
