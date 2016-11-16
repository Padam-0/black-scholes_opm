def get_bsm_inputs():
    print("Please define some initial conditions")
    met = False
    while met == False:
        S = input("What is today's stock price?")
        X = input("What is the strike (exercise) price?")
        T = input("How many days away is the exercise date?")
        sigma = input("What is the volatility (0.2 - 0.4)")
        r = input("What is the interest rate? (0.01 - 0.03)")

        if type(S + 0.01) == float and S > 0 and type(X + 0.01) == float \
                and X > 0 and type(T + 0.01) == int and T > 0 and \
                type(sigma) == float and sigma > 0 and type(r + 0.01) == float \
                and r > 0:
            met = True
        else:
            print("Error, please ensure each value is a positive number.")
            continue

    return S, X, T, sigma, r,