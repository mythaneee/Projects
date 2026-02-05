# finance_simulator.py (snippet)
# Collaborative development notes:
# - Senior Dev: Gen - Defined the function signature and docstring for clarity.
# - Junior Dev: Myth - Implement the body following the inline comments below.
# - Code Reviewer: Qaced, Crim - Ensure input validation covers all edge cases; add unit tests later.
transactions = []

def add_transact():
    """ Adds new transactions and re-prompts user until they no longer have any."""
    while True:
        category = input("Category: ").strip().lower()
        if len(category) > 0 <= 30:
         break
        print(f"Invalid category: Must be between 1 and 30 characters.")
    
    while True:
        amount = input("Amount: ").strip()
        if amount == "":
             print(f"Invalid amount. Has to be a non-zero number.")
             continue
        try:
            amount = float(amount)  
            if amount != 0:
                break
            print(f"Amount cannot be zero.")
        except ValueError:
            print(f"Please input a numerical value.")

    transactions.append((category, amount))
    print(f"Added: {category.title()} {amount:.2f}")

def view_summary():
    """ Provides the user with a summary of all transactions that are made """

    if not transactions:
          print("No transactions made.")
          return
     
    total_inc = 0.00
    total_exp = {}

    for cat, amt in transactions:
        if amt > 0:
            total_inc += amt
        elif amt < 0:
            if cat in total_exp:
                total_exp[cat] += amt
            else:
                total_exp[cat] = amt
                
    print(f"Summary: ")
    print(f"Income: {total_inc:.2f}")
    print(f"Expenses: ")
    for cat in total_exp:
        print(f"  {cat.title()}: {total_exp[cat]:.2f}")
    net = total_inc + sum(total_exp.values()) if total_exp else total_inc
    print(f" Net: {net:.2f}")

    if net < 0: 
            print(f"Warning: Your balance is negative.")
    elif abs(sum(total_exp.values())) > 0.8 * total_inc and total_inc > 0:
            print(f"Warning: Reaching overspending threshold (80% of income)")
                    
def proj_savings():
     """ Projects users' savings based on the amount they decided on and the duration they invest for """
     while True:
        Princ = input("How much would you like to invest? ").strip()
        if Princ == "":
            print(f"Invalid Principal: Has to be a positive number.")
            continue
        try:
            Princ = float(Princ)
            if Princ > 0:
                break
            print(f"Your principal has to be positive.")
        except ValueError:
            print(f"Invalid Principal: Has to be a number.")

     scen = {"1": 0.03, 
             "3": 0.05, 
             "5": 0.08
             }
     while True:       
        years = input("How many years would you like to invest this amount for (1, 3 or 5): ").strip()
        if years in scen:
            years = int(years)
            rate = scen[years]
            break
        print("Invalid years. Must be 1, 3 or 5.")

     amount = Princ
     for _ in range(years):
      amount *= (1 + rate)

     print(f"Your amount after {years} year{'s' if years > 1 else ''} will be: {amount:.2f}")

     while True:
        retry = input("Try for another Projection?(y/n) ").strip()
        if retry == "y":
            proj_savings()
            return
        elif retry == "n":
            break
        else:
            print("Invalid input. Enter y/n.")

is_running = True
""" main loop """
while is_running:

    print(f"Welcome to your Personal Finance Simulator!")
    print(f"\n1: Add Transaction \n2: View Summary \n3: Project Savings \n4: Quit")

    choice_sel = input("\nEnter choice: ").strip()

    if choice_sel == "1": add_transact()
    elif choice_sel == "2": view_summary()
    elif choice_sel == "3": proj_savings()
    elif choice_sel == "4":  is_running = False; print(f"This session has ended.")    
