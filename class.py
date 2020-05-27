class student():
    def __init__(self,name,age,course): #initializer does work of constructor
#self in not a keyword, its a value holder,self holds ref of instance st1 & so on
        self.name=name
        self.age=age
        self.course=course
st1 = student("asad",12,"AI") #object is created here & refers to initializer
st11 = student("asad",13,"AI")
st111 = student("asad",12,"AI")
st1111 = student("asad",12,"AI") 
print(st1.name,st11.age)
