def Calc_Investment_Report(Year,Amount_Investing,Interest_Rate):
    print("%-8s %-20s %-14s %-20s" % ("Year","Opening_Balance", "Interest", "Closing_Balance"))

    for count in range(1,Year+1):
        Opening_Balance = Amount_Investing
        Interest_Amount = Amount_Investing * Interest_Rate 
        Amount_Investing += Interest_Amount
        print("%-8d %-20.2f %-14.2f %-20.2f" % (count, Opening_Balance, Interest_Amount, Amount_Investing))

def main():

    Amount_Investing=float(input("Enter the amount to be invested:"))
    Interest_Rate=float(input("Enter the Rate in %:"))/100
    Year=int(input("Enter the number of years:"))

    Calc_Investment_Report(Year,Amount_Investing,Interest_Rate)

main()
    