#task1: update dictionary
dic1 = {}
print(dic1)
print(type(dic1))
key1 = input("enter key: ")
val1 = input("enter value: ")
#dic1[key1] = val1
dic1.update(key1 = val1)
dic1.update(y = 3, z = 0)
print(dic1)
#task2: concatenate dict
dic2 = {1:23, "a":"abc"}
print(dic2)
dic2.update(dic1)
print(dic2)
#task3: check if given key exist or not
key2 = input("Enter key to search: ")
if key2 in dic2.keys():
    print("Its there")
else:
    print("not there")

#task4: generate dict 1-n
x = int(input("Enter a no: "))
dic3 = {}
for num in range(x):
    dic3[num] = num * num
print(dic3)
#task5 & 6: sum & multiply all values in dict
total_sum = 0
total_mul = 1
for value in dic3.values():
    total_sum += value
    if value > 0:
        total_mul = total_mul * value
print(total_sum)
print(total_mul)

#task7: del key in dict
y = input("Enter key: ")
if y in dic2.keys():
    dic2.pop(y) #del dic2[y]
    print(dic2)
else:
    print("key not found")
