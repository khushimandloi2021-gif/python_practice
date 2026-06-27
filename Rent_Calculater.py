# project about rent calculator

Total_rent = int(input("enter total rent: "))

units_spent = int(input("enter total electricity units spent: "))

charge_per_unit = int(input("enter electricity charge per unit: "))
cook_spent = int(input("enter the cook charge of the /month: "))
D_mart_grocery = int(input("enter the grocery charge of the /month: "))
num_persons = int(input("enter number of person total divide the amount: "))
total_electricity_bill = units_spent * charge_per_unit
output = (Total_rent + total_electricity_bill + cook_spent + D_mart_grocery)/num_persons

#each_will_pay = total_amount/num_persons



print(f"each will pay {output}")







