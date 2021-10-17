# Module 5 - Skill Building Exercise No. 1 Solution

def main():
    print("Number of years for an investment to double.\n")

    apr = float(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal*(1+apr)
        years = years + 1

    print("Years to double:", years)


main()
