import mysql.connector as c

con = c.connect(host="localhost",
                user="root",
                passwd="1234",
                database="project")
cursor = con.cursor()

print("*" * 65)
print(" " * 25, end='')
print("Bank Management System")
print("*" * 65)

acno = 101

while True:
    choice = int(input("1->Open Account\n2->Cash Withdrawal\n3->Cash Deposit\n4->Account statement\n5->Update Account\n6->Exit\nEnter Your Choice:"))

    if choice == 1:
        name = input("Enter Name of Account Holder: ")
        balance = int(input("Enter Opening Balance: "))
        mob = input("Enter Registered Mobile Number: ")
        query = "INSERT INTO bank VALUES({},'{}',{},'{}')".format(acno, name, balance, mob)
        acno += 1
        cursor.execute(query)
        con.commit()
        print("Account Opened Successfully..")

    elif choice == 2:
        account_number = int(input("Enter Account Number: "))
        withdrawal_amount = int(input("Enter Withdrawal Amount: "))
        query = "SELECT balance FROM bank WHERE acno = {}".format(account_number)
        cursor.execute(query)
        balance = cursor.fetchone()[0]
        if withdrawal_amount <= balance:
            new_balance = balance - withdrawal_amount
            update_query = "UPDATE bank SET balance = {} WHERE acno = {}".format(new_balance, account_number)
            cursor.execute(update_query)
            con.commit()
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    elif choice == 3:
        account_number = int(input("Enter Account Number: "))
        deposit_amount = int(input("Enter Deposit Amount: "))
        query = "SELECT balance FROM bank WHERE acno = {}".format(account_number)
        cursor.execute(query)
        balance = cursor.fetchone()[0]
        new_balance = balance + deposit_amount
        update_query = "UPDATE bank SET balance = {} WHERE acno = {}".format(new_balance, account_number)
        cursor.execute(update_query)
        con.commit()
        print("Deposit Successful.")

    elif choice == 4:
        account_number = int(input("Enter Account Number: "))
        query = "select * from bank where acno = {}".format(account_number)
        cursor.execute(query)
        account_details = cursor.fetchone()
        print("="*65)
        print("Account Number:", account_details[0])
        print("Account Holder Name:", account_details[1])
        print("Balance:", account_details[2])
        print("Mobile Number:", account_details[3])
        print("="*65)
    elif choice == 5:
        account_number = int(input("Enter Account Number: "))
        mob = input("Enter New Mobile Number: ")
        update_query = "UPDATE bank SET mobile_number = '{}' WHERE acno = {}".format(mob, account_number)
        cursor.execute(update_query)
        con.commit()
        print("Account Updated Successfully.")

    elif choice == 6:
        break

    else:
        print("Invalid Choice.")

con.close()
