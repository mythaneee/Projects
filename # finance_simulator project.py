# finance_simulator.py (snippet)
# Collaborative development notes:
# - Senior Dev: Gen - Defined the function signature and docstring for clarity.
# - Junior Dev: Myth - Implement the body following the inline comments below.
# - Code Reviewer: Qaced, Crim - Ensure input validation covers all edge cases; add unit tests later.

transaction = []

def rec(t): transaction.append(t)
    """ 
    Adds transactions to the list
    """

def add_transaction (transactions):
      """ 
      Adds new transactions and re-prompts user until they no longer have any. 
      """
    try: 
        what_category = input("Category: ")
        assert len(what_category) <= 30 and len(what_category) > 3
    except AssertionError:
        print(f"Invalid, please enter not more than 30 and more than 5 letters.")
        return {what_category}

    try:
        deposit = input("Amount: ")
        deposit = deposit
        assert deposit.isdigit()
    except ValueError, AssertionError:
        print(f"Please input a numerical value.")
        return {deposit}

    if deposit > "0.00" and deposit != "0.00":
            print(f"Added.")
            rec(f"Income: {deposit}")
                            
    else: 
            print(f"Added.")   
            rec(f"Expenses: {deposit}")  

def view_summary():
    """ 
    Provides the user with a summary of all transactions that are made
    """
     if not transaction:
          print("No transactions made.")
          return
     if transaction != []:
        print(rec(transaction))
        """ 
        TODO: Make a for loop to add and show all transactions made by user 
        """

is_running = True

while is_running:

    print(f"Welcome to your Personal Finance Simulator!")
    print(f"\n1: Add Transaction \n2: View Summary \n3: Project Savings \n4: Quit")

    choice_sel = input("\nEnter choice: ").strip()

    if choice_sel == "1":
        add_transaction(transaction)
        continue

    elif choice_sel == "2":
        view_summary()

    elif choice_sel == "3":
        pass

    elif choice_sel == "4":
        is_running = False
        print(f"This session has ended.")
    
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

