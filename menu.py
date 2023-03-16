'''You have to run main.py using command python main.py in the terminal and it will run the program without need to run
validation module and cashier module
'''

#import modul yang akan digunakan
import transaction

trnsct_123 = transaction.Transaction()

def main_menu():
    '''create menu for user and use every method in object trnsct_123 
    '''
    print()
    print("=" * 10, "MAIN MENU CASHIER", "=" * 18)
    print(" " * 7, "WELCOME TO SUPER CASHIER\n")
    print("=" * 5, "Please enter one of the option", "=" * 10)
    print("1. Add new product")
    print("2. Update product")
    print("3. Delete product")
    print("4. Reset transaction")
    print("5. Check order")
    print("6. Check total price")
    print("7. Exit")
    
    while True:
        # input pilihan
        try:
            pilihan = input("Choose menu: ")

            # pilihan menu
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
            print("Input according to menu")

main_menu()