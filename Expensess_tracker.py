Expenses = []
while (True):
    print("-----WELCOME TO EXPENSES TRACKER-----")
    print("1. Add Expense ")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4 Exit")


    choice = int(input("Enter Your Choice :"))
    if choice == 1:
        name = input("Enter Expense Name :")
        amount = float(input("Enter The  Amount :"))


        Expenses.append([name, amount])
        print("Expense Added Successfully...!")

    elif choice == 2:
        print("----Your Expenses----")
        for item in Expenses:
            print(f"{item[0]} : Rs. {item[1]}")


    elif choice == 3:
        total = 0
        for item in Expenses:
            total += item [1]


        print("Total Expense : Rs. ", total)

    elif choice == 4:
        print("THANK YOU..! YOU ARE EXITING  EXPENSES TRACKER")
        break

    else:
        print("INVALID CHOICE...! PLEASE TRY AGAIN...!")   

                        









