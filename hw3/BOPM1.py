import math

X = float(input("Strike Price: "))
S = float(input("Stock Price: "))
r = float(input("Riskless Rate(%): ")) / 100
u = float(input("Uptick: "))
d = float(input("Downtick: "))
n = int(input("Periods: "))

R = math.exp(r)
P = (R - d) / (u - d)

sList = list()
for i in range(n + 1):
    s = S * (u ** (3 - i)) * (d ** (i))
    sList.append(s)

cList = list()
pList = list()
for i in range(n + 1):
    c = max(0, sList[i] - X)
    p = max(0, X - sList[i])
    cList.append(c)
    pList.append(p)

for i in range(n):
    tempList = [[],[]]
    for j in range(len(cList) - 1):
        cu = cList[j]
        cp = cList[j + 1]
        c = (P * cu + (1 - P) * cp) / R
        tempList[0].append(c)
        
        pu = pList[j]
        pp = pList[j + 1]
        p = (P * pu + (1 - P) * pp) / R
        tempList[1].append(p)
        
    cList = tempList[0]
    pList = tempList[1]

print("-------------------------")
print(f"Call Value = {cList[0]}")
print(f"Put Value = {pList[0]}")