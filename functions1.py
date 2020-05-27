def display_nums(first_num,second_num,*opt_nums):
    print(first_num)
    print(second_num)
    print(opt_nums)
    print(type(first_num))
    print(type(opt_nums))
display_nums(2,2,3,4,5)
# getting value back from functions using return keyword
def add(val1,val2):
    ans = val1+val2
    return ans,'Hello'#creates tupple
    print('after return')#this line will not be executed
result = add(2,4)
print(result)
print(type(result))
#functions as variables
def add(a,b):
    return a+b
def sub(b,a):
    return a-b
result = add(2,3)+sub(2,3)
print(result)
#local vs global variables
def beHappy():
    name = "Mr. A"#local variable
    print(f"{name} is happy")
beHappy()
#print(name) local scope will generate error
anotherName = "Mr. B"
def sad():
    print(f"{anotherName} is sad")
sad()
print(anotherName)#global scope
