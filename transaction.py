'''
This module contains few method that will be run in module menu.py,
using simple OOP to make this module(optional), 
and using the implementation of "try-except".
'''
#import library that will be used for the functions below
from tabulate import tabulate

class Transaction:
    '''
    Create class Transaction for initialize while makes method,
    and I used implementation of dictionary.
    '''

    #initialize the method
    def __init__(self):
        self.items = {}
    
    #add_item method used for adding some product to the dictionary(cart)
    def add_item(self):
        #looping for input some product in one time
        while True:
            try:
                #input area
                product = input('Enter product name: ')
                price = int(input('Enter product price: '))
                quantity = int(input('Enter product quantity: '))
            
                #validation/checking area
                if product in self.items:
                    raise ValueError(f"Don't input {product} twice!")
                elif price < 0:
                    raise ValueError("Price value can't be negative")
                elif quantity < 0:
                    raise ValueError("Quantity value can't be negative")
            
                #add_item logic
                self.items[product] = {
                    'quantity': quantity,
                    'price': price,
                    'total_price' : quantity * price
                    }
                print('Product successfully added!')

                #yes no question for add any product again
                while True:
                    yn = input("Are you wanna add any product? (y/n): ")
                    if yn == 'y':
                        break
                    elif yn == 'n':
                        print('Your product successfully added')
                        return
                    else:
                        continue      
            except Exception as e:
                print(e)

    #delete_item method used for deleting product from dictionary(cart) based on product's name
    def delete_item(self):
        #looping for delete some product in one time
        while True:
            try:
                #input area
                product = input('Enter product name you want to delete: ')

                #validation/checking area
                if product in self.items:
                    del self.items[product]
                    print(f'Successfully delete {product}!')
                    pass
                else:
                    raise KeyError
                
                #yes no question for delete any product again
                while True:
                    yn = input("Are you wanna delete any product? (y/n): ")
                    if yn == 'y':
                        break
                    elif yn == 'n':
                        print('Your product successfully deleted')
                        return
                    else:
                        continue
            except KeyError:
                print(f'There is no {product} in dictionary')
    
    #reset_item method used for delete all product in dictionary(cart)
    def reset_item(self):
        try:
            #check amount products in dictionary(cart)
            if len(self.items) != 0:
                self.items.clear()
                print('All product successfully delete!')
            else:
                #if no product it will raise syntax 'ValueError'
                raise ValueError
        except ValueError:
            print('There is empty transaction, please add item first!')

    #update_item method used for update the product's name/quantity/price
    def update_item(self):
        #looping for updating product in one time
        while True:
            #check amount products in dictionary(cart)
            if len(self.items) != 0:
                choose = input('\nChoose update \n1. name \n2. quantity \n3. price \nEnter the number: ')
                
                #update product's name area
                if choose == '1':
                    try:
                        #input area
                        product = input('Enter product that you wanna to update: ')
                        update = input('Enter new product name: ')
                        #update product's name logic
                        if product in self.items:
                            self.items[update] = self.items.pop(product)
                            pass
                        else:
                            raise KeyError
                    except KeyError:
                        print(f"There's no {product} in transaction")
                        continue
            
                #update product's quantity
                elif choose == '2':
                    try:
                        #input product's name first for checking
                        product = input('Enter product that you wanna to update: ')
                        #update product's quantity logic
                        if product in self.items:
                            #input last product's quantity after checking its name
                            quantity = int(input('Enter new quantity of the product: '))
                            if quantity > 0 and int:
                                self.items[product]['quantity'] = quantity
                            else:
                                raise ValueError
                        else:
                            raise KeyError
                    except KeyError:
                        print(f"There's no {product} in transaction")
                    except ValueError:
                        print("Please input quantity correctly!")

                #update product's price
                elif choose == '3':
                    try:
                        #input product's name first for checking
                        product = input('Enter product that you wanna to update: ')
                        #update product's price logic
                        if product in self.items:
                            #input last product's price after checking its name
                            price = int(input('Enter new price of the product '))
                            if price > 0 and int:
                                self.items[product]['price'] = price
                            else:
                                raise ValueError
                        else:
                            raise KeyError
                    except KeyError:
                        print(f"There's no {product} in transaction")
                    except ValueError:
                        print("Please input price correctly!")
                else:
                    continue

                #yes no question for any update again
                while True:
                    yn = input("Are you wanna do any update? (y/n): ")
                    if yn == 'y':
                        break
                    elif yn == 'n':
                        print('Your product successfully updated')
                        return
                    else:
                        continue
            else:
                print('Please add product first!')
    
    #check_order method used for displaying products in dictionary(cart) in form of a table
    def check_order(self):
            #declare list_order that will contain headers and rows
            list_order = []
            #header area
            headers = ['No', 'Product', 'Quantities', 'Price/Product', 'Total Price']
            list_order.append(headers)
            
            #rows area
            n = 0
            for key, _ in self.items.items():
                n += 1
                table_no = n
                product = key
                quantity = self.items[key]['quantity']
                price = self.items[key]['price']
                total_price = self.items[key]['total_price']
                rows = [table_no, product, quantity, price, total_price]
                list_order.append(rows)
            
            #table logic for displaying the product
            if len(self.items) != 0:
                print(tabulate(list_order, tablefmt="fancy_grid"))
            else:
                print('Empty cart, Please add product first!')
    
    #total_price method used for calculating the total price to be paid of
    def total_price(self):
        #total_price logic
        total_price = 0
        for keys, _ in self.items.items():
            total_price += (self.items[keys]['total_price'])
        
        #requirements for the discount
        discount = 0
        if total_price > 200_000 and total_price <= 300_000:
            discount = 0.05
        elif total_price > 300_000 and total_price <= 500_000:
            discount = 0.08
        elif total_price > 500_000:
            discount = 0.1
        else:
            total_price = total_price
        
        print(f"Your initial price is Rp. {total_price:.0f},-")
        print(f"You got discount {(discount*100):.0f}% and your total price become Rp. {(total_price-(total_price*discount)):.0f},-")
            