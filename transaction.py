from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = {}
    
    def add_item(self):
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
        except Exception as e:
            print(e)

    def delete_item(self):
        product = input('Enter product name you want to delete: ')
        try:
            del self.items[product]
            print(f'Successfully delete {product}!')
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
        if len(self.items) != 0:
            choose = input('Choose update product/quantity/price: ')
            if choose == 'product':
                try:
                    product = input('Enter product that you wanna to update: ')
                    update = input('Enter new product name: ')
                    if product in self.items:
                        self.items[update] = self.items.pop(product)
                    else:
                        raise ValueError
                except ValueError:
                    print(f"There's no {product} in transaction")
            elif choose == 'quantity':
                try:
                    product = input('Enter product that you wanna to update: ')
                    quantity = int(input('Enter new quantity of the product: '))
                    if product in self.items:
                        self.items[product]['quantity'] = quantity
                    else:
                        raise ValueError
                except ValueError:
                    print(f"There's no {product} in transaction")
            elif choose == 'price':
                try:
                    product = input('Enter product that you wanna to update: ')
                    price = int(input('Enter new price of the product '))
                    if product in self.items:
                        self.items[product]['price'] = price
                    else:
                        raise ValueError
                except ValueError:
                    print(f"There's no {product} in transaction")
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
            