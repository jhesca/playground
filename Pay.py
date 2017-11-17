import math

# Calculate gross pay
def gross_pay(hours, pay):
    if hours <=40:
        gross=hours*pay
    elif hours>40:
        gross=(hours*pay)+((hours-40)*(.5*pay))
    else:
        print("Bad hours.")
    return gross
        
user_hours=float(input("How many hours for the week? "))
user_pay=11.25 #pay

#pre-tax deductions
insurance=59.03 #medical/dental insurance
gross=gross_pay(user_hours, user_pay)
four=gross*.03
pretax=gross-insurance-four

taxes=.145*pretax #an average from
netpay=pretax-taxes

#Prints stuff
print("Your gross pay is $%.2f." %gross)
print("Your pay after insurance is $%.2f." %pretax)
print("You will pay $%.2f towards your 401(k)." %four)
print("You will pay about $%.2f in taxes." %taxes)
print("Your net pay will be about $%.2f." %netpay)
