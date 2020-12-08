import random
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS card (
    id integer,
    number text,
    pin text,
    balance integer default 0)''')

print(cur.fetchall())
def insert_new_account(id, number, pin, balance):
    with conn:
        cur.execute("insert into card values (:id, :number, :pin, :balance)", {"id": id, "number": number, "pin": pin, "balance": balance})

def modify_balance(card_number, balance, income, type):
    if type == "deposit":
        new_balance = balance + income
    elif type == "withdraw":
        new_balance = balance - income
    with conn:
        cur.execute('UPDATE card SET balance = :balance where number = :number', {"number": card_number, "balance": new_balance})

def delete_account(number):
    with conn:
        cur.execute('DELETE from card where number = :number', {"number": number})

def print_database():
    with conn:
        cur.execute('Select * from card')
        print(cur.fetchall())

def all_card_num():
    with conn:
        cur.execute('Select number from card')
        print(cur.fetchall())
        return cur.fetchall()

def luhn(dig):
    dig = list(map(int, dig))
    for i in range(0, -len(dig) - 1, -1):
        if i % 2 != 0:
            dig[i] = dig[i] * 2
    for i, j in enumerate(dig):
        if j > 9:
            dig[i] = j - 9
    cont_num = sum(dig)
    print(cont_num)
    checksum = str(cont_num * 9)[-1]
    return checksum

# customer = Customer() # a new customer is created every time an account is created

while True:
    checker = 0
    if checker == 1:
        break

    user_inp = int(input("1. Create an account\n2. Log into account\n0. Exit\n", ))

    if user_inp == 1:
        # create customer info
        cus_num = str(random.randint(000000000, 999999999)).zfill(9)
        cus_ping = str(random.randint(0000,9999)).zfill(4)
        temp_num = "400000" + cus_num
        cus_checksum = str(luhn(temp_num))
        card_num = "400000" + cus_num + cus_checksum
        
        balance = 0
        id = 1
        
        insert_new_account(id, card_num, cus_ping, balance)  # this stores into the database
    
        print("Your card has been created")
        print("Your card number:", card_num, sep="\n")
        print("Your card PIN:", cus_ping, sep="\n")

    elif user_inp == 2:
        card_inp = input("Enter your card number:", )
        ping_inp = input("Enter your PIN:", )
        
        cur.execute('select * from card where number = :number', {"number": card_inp})  # this is the row where card number matches
        database_out_1 = cur.fetchone()
        
        cur.execute('select number from card')
        database_all_card_num = cur.fetchall()  # this gives a list of all card number
        
        card_list_total = []
        for i in database_all_card_num:
            card_list_total.append(i[0])

        # if card_inp not in cus_info or customer.info[card_inp] != ping_inp:
        if not database_out_1:
            print("Wrong card number or PIN!")
        
        elif database_out_1:  #fetchone returns None if there's no match so we must first return a row with the matching card number
            if database_out_1[2] != ping_inp:  #list is [id, card number, ping, balance]
                print("Wrong card number or PIN!")
            else:
                print("You have successfully logged in!")
                checker = 0

                while checker == 0:
                    cur.execute('select * from card where number = :number', {"number": card_inp})  # this is the row where card number matches
                    database_out_1 = cur.fetchone()
        
                    cur.execute('select number from card')
                    database_all_card_num = cur.fetchall()  # this gives a list of all card number
        
                    card_list_total = []
                    for i in database_all_card_num:
                        card_list_total.append(i[0])

                    user_inp_2 = int(input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n6. Exit", ))
                    
                    if user_inp_2 == 1:
                        print("Balance:", database_out_1[3])

                    elif user_inp_2 == 2:
                        income = int(input("Enter income:", ))
                        modify_balance(card_inp, database_out_1[3], income, "deposit")
                        print("Income was added!")

                    elif user_inp_2 == 3:
                        new_card = input()
                        cur.execute('Select * from card where number = :number', {"number": new_card})
                        card_num_temp = cur.fetchone()

                        if luhn(new_card[:-1]) != new_card[-1]:
                            print("Probably you made a mistake in the card number. Please try again!")
                        elif new_card not in card_list_total:
                            print("Such a card does not exist.")
                        else:
                            deposit = int(input("Enter how much money you want to transfer:", ))

                            if deposit > database_out_1[3]:
                                print("Not enough money!")
                            else:
                                modify_balance(card_inp, database_out_1[3], deposit, "withdraw")
                                modify_balance(new_card, card_num_temp[3], deposit, "deposit" )
                                print("Success!")

                    elif user_inp_2 == 4:
                        delete_account(card_inp)
                        print("The account has been closed!")

                    elif user_inp_2 == 5:
                        print("You have successfully logged out!")
                        checker = 1

                    elif user_inp_2 == 0:
                        checker = 2
            if checker == 2:
                break

    elif user_inp == 0:
        break

conn.close()
