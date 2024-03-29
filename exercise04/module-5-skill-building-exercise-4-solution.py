# Module 5 - Skill Building Exercise No. 4 Solution

def main():
    print("Heating and Cooling degree-day calculation.\n")

    heating = 0.0
    cooling = 0.0
    tempStr = input("Enter an average daily temperature: ")
    while tempStr != "":
        temp = float(tempStr)
        heating = heating + max(0, 60-temp)
        cooling = cooling + max(0, temp-80)
        tempStr = input("Enter an average daily temperature: ")

    print("\nTotal heating degree-days", heating)
    print("Total cooling degree-days", cooling)


main()
