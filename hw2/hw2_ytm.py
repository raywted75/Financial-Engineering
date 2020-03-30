from utils import compute_r

if __name__ == "__main__":        
    P = float(input("Current Bond Price: "))
    F = float(input("Bond Par Value: "))
    c = float(input("Bond Coupon Rate(%): ")) / 100
    n = float(input("Years to Maturity: "))
    m = int(input("Payment(1. Annually, 2. Semi-annually, 4. Quarterly): "))

    r = compute_r(P, F, c, m, n)
    print("------------------------")
    print(f"Yield to Maturity: {r*100:.4f}%")