import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range
    # dimension should be 6row 2 columns
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2))
    print(x)

    return x
function1()

# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape
    x = np.arange(1,28,dtype=np.float64).reshape((3,3,3))     #wrtie your code here
    print(x)

    return x
function2()

#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[(a%5==0) & (a%7==0)] #wrtie your code here
    print(x)
    return a
function3()

#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
    arr = np.arange(9).reshape(3,3)
    print(arr)
    arr = arr[:,[1,0,2]]
    print(arr)
    return arr
function4()
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
    arr = np.zeros(20,dtype=np.int).reshape(4,5)
    print(arr)
    return arr
function5()

#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
    arr = np.zeros(10,dtype=np.int)
    arr[4] = 10
    arr[7] = 20
    print(arr)
    return arr
function6()

#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    return np.zeros(4 ,dtype=np.int64)#write your code here
function7()

def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.empty((2,5),dtype=np.uint32)#write your code here
    x.fill(6)
    return x
function8()

#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    x = np.arange(2,101,2)
    print(x)
    return x
function9()

#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-np.vstack(brr)# write your code here 
    print(subt)
    return subt
function10()

#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr1 = np.where((arr % 2) != 0, -1,arr)#write your code here 
    print(arr1)
    return
function11()

#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((arr.repeat(3),arr,arr,arr))#write your code here 
    print(ans)
    return ans
function12()

#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([3, 7, 2, 9, 12, 1, 27])
    ans = arr[(arr>5) & (arr<11)]#write your code here 
    print(ans)
    return ans
function13()

#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    ans = np.arange(10,34)
    print(ans)
    first, second, third, forth = np.split(ans, [6, 12, 18])#write your code here 
    print(first,"\n",second,"\n",third,"\n",forth)
    return ans
function14()

#task15
def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    print(arr)
    ans = arr[[1,0,2]]#write your code here 
    print(ans)
    return
function15()

#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.hstack((x,y))#write your code here 
  
    return ans
function16()

#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    print(arr)
    return np.where((arr%3 ==0) & (arr % 5 == 0) , 'YES' , 'NO')#write your code here  
function17()

#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = len(np.intersect1d(piaic,students)) # Write you code Here
    print(x)
    return x
function18()

def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =    np.arange(1,26).reshape(5,5)# Write your code here
    W =    X.T # Write your code here 
    b =     5 # Write your code here
    output =  (X*W)+b  # Write your code here
    return output
function19()


#Task20
def function20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2

    return xyz(x) #Write your Code here
function20()
