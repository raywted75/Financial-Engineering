import math
from scipy.special import comb

X = float(input("Strike Price: "))
S = float(input("Stock Price: "))
r = float(input("Riskless Rate(%): ")) / 100
u = float(input("Uptick: "))
d = float(input("Downtick: "))
n = int(input("Periods: "))

R = math.exp(r)
P = (R - d) / (u - d)

c = 0
p = 0
for j in range(n + 1):
    c += comb(n, j) * (P ** j) * ((1 - P) ** (n - j)) * max(0, S * (u ** j) * (d ** (n - j)) - X)
    p += comb(n, j) * (P ** j) * ((1 - P) ** (n - j)) * max(0, X - S * (u ** j) * (d ** (n - j)))
cValue = c / (R ** n)
pValue = p / (R ** n)

print(f"Call Value = {cValue}")
print(f"Put Value = {pValue}")