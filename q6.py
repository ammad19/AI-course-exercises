import math
C = 50
H = 30
Q = []
D = input("Enter no: ")
items = D.split(",")
for d1 in items:
    Q.append(str(int(round(math.sqrt(2*C*float(d1))/H))))
print(Q)
