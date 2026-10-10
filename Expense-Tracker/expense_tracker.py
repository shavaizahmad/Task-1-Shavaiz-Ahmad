total_amount = 0
total_spend = 0
total_remaining = 0
while True:
    print("\n=======Your Expense Track=======")
    print("1- Add Money : ")
    print("2- Add Expenses : ")
    print("3- View Balance : ")
    print("4- Exit : ")

    try:
       choice = int(input("\nEnter Your Choice : "))
    except ValueError:
        print("Please Enter valid number")
        continue

    if(choice == 1):
        print("\nAdd Money in your Account Balance\n")

        try:
           new_total = int(input(f"How much amount add to your current balance- {total_amount}? : "))
        except ValueError:
           print("Please Enter valid number")
           continue
        
        total_amount +=new_total
        print(f"{new_total} amount is added to your account balance and now Net balance is = {total_amount}")
   
    elif(choice == 2):
        print("\n-------------Add an Expenses---------------")

        try:
            expense = int(input(f"How much you spend from your balance {total_amount}? : "))
        except ValueError:
            print("Please Enter valid number")
            continue

        if(expense > total_amount):
           print("\nExceed your Expense, Warning!")
           continue
        else:
            total_amount -= expense
            total_spend += expense
            print(f"you spend {total_spend} and your current balance is {total_amount} ")

    elif(choice == 3):
        print("---------View Your Account Balance---------")
        print(f"Your spend amount is = {total_spend}")
        print(f"your Total Balance is = {total_amount}")

    elif(choice == 4):
        print("\nThanks For Using Expense Tracker")
        break
    
    else:
        print("\nEnter Valid input  1,2,3,4 ")
        continue
        
