import argparse
import math

def find_num_months(principal, month_pay, interest):
    P = int(principal)
    A = float(month_pay)
    i = float(interest) / 1200
    result = math.ceil(math.log((A / (A - i * P)), (i + 1)))
    result_years = result // 12
    result_months = result % 12
    overpayment = month_pay * result - principal
    if result_years == 0:
        print(f"It will take {result_months} months to repay the loan")
    elif result_months != 0:
        print(f"It will take {result_years} years and {result_months} months to repay the loan!")
    else:
        print(f"It will take {result_years} years to repay the loan!")
    print("Overpayment =", int(overpayment))

def find_monthly(principal, periods, interest):
    P = int(principal)
    n = int(periods)
    i = float(interest) / 1200
    temp = (1 + i) ** n
    A = math.ceil(P * ((i * temp) / (temp - 1)))
    overpayment = A * periods - principal
    print(f"Your monthly payment = {A}!")
    print("Overpayment =", int(overpayment))

def find_prin(month_pay, periods, interest):
    A = float(month_pay)
    n = int(periods)
    i = float(interest) / 1200
    temp = (1 + i) ** n
    P = math.floor(A / ((i * temp) / (temp - 1)))
    overpayment = month_pay * periods - P
    print(f"Your loan principal = {P}!")
    print("Overpayment =", int(overpayment))

def find_difpay(principal, periods, interest):
    overpayment = 0
    P = int(principal)
    n = int(periods)
    i = float(interest) / 1200
    for m in range(1, n + 1):
        D_m = math.ceil(P / n + i * (P - (P * (m - 1)) / n))
        overpayment = overpayment + (D_m - (principal / periods))
        print(f"Month {m}: payment is {D_m}")
    print("Overpayment =", int(overpayment))

def find_overpayment(principal, periods, interest):
    P = int(principal)
    n = int(periods)
    i = float(interest) / 1200
    
    return

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="diff vs annuity", choices=["annuity", "diff"])
    parser.add_argument("--payment", help="monthly payment amount", type=float)
    parser.add_argument("--principal", help="principal", type=int)
    parser.add_argument("--periods", help="periods", type=int)
    parser.add_argument("--interest", help="interest percent", type=float)
    args = parser.parse_args()  # this puts all of the arguments into a namespace
    # incorrect parameter 1 - 
    if args.type == None:
        print("Incorrect Parameters")
    elif args.type == "diff" and args.payment != None:
        print("Incorrect Parameters")
    elif args.principal and args.principal < 0:
        print("Incorrect Parameters")
    elif args.periods and args.periods < 0:
        print("Incorrect Parameters")
    elif args.interest and args.interest < 0:
        print("incorrect Parameters")
    elif args.type == "diff" and args.principal and args.periods and args.interest:
        find_difpay(args.principal, args.periods, args.interest)
    else:  # args.type = "annuity"
        if args.interest == None:
            print("Incorrect Parameters")
        elif args.payment == None and args.principal != None and args.periods != None and args.interest != None:
            find_monthly(args.principal, args.periods, args.interest)
        elif args.principal == None and args.payment != None and args.periods != None and args.interest != None:
            find_prin(args.payment, args.periods, args.interest)
        elif args.periods == None and args.principal != None and args.payment != None and args.interest != None:
            find_num_months(args.principal, args.payment, args.interest)
    
if __name__ == "__main__":
    Main()
