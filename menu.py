'''
This module is used for running transaction module
in form that more customer friendly
'''
#import transaction module
import transaction

#running transaction module
trnsct_123 = transaction.Transaction()

#input customer name first
username = input("Username: ")
#main_menu method used for displaying the option that will help the customer in this transaction
def main_menu():
    print("\n",8*"=","WELCOME TO SUPER CASHIER",8*"=")
    print(2*" ",f"~ Enjoy Your Transaction Mr. {username} ~")
    print("\nPlease select the option")
    print("1. Add new product \n2. Update product \n3. Delete product \n4. Reset transaction \
          \n5. Check order \n6. Check total price \n7. Exit program")
    #looping that used for returning back to menu after using with one transaction method
    while True:
        try:
            #choose the menu logic
            pilihan = input("Choose menu: ")

            if pilihan == '1':
                trnsct_123.add_item()
                main_menu()
            elif pilihan == '2':
                trnsct_123.update_item()
                main_menu()
            elif pilihan == '3':
                trnsct_123.delete_item()
                main_menu()
            elif pilihan == '4':
                trnsct_123.reset_item()
                main_menu()
            elif pilihan == '5':
                trnsct_123.check_order()
                main_menu()
            elif pilihan == '6':
                trnsct_123.total_price()
                main_menu()
            elif pilihan == '7':
                print("Program exit")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Only the options listed in the menu")
            print("Input and choose correctly!")

main_menu()