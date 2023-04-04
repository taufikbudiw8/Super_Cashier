## **SUPER CASHIER PROJECT**
___
Super cashier is a project which is the implementation of OOP and CRUD in fundamental python programming. 
___
### **Background and Goals of The Project**
It started with market owner who is upgrading his business. This owner wants an update to the market transaction system, so that users could do and experience of transaction by themselves anytime and anywhere, and we can call it as self-service cashier system.

Goals from super cashier project is to be able to create a simple and useful methods for customer to do transactions by themselves.
___
### **Code Short Explanation:**
#### -  Attributes
In this project, the instance attribute is used for initialize the data on the class, in this case `.items` would be initialized as a dictionary.

#### -  Method
In this super cashier project, there are using several methods for better transaction experience, that is:
1. `add_item`
Adding the items to the dictionary that consist of name, quantity, and price of the product. Because the class that it used was a dictionary type, so the name of product would be the ‘key’ and others would be the ‘value’.
2. `update_item`
As a form of updating the name/quantity/price of the product that have been added to the dictionary before.
3. `delete_item`
Delete products based on their names for products that have been added to the dictionary.
4. `reset_item`
Delete all products that have been added to the dictionary regardless of product name, quantity, price.
5. `show_order`
Displays all names, quantities, prices of products that have been added before. The total price of each product will be displayed too.
6. `total_price`
Calculate the total price of the products in the dictionary and also calculate the discount you get. So that the total initial price, discount, and final price will be displayed.
7. `menu`
Displays menu functions to make it easier for customers to do self-service.

#### -  Notes
Conditions for discounts based on project guidance,
1. If above IDR 200,000 a discount of 5%
2. If above IDR 300,000 a discount of 8%
3. If above IDR 500,000 a discount of 10%
___
#### **Flowchart**
This flowchart illustrates how the program works during the transactions.
![Flowcharts - Algorithm flowchart example](https://user-images.githubusercontent.com/124851791/228711908-37a29a89-95c3-4750-a877-0cbd54ebd9ae.png)
___
### **Program Demonstration**
Start the `menu`
![menu](https://user-images.githubusercontent.com/124851791/229718154-1e412c7d-3f4d-4146-9229-4657e0342734.png)

1. Test Case 1: `add_item`
![add_item](https://user-images.githubusercontent.com/124851791/229718244-bdc1a1ea-e33e-4f80-aa14-b9e9b25abe9f.png)
Ae can see, there will be additional products in the dictionary(cart). 
![check_order(add)](https://user-images.githubusercontent.com/124851791/229718430-f740a7d3-6390-4f0c-b4c9-8978f885441e.png)

2. Test Case 2: `update_item`
![update](https://user-images.githubusercontent.com/124851791/229718722-4e464d45-e7d5-475a-81a6-4231dd2aabab.png)
As we can see, there will be a change in the initial product to a new product in the dictionary(cart)
![check_order(update)](https://user-images.githubusercontent.com/124851791/229718974-570ac83b-b320-40c9-96ee-941e48305831.png)

3. Test Case 3: `delete_item`
![delete_item](https://user-images.githubusercontent.com/124851791/229719019-181e353f-db48-419d-9116-322765621db8.png)
As we can see, product Pasta Gigi will be deleted from the dictionary(cart)
![check_order(delete)](https://user-images.githubusercontent.com/124851791/229719303-caa7b62e-21ec-4097-adf0-d1299404caed.png)

4. Test Case 4: `reset_item`
After we delete all of product from the dictionary(cart), there will be no more products when we check it
![reset](https://user-images.githubusercontent.com/124851791/229719364-8caec9d8-178e-4528-85b5-a1a92e3498d0.png)

5. Test Case 6: `total_price`
![total_price](https://user-images.githubusercontent.com/124851791/229719920-bc908843-40a9-4ad7-ad59-6c62ab41f790.png)

`Exit` from the program.

---
### **Future Expectation**
1. Changing the system appearance for better customer experience.
2. More additional and complicated methods for the transaction.
3. Product/ Item ID maybe usefull for big scale of transaction
