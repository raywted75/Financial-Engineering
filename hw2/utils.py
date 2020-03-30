def compute_p(F, c, m, n, r):
    C = F * c / m
    P = C * (1 - (1 + r/m)**(-n*m)) / (r/m) + F / (1 + r/m)**(n*m)
    return P


def approximate_r(P, F, c, m, n):
    r = ((F*c/m) + (F-P)/n) / ((F+P)/2)
    return r


def compute_r(P, F, c, m, n):
    r = approximate_r(P, F, c, m, n) # Initialize r by approximation    
    inc = 0.01
    
    while compute_p(F, c, m, n, r) - P > 0.0001: # If the derived P is larger than actual P, we should increase r
        if compute_p(F, c, m, n, r+inc) < P:  # If the derived P is smaller than actual P, we should lower the amount added to r
            inc /= 10
        else:
            r += inc          
    while P - compute_p(F, c, m, n, r) > 0.0001: # If the derived P is small than actual P, we should decrease r
        if compute_p(F, c, m, n, r-inc) > P:  # If the derived P is larger than actual P, we should lower the amount minus to r
            inc /= 10
        else:
            r -= inc

    if r < 0:
        r = 0
    return r/m


def compute_spot(spot_rates, m, ytm, c):
    pv = 0
    for i in range(len(ytm)):
        if i != (len(ytm) - 1):
            pv += (c / 2) / ((1 + ytm[len(ytm)-1] / 2) ** (i + 1))
            pv -= (c / 2) / ((1 + spot_rates[i] / m) ** (i + 1))
        else:
            pv += (1 + c / 2) / ((1 + ytm[len(ytm)-1] / 2) ** (i + 1))
            sn = ((pv / (1 + c / 2)) ** (-1 / (i + 1)) - 1) * 2
            return sn


def compute_forward(spot_rate_list):
    forward_rate_matrix = list()
    for i in range(len(spot_rate_list)):
        forward_rates = list()
        for j in range(len(spot_rate_list)):
            if j <= i:
                forward_rates.append("x")
            else:
                forward_rate = (((1 + spot_rate_list[j]) ** j) / ((1 + spot_rate_list[i]) ** i)) ** (1 / (j - i)) - 1
                forward_rates.append(f"{round(forward_rate*100, 2)}%")
        forward_rate_matrix.append(forward_rates)
    return forward_rate_matrix