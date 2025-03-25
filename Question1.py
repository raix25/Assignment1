#taxableinc is the user's income 
taxableinc = int (input('Enter your taxable income:'))

#as each taxable income has different rates
if taxableinc <= 40922: 
    rate= 0.505
elif taxableinc <= 81847: 
    rate= 0.915
elif taxableinc <= 150000: 
    rate= 0.1116
elif taxableinc <= 220000: 
    rate= 0.1216
else: 
    rate= 0.1316

#calculating tax amount 
tax_amt= taxableinc * rate 
tax_paid= int(input("Enter the amount of tax that you have aready paid:"))

tax_balance= tax_amt - tax_paid #subtracting the amt that needs to be paid

#lastly tax balance is shown
if tax_balance > 0: 
    print (f"You still owe: ${tax_balance:.2f}")
elif tax_balance < 0:
    print (f"You are entitled to :${tax_balance:.2f}")
else:
    print ("You have no remaining tax balance. ")
