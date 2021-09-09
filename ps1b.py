#Problem Set 1b
#Name: Rashmi Sharma
#Time Spent : 3hrs



outstand_balance = float(input("Enter the outstanding balance on your credit card"))
annual_int_rate=float(input("Enter the annual credit card interest rate as a decimal"))

minmum_monthly_payment= .05*outstand_balance
outstand_balance=outstand_balance
while outstand_balance>=0:
    month=1
    minmum_monthly_payment=minmum_monthly_payment+500
    outstand_balance=outstand_balance

    while month<=12 and outstand_balance>0:
        month=month+1
        monthly_interest_rate=annual_int_rate/12.0
        outstand_balance=outstand_balance*(1+monthly_interest_rate)-minmum_monthly_payment
print("RESULT")
print("Monthly payment to pay off debt in 1 year:",minmum_monthly_payment)
print("Number of months needed:",month)
print("Balance:",outstand_balance)
