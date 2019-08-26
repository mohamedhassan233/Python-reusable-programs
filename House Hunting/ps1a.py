
#Problem Set 1A

def main():
    total_cost=float(input("Enter the cost of your dream home: "))
    portion_down_payment = 0.25*total_cost

    current_savings = 0.0
    months=1       #months it will take to save up enough money (initialized by 1)


    annual_salary = float(input("Enter your annual salary: "))
    r = 0.04

    portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
    monthly_salary = annual_salary/12

    while(True):
        current_savings+=current_savings*r/12
        current_savings+=(monthly_salary*portion_saved)
        if current_savings >= portion_down_payment:
            break
        else:
            months+=1
    print(months)

main()
