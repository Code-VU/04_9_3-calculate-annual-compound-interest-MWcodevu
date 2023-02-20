def calculateCompoundInterest():
    for x in range (3):
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))
        total = round(client_one_principal*(1+client_one_rate / 100)**client_one_time, 2)
        interest = round((total) - client_one_principal, 2)
        print(f"Compound Interest: {interest}")
        if x < 2:
            print("---")
if __name__ == "__main__":
    calculateCompoundInterest()