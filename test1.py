mydic = {}
print(type(mydic))
print(mydic)
mydic1 = {"name":"Ammad", 100:2000, 1:"Khan"}
print(mydic1[1])
mydic["class"] = "AI"
print(mydic)
mydic["batch"] = 35
print(mydic)
mydic["students"] = ["ankd", "abc","xyz"]
print(mydic)
list1 = [1,2,3,4,5,6]
mydic[99] = list1
print(mydic)
print(mydic[99][4])
print(mydic[99][2:4])
mydic["batch"] = 1
print(mydic)
#newdic = {} 
#newdic = mydic + mydic1
#print(newdic)
nestdic = {"key1":{"name":"Ammad"},"key11":{"name":"Naeem"},"key111":[1,2,3]} 
print(nestdic["key11"]["name"])
print(nestdic["key111"][0])
for k,v in nestdic.items():
    print(k,v)
#for k in nestdic.values():
#    for k2 in k.keys():
#        print(k2)
liste = [1,2,2,3,4,5,5,6,7,7]
mylist = set(liste)
print(mylist)
