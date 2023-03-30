from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = {}
    
    def add_item(self):
        while True:
            try:
                product = input('Enter product name: ')
                price = int(input('Enter product price: '))
                quantity = int(input('Enter product quantity: '))
            
                if product in self.items:
                    raise ValueError(f"Don't input {product} twice!")
                elif price < 0:
                    raise ValueError("Price value can't be negative")
                elif quantity < 0:
                    raise ValueError("Quantity value can't be negative")
            
                self.items[product] = {
                    'quantity': quantity,
                    'price': price,
                    'total_price' : quantity * price
                    }
                print('Product successfully added!')

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

    def delete_item(self):
        while True:
            try:
                product = input('Enter product name you want to delete: ')
                if product in self.items:
                    del self.items[product]
                    print(f'Successfully delete {product}!')
                    pass
                else:
                    raise KeyError
                
                while True:
                    yn = input("Are you wanna delete any product? (y/n): ")
                    if yn == 'y':
                        break
                    elif yn == 'n':
                        print('Your product successfully added')
                        return
                    else:
                        continue
            except KeyError:
                print(f'There is no {product} in dictionary')
    
    def reset_item(self):
        try:
            if len(self.items) != 0:
                self.items.clear()
                print('All product successfully delete!')
            else:
                raise ValueError
        except ValueError:
            print('There is empty transaction, please add item first!')

    def update_item(self):
        while True:
            if len(self.items) != 0:
                choose = input('\nChoose update \n1. product \n2. quantity \n3. price \nEnter the number: ')
                if choose == '1':
                    try:
                        product = input('Enter product that you wanna to update: ')
                        update = input('Enter new product name: ')
                        if product in self.items:
                            self.items[update] = self.items.pop(product)
                            pass
                        else:
                            raise KeyError
                    except KeyError:
                        print(f"There's no {product} in transaction")
                        continue
            
                elif choose == '2':
                    try:
                        product = input('Enter product that you wanna to update: ')
                        if product in self.items:
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

                elif choose == '3':
                    try:
                        product = input('Enter product that you wanna to update: ')
                        if product in self.items:
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
    
    def check_order(self):
            list_order = []
            header = ['No', 'Product', 'Quantities', 'Price/Product', 'Total Price']
            list_order.append(header)
            
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
            
            if len(self.items) != 0:
                print(tabulate(list_order, tablefmt="fancy_grid"))
    
    def total_price(self):
        total_price = 0
        for keys, _ in self.items.items():
            total_price += (self.items[keys]['total_price'])
        
        if total_price > 200_000 and total_price <= 300_000:
            discount = 0.05*total_price
        elif total_price > 300_000 and total_price <= 500_000:
            discount = 0.08*total_price
        elif total_price > 500_000:
            discount = 0.1*total_price
        else:
            total_price = total_price
        
        print(f"Your initial price is Rp. {total_price:.0f},-")
        print(f"You got discount {discount*100}% and your total price become Rp. {(total_price-discount):.0f},-")
            