
#Problem Set 1C

starting_salary=float(input("Enter the starting salary: "))

def best_saving_rate():
    total_cost = 1000000
    down_payment = 0.25*total_cost

    months = 36

    r = 0.04

    semi_annual_raise = 0.07

    bisection_steps = 0

    low,high = 0 , 10000
    mid = (low+high)//2

    def bisection(starting_salary, mid, low, high):
        global best_r
        best_r = mid/10000
        current_savings=0
        for month in range(0,months):
            if month%6==0 and month != 0:
                starting_salary+=(starting_salary*semi_annual_raise)
            current_savings+=current_savings*r/12
            current_savings+=(starting_salary*best_r/12)
        return current_savings

    current_savings =  bisection(starting_salary, mid, low, high)

    if  bisection(starting_salary,high,low,high) < down_payment + 100:
        print("It is not possible to pay the down payment in three years.")
    elif  bisection(starting_salary,high,low,high) < down_payment - 100:
        print("It is not possible to pay the down payment in three years.")
    else:
        while abs(current_savings - down_payment) > 100 :
            current_savings = bisection(starting_salary, mid, low, high)
            if current_savings < down_payment :
                low = mid
            else :
                high = mid
            mid=(high+low)//2
            bisection_steps+=1
        print("Best savings rate: "+str(best_r))
        print("Steps in bisection search: "+str(bisection_steps))

best_saving_rate()
