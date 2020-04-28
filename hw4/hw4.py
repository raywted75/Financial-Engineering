import math
from scipy.stats import norm


S = float(input("Stock Price: "))
X = float(input("Strike Price: "))
sigma = float(input("Stock’s Volatility(%): ")) / 100
dividend = float(input("Dividends: "))
months = [int(x) for x in input("Months that dividends paid(example input: 1,4,7,10)").split(',')]   
r = float(input("Riskless Interest Rate(%)")) / 100
t = float(input("Duration of maturity(month): ")) / 12


D = 0
for month in months:
    if month / 12 < t:
        D += dividend * math.exp(-1 * r * (month / 12))
S_new = S - D

d1 = (math.log(S_new / X) + (r + sigma**2 / 2) * t) / (sigma * t**(1/2))
d2 = d1 - (sigma * t**(1/2))

n1 = norm.cdf(d1)
n2 = norm.cdf(d2)

call = S_new * n1 - X * math.exp(-1 * r * t) * n2
put = call + X * math.exp(-1 * r * t) - S_new


print(f"Call Price: {call}")
print(f"Put Price: {put}")