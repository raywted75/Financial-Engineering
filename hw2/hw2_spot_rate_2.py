import pandas as pd
from tabulate import tabulate
from utils import compute_r, compute_spot


if __name__ == "__main__": 
    n = float(input("Years to Maturity: "))
    m = int(input("Payment(1. Annually, 2. Semi-annually, 4. Quarterly): "))

    coupon_rate = list()
    ytm = list()
    for i in range(int(m * n)):
        P = float(input(f"Bond Price of a {(i+1) / m} year due bond: "))
        F = float(input(f"Par Value of a {(i+1) / m} year due bond: "))
        c = float(input(f"Coupon Rate of a {(i+1) / m} year due bond: ")) / 100
        coupon_rate.append(c)
        r = compute_r(P, F, c, m, (i+1) / m)
        ytm.append(r * m)
        print()

    spot_rates = list()
    for i in range(int(m * n)):
        if (i+1) / m <= 1:
            spot_rates.append(ytm[i])
        else:
            spot_rates.append(compute_spot(spot_rates, m, ytm, coupon_rate[i]))

    due_row = [f"{(i+1)/m} 年" for i in range(int(m * n))]
    ytm_row = [f"{round(i*100, 2)}%" for i in ytm]
    spot_rates_row = [f"{round(i*100, 2)}%" for i in spot_rates]

    spot_rate_matrix = [due_row, ytm_row, spot_rates_row]

    spot_rate_table = pd.DataFrame(spot_rate_matrix, index=['到期時間', 'YTM', 'Spot Rate'])
    print(tabulate(spot_rate_table, tablefmt="grid"))
