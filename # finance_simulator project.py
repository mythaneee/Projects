# finance_simulator.py (snippet)
# Collaborative development notes:
# - Senior Dev: Gen - Defined the function signature and docstring for clarity.
# - Junior Dev: Myth - Implement the body following the inline comments below.
# - Code Reviewer: Qaced, Crim - Ensure input validation covers all edge cases; add unit tests later.
transactions = []

def add_transact ():
    """ Adds new transactions and re-prompts user until they no longer have any."""
    try: 
        category = input("Category: ").strip().lower()
        assert len(category) <= 30 and len(category) > 3
    except AssertionError:
        print(f"Invalid, please enter not more than 30 and more than 5 letters."); return {category}
    
    try:
        amount = input("Amount: ").strip()
        amount = float(amount)
    except ValueError:
        print(f"Please input a numerical value."); return {amount}

    if amount > 0.00 and amount != 0.00:
            print(f"Added.")
                            
    elif amount < 0:
            print(f"Added.")         

    data = (category, amount)
    transaction = tuple(data)
    transactions.append(transaction)

def view_summary():
     """ Provides the user with a summary of all transactions that are made """

     if not transactions:
          print("No transactions made.")
          return
     total_inc = 0.00
     total_exp = 0.00
     print(f"Summary: ")
     for cat, amt in transactions:
          if amt > 0:
               total_inc += amt
               print(f" Income: {total_inc:.2f}")
          elif amt < 0:
               total_exp += amt
               print(f" Expenses: {cat}   {total_exp:.2f}")
     net = total_inc + total_exp
    
     print(f" Net: {net:.2f}")
     if net < 0: 
          print(f"You are approaching your spending limit for this period.")
               
def proj_savings():
     """ Projects users' savings based on the amount they decided on and the duration they invest for """
     Princ = input("How much would you like to invest? ").strip()
     years = input("How many years would you like to invest this amount for (1, 3 or 5): ").strip()
     rate = 0.00
     found = False

     for option, r in [("1", 0.03), ("3", 0.05), ("5", 0.08)]:
        if years == option:
            rate = r
            found = True
            break

     r = float(rate); n = float(1); t = float(years); P = float(Princ)
     interest = P *((1+r/n)**(n*t))

     print(f"Your amount after {years} year{'s' if len({years}) > 1 else ''} will be: {interest:.2f}")

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
            
    # Responsible for collecting and validating ONE new transaction.
    # Enforces business rules: income > 0, expenses < 0, valid category.
    # Re-prompts on bad input (defensive programming — industry standard).
    # Modifies the transactions list in-place (passed by reference).
    # Business context: This mimics a transaction entry in a banking API endpoint.
    

    # Step 1: Validate and collect category (use while loop for re-prompting)
    # - Prompt user for category string
    # - Check: not empty, length <= 30 (prevent buffer issues)
    # - Normalize: strip whitespace, convert to lowercase for consistency
    # - If invalid: print error and continue loop
    # Why: Categories should be standardized to avoid duplicates in summaries

    # Step 2: Validate and collect amount (use another while loop)
    # - Prompt for amount as string
    # - Try-convert to float; catch ValueError and re-prompt
    # - Enforce: != 0 (no zero transactions)
    # - Note: Sign determines type (positive=income, negative=expense) — no separate type input
    # Why: Defensive against non-numeric input; aligns with double-entry accounting basics

    # Step 3: Append to transactions list
    # - Store as tuple: (category, amount)
    # - No need for type field since sign implies it
    # Why: Keep data structure simple and immutable per entry

    # Step 4: Confirm addition to user
    # - Print formatted message: e.g., "Added: Category → +amount.2f"
    # - Use title() for category display
    # Why: Provides immediate feedback, improves UX in command-line app

    # Edge cases to handle:
    # - Empty string category → re-prompt
    # - Non-float amount (e.g., "abc") → re-prompt
    # - Zero amount → error and re-prompt
    # - Very large/small floats → float handles it, but consider adding abs(amount) < 1e6 check if scaling to production

    # Potential extension (YAGNI for now):
    # - Add date field if we want time-based filtering later
    # - Integrate with logging for audit trail in enterprise version

