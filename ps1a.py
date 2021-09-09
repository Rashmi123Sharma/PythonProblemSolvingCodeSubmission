#Problem Set 1a
#Name: Rashmi Sharma
#Time Spent : 8hrs



outstand_balance = float(input("Enter the outstanding balance on the credit card"))
annual_int_rate = float(input ("Enter the annual interest rate"))
minimum_month_paymentrt = float(input("Enter the minimum monthly payment rate"))
for month in range(1,13):
    minimum_month_payment= round(( minimum_month_paymentrt*outstand_balance),2)
    intrt_paid = round(((annual_int_rate/12)*outstand_balance), 2)
    prin_paid = round(( minimum_month_payment - intrt_paid),2)
    remain_balance = round(( outstand_balance- prin_paid),2)
    outstand_balance = remain_balance
    month +=1
    print (("Minmimum monthly payment ") + str(minimum_month_payment))
    print (("Principle Paid ") + str(prin_paid))
    print (("Remaining Balance ") + str(remain_balance))
    print ( ("Month")+str (month))
    print (("Remaining Balance")+ str(outstand_balance))
    
    
