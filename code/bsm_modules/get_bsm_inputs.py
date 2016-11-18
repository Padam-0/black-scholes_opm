"""
create_BS_matrix.py

This module contains 1 function, get_bsm_inputs() which takes no arguments

get_bsm_inputs() asks the user to enter the Black-Scholes input information
necessary for calculating the present day value of an option. If the user
doesn't want to enter manual inputs, they can select a default option.

The function returns the present day stock price, strike price, days to
maturity, volatility and risk free interest rate.

Requirements: None

"""


def get_bsm_inputs():
    met = False
    print("Please define some initial conditions")
    while met != True:
        if input('Would you like to enter initial conditions for '
                 'Black-Scholes? [y/n]: ').upper() == 'Y':
            s, x, t, sig, r = False, False, False, False, False

            try:
                S = float(input("What is today's stock price? "))
            except:
                print("Please try again. Stock price must be a number.")
                continue
            if S > 0:
                s = True

            try:
                X = float(input("What is the strike (exercise) price? "))
            except:
                print("Please try again. Exercise price must be a number.")
                continue
            if X > 0:
                x = True

            try:
                T = int(input("How many days away is the exercise date? "))
            except:
                print("Please try again. Days to maturity must be a number.")
                continue
            if T > 0:
                t = True

            try:
                sigma = float(input("What is the volatility (0.2 - 0.4) "))
            except:
                print("Please try again. Volatility must be a number.")
                continue
            if sigma > 0:
                sig = True

            try:
                R = float(input("What is the interest rate? (0.01 - 0.03) "))
            except:
                print("Please try again. Interest rate must be a number.")
            if R > 0:
                r = True

            if s and r and x and t and sig:
                met = True
                continue
            else:
                print("Error, please ensure each value is a positive number.")
                continue
        else:
            if input("Is using default inputs ok?\n\n"
                     "  - Stock Price today: $40.00\n"
                     "  - Strike Price: $42.00\n"
                     "  - Days to Maturity: 90\n"
                     "  - Risk Free Rate: 2%\n"
                     "  - Volatility: 30%\n\n"
                     "[y/n]: ").upper() == "Y":
                S = 40  # Stock Price today, in Dollars
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