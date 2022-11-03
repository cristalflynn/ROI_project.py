def main():
    income = Income()
    expenses = Expenses()  
    initial_costs = Initial_costs() 
    total_income = income.total()
    total_expenses = expenses.total()
    total_cashflow = cashflow(total_income, total_expenses)
    total_investment = initial_costs.total()
    print(float(return_investment(total_cashflow, total_investment)))

def cashflow(income, expenses):
    return income - expenses

def return_investment(total_cashflow, total_investment):
    annual_cashflow = total_cashflow * 12
    return annual_cashflow / total_investment

class Initial_costs():
    def __init__(self):
        self.down_payment =  int(input("Enter your Down Payment amount: "))
        self.closing_costs =  int(input("Enter your Closing Costs amount: "))
        self.repair =  int(input("Enter your Repair amount: "))
        self.other =  int(input("Enter your Other amount: "))

    def total(self):
        total = self.down_payment + self.closing_costs + self.repair + self.other
        return total

class Income():
    def __init__(self):

        self.rent = int(input("Enter your Rent amount: "))
        self.laundry = int(input("Enter your Laundry amount: "))
        self.storage = int(input("Enter your Storage amount: "))
        self.misc = int(input("Enter your MISC amount: "))

    def total(self):
        total = self.rent + self.laundry + self.storage + self.misc
        return total


class Expenses():
    def __init__(self):

        self.tax = int(input("Enter your Tax amount: "))
        self.insurance = int(input("Enter your Insurance amount: "))
        self.utilities = int(input("Enter your Utilities amount: "))
        self.hoa = int(input("Enter your HOA amount: "))
        self.lawn = int(input("Enter your Lawn/Snow amount: "))
        self.vacancy = int(input("Enter your Vacancy amount: "))
        self.repair = int(input("Enter your Repair amount: "))
        self.capex = int(input("Enter your Capex amount: "))
        self.property_managment = int(input("Enter your Property Managment amount: "))
        self.mortgage = int(input("Enter your Mortgage amount: "))
    
    def total(self):
        total = self.tax + self.insurance + self.utilities + self.hoa + self.lawn + self.vacancy + self.repair + self.capex + self.property_managment + self.mortgage
        return total

if __name__ == "__main__":
    main()