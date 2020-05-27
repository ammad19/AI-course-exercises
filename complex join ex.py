z = ""
a = input("Enter CNIC:")
print("".join((x for x in a if str.isnumeric(x))))
#z = "z".join((x for x in a if str.isnumeric(x)))
#print(z)
dic1 = {"name": "Amad"}
y = input("Enter something: ")
dic1["name"] = y
#dic1.get(y)
print(y)
print(type(dic1))
