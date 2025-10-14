rent = int(input("Enter your total flat rent: "))
condom = int(input("Enter your total money spent on condoms: ")) 
subscriptions = int(input("Enter your total amount spent on subscriptions: "))
food = int(input("Enter your total food order amount: "))
electricity_bill = int(input("Enter your total electricity units: "))
per_unit_charge = int(input("Enter your per-unit charge: "))  
persons = int(input("How many people to divide the cost among: "))

total_bill = electricity_bill * per_unit_charge
total_expenses = rent + condom + subscriptions + food + total_bill
output = total_expenses / persons

print(f"Each person should pay = {output:.2f}")
