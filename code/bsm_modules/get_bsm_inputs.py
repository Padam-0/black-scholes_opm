def get_bsm_inputs():
    met = False
    print("Please define some initial conditions")
    while met != True:
        if input('Would you like to enter initial conditions for Black-Scholes? '
                 '[y/n]: ').upper() == 'Y':
            s, x, t, sig, r = False, False, False, False, False

            S = input("What is today's stock price?")
            if type(S + 0.01) == float and S > 0:
                s = True
            X = input("What is the strike (exercise) price?")
            if type(X + 0.01) == float and X > 0:
                x = True
            T = input("How many days away is the exercise date?")
            if type(T + 0.01) == int and T > 0:
                t = True
            sigma = input("What is the volatility (0.2 - 0.4)")
            if type(sigma) == float and sigma > 0:
                sig = True
            R = input("What is the interest rate? (0.01 - 0.03)")
            if type(R + 0.01) == float and R > 0:
                r = True

            if s and r and x and t and sig:
                met = True
                continue
            else:
                print("Error, please ensure each value is a positive number.")
                continue
        else:
            if input("Is using default inputs ok? [y/n]: ").upper() == "Y":
                S = 42  # Stock Price today, in Dollars
                X = 42  # Strike Price, in Dollars
                T = 90  # Maturity Date, Days from now
                R = 0.02  # Risk free rate (% per year)
                sigma = 0.3  # Volatility
                met = True
                continue
            else:
                # If user elects to exit
                if input('Would you like to exit? [y/n]: ').upper() == 'Y':
                    # Exit
                    exit("User exit. No output file created.")
                # Otherwise, restart loop
                else:
                    # Restart loop
                    continue

    return S, X, T, sigma, R