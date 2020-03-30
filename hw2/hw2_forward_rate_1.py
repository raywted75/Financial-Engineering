if __name__ == "__main__": 
    t = int(input("Time due for the beginning of forward rate(year): "))
    r = int(input("Duration of forward rate(year): "))
    pt = float(input(f"The price of the {t} year zero-coupon bond per unit nominal: "))
    ptr = float(input(f"The price of the {t+r} year zero-coupon bond per unit nominal: "))

    f = (pt / ptr) ** (1 / r) - 1
    print(f"f({t},{r}) = {f*100:.2f}%")