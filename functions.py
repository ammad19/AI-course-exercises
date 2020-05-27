print('a line before function')
def add():
    no1 = int(input('Enter 1st no: '))
    no2 = int(input('Enter 2nd no: '))
    print(no1 + no2)
print('a line after function')
add()
def add1(number1, number2):
    print(number1,'+',number2,'=', number1 + number2)
add1(number2=3,number1=5)
def add2(number1=0, number2=0):
    print(number1+number2)
add2(number2=5)
