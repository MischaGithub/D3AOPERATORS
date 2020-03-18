Basic_salary = 1500
Bonus_rate = float(200)
Commission_rate = (0.02)
#Declaring the number of laptops as well as price as a integer
NumofLaptops = int(input("Please enter number of laptops \n"))
PriceOfLaptops = float(input("Please enter the price of the laptops \n"))

#Calculating the Gross Salary Of a Salesman

Bonus = (Bonus_rate * NumofLaptops)
if PriceOfLaptops < Bonus:
    PriceOfLaptops = float(input("Please Enter Price again \n"))

    Commisson = (Commission_rate * NumofLaptops * PriceOfLaptops)
    Gross_Salary = (Basic_salary + Bonus + Commisson)
#Printing the Salary according to the Structure required
    print("The bonus is R", int(Bonus))
    print("The commission is R", int(Commisson))
    print("The gross salary is R", int(Gross_Salary))










