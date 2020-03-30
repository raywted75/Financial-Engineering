if __name__ == "__main__": 
    t = float(input("Duration of spot rate: "))
    p = float(input("Unit zero-coupon bond price(0-1): "))

    s = p ** (-1 / t) - 1
    print("------------------------")
    print(f"{t} year spot rate of interest: {s*100:.2f}%")