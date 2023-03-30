import transaction

trnsct_123 = transaction.Transaction()

username = input("Username: ")
def main_menu():
    print("\n",8*"=","WELCOME TO SUPER CASHIER",8*"=")
    print(2*" ",f"~ Enjoy Your Transaction Mr. {username} ~")
    print("\nPlease select the option")
    print("1. Add new product \n2. Update product \n3. Delete product \n4. Reset transaction \
          \n5. Check order \n6. Check total price \n7. Exit program")
    
    while True:
        try:
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