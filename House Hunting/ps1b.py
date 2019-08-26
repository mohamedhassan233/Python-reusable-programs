
#Problem Set 1B

def main():
    total_cost=float(input("Enter the cost of your dream home: "))
    portion_down_payment=0.25*total_cost

    current_savings=0.0
    months=1      #months it will take to save up enough money (initialized by 1)

    annual_salary=float(input("Enter your annual salary: "))
    r=0.04

    portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
    monthly_salary=annual_salary/12

    semi_annual_raise=float(input("Enter the semiannual raise, as a decimal: "))

    while (True) :
        current_savings+=current_savings*r/12
        current_savings+=(monthly_salary*portion_saved)
        if months%6 == 0:
            monthly_salary=monthly_salary+(semi_annual_raise*monthly_salary)
        if current_savings >= portion_down_payment :
            break
        else :
            months+=1
    print(months)

main()
