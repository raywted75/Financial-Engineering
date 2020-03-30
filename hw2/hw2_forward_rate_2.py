import pandas as pd
from tabulate import tabulate
from utils import compute_forward


if __name__ == "__main__":
    n = float(input("Years to Maturity: "))
    m = int(input("Payment(1. Annually, 2. Semi-annually, 4. Quarterly): "))

    spot_rate_list = [0.0]
    for i in range(int(m * n)):
        spot_rate = float(input(f"Add the spot rate(%) of {(i+1)/m} year zero coupon bond: ")) / 100
        spot_rate_list.append(spot_rate)

    label = [i / m for i in range(len(spot_rate_list))]
    forward_rate_table = pd.DataFrame(compute_forward(spot_rate_list), columns=label, index=label)

    print("--- Forward Rate Table ---")
    print(tabulate(forward_rate_table, headers='keys', tablefmt="grid"))