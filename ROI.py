class ROI: #Class definition
    def __init__(self,income, expenses, cash_flow,cash_on_cash):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_on_cash = cash_on_cash

    
    #Box 1
    def gather_income(self):
        print("First, we'll find out what sort of income you make from this property")
        rent = int(input("What will you be charging for rent per month at this property?: \n")) #Establishes monthly
        
        income_cont = input("Will you generate any other income from options at this property? Y/N: \n")
        if income_cont.lower() == "y": #Finds other common income scenarios
            print("We'll go line by line for other common income scenarios. If any of these do not apply to you, please input 0:")
            while True:
                try: 
                    laundry = int(input("How much do you expect to make from Laundry?: \n"))
                    storage = int(input("How much do you expect to make from storage: \n"))
                    parking = int(input("How much do you expect to make from parking?: \n"))
                    misc = int(input("How much do you expect to make from any other miscellanous fees?: \n"))
                    other = laundry+storage+parking+misc
                    break
                except ValueError:
                    print("That is not a valid amount. Please try and enter a number")
        else:
            other = 0
        
        self.income = rent+other #totals rent+other items
        print(f"\nYou can expect to receive {self.income} as income from this property each month\n")


    #Box #2
    def gather_expenses(self):
        print("Lets find out a little bit about your expenses\n")
        
        mortgage = input("Do you have a mortgage on this property?: Y/N\n")
        if mortgage.lower() =="y":
            while True:
                try:    
                    principal = int(input("How much of your monthly payment goes toward your principal and interest?\n"))
                    taxes = int(input("How much of that monthly payment is property tax?: \n"))
                    insurance = int(input("How much of that monthly payment is insurance?: \n"))
                    total_mort = principal+taxes+insurance
                    break
                except ValueError:
                    print("That is not a valid amount. Please try and enter a number")
        else:
            total_mort = 0
        
        util = input("Who will be paying for the utilities? You or the tenant?")
        if util.lower() == "me":
            while True:
                try:  
                    water = int(input("Please enter the amount of the monthly water bill: \n"))
                    sewer = int(input("Please enter the amount of the monthly sewer bill: \n"))
                    elec = int(input("Please enter the amount of the monthly electric bill: \n"))
                    garbage = int(input("Please enter the amount of the montly garbage bill: \n"))
                    total_util = water+sewer+elec+garbage
                    break
                except ValueError:
                    print("That is not a valid amount. Please try and enter a number")
        else:
            total_util = 0
        
        options = input("We recommend you budget each month for Vacancy, Repairs, and Capital Expenses. Would you like to do that now?: Y/N")
        if options.lower() == "y":
            while True:
                try:  
                    vacancy = int(input("We recommend a 5% Vacancy budget per month of the rent cost. What percentage would you like to use?\n"))
                    repairs = int(input("What would you like to budget for monthly repair costs?: \n"))
                    capex = int(input("How much are you budgeting per month for capital expenses?: \n"))
                    total_opt = vacancy+repairs+capex
                    break
                except ValueError:
                    print("That is not a valid amount. Please try and enter a number")
        else:
            total_opt = 0
        prop_mgmt = int(input("If you use a property management service, please input their monthly fee here. Else, please put 0: \n"))
        
        total_exp = total_mort+total_util+total_opt+prop_mgmt
        self.expenses = total_exp
        print(f"Your total monthy expenses are {self.expenses}")

    #box 3 - Cash Flow
    def gather_cash_flow(self):
        monthly_cashflow = self.income-self.expenses
        self.cash_flow = monthly_cashflow
        print(f"\nYour monthly cashflow on this property is {self.cash_flow}\n")


    #Box 4 - Cash on Cash - ROI
    def gather_cash_on_cash_roi(self):
        print("Well need a few more parts of information to complete your ROI Summary\n")
        
        down = int(input("How much did you put down towards the property?: \n"))
        closing_costs = int(input("What were your final closing costs?: \n"))
        
        rehab = input("Did you put any additional money towards rehabilitation or renovation? Y/N: \n")
        if rehab.lower() == "y":
            while True:
                try: 
                    rehab_costs = int(input("What were your rehabilitation or renovation costs?: \n"))
                    break
                except ValueError:
                    print("That is not a valid amount. Please try and enter a number")
        else:
            rehab_costs = 0
        other_costs = int(input("If there were any additional one-time costs on this property, please enter them now, otherwise put 0: \n"))
        total_invest = down+closing_costs+rehab_costs+other_costs  
        print(f"Your total investment into this property has been {total_invest}\n")
        #final caclulation of ROI
        yearly_cashflow = self.cash_flow *12
        roi_percentage = yearly_cashflow/total_invest *100
        print(f"Your ROI is {round(roi_percentage)}% \n")

new_property = ROI(0,0,0,0)
def run_program():
    print("Welcome to the Rental Property ROI calculator! \nIn this program, we'll ask you some questions to gather your Return on investment for this property.\n\n")
    while True:
        new_property.gather_income()
        new_property.gather_expenses()
        new_property.gather_cash_flow()
        new_property.gather_cash_on_cash_roi()
        break

run_program()