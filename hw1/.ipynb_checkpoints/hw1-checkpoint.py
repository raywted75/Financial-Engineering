import math
import pandas as pd
from tabulate import tabulate


principal = float(input("本金(萬元): ")) * 10000
period = int(input("期數(年): ")) * 12
r = float(input("年利率(%): "))

avg_payment = math.ceil(principal / period)
remaining_principal = principal
payments, interests, accumulated, indices  = [list() for i in range(4)]

total = 0
for i in range(period):
    payment = avg_payment if remaining_principal > avg_payment else int(remaining_principal)
    decimal, integer = math.modf(remaining_principal * r / 1200)
    interest = int(integer + 1) if decimal >= 0.5 else int(integer)
    total += payment + interest
    
    payments.append(payment)
    interests.append(interest)
    accumulated.append(total)
    indices.append(f"第 {i+1} 期")
    
    remaining_principal -= payment
    
table = pd.DataFrame({"本金(元)": payments, "利息(元)": interests, "本金利息累計(元)": accumulated}, index=indices)
summary = pd.DataFrame(data={"": [int(principal), int(period/12), r, avg_payment, table["利息(元)"].sum()]}, index=["本金(元)", "期數(年)", "年利率(%)", "平均每月攤還本金(元)", "全部利息(元)"], dtype='object')

print("\n")
print("基本資訊:")
print(tabulate(summary, tablefmt="grid"))
print("\n")
print(f"每月攤還本金、利息一覽表(共 {int(period)} 期):")
print(tabulate(table, headers='keys', tablefmt="grid"))