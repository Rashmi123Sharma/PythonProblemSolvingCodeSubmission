#Problem Set 1c
#Name: Rashmi Sharma
#Time Spent : 2hrs



outstand_balance = float(input("Enter the outstanding balance on the credit card: "))
annual_int_rate = float(input("Enter the annual interest rate as a decimal: "))
monthly_interest_rt = annual_int_rate/12.0
low = outstand_balance/12.0
high = (outstand_balance * ((1.0 + monthly_interest_rt)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, outstand_balance, minPay, monthly_interest_rt):
    while month <12:
        unpaid_balance = outstand_balance - minPay
        outstand_balance = unpaid_balance + (monthly_interest_rt * unpaid_balance)
        month += 1
        return outstand_balance
    while abs(outstand_balance) >= epsilon:
     outstand_balance = initbalance
     month = 0
     outstand_balance = calculate(month, balance, minPay, monthly_interest_rt)
    if outstand_balance > 0:
            low = minPay
    else:
                high = minPay
                minPay = (high + low)/2.0
                minPay = round(minPay,2)
                print('Lowest Payment: ' + str(minPay))
