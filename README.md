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
<img width="390" alt="flow" src="https://user-images.githubusercontent.com/124851791/229742483-8e33ac6e-8b48-4a0a-9c4c-7d154adc8c98.png">
___
### **Program Demonstration**
Start the `menu`

Don't forget to input your nickname first
<img width="244" alt="menu" src="https://user-images.githubusercontent.com/124851791/229741178-363fd0dc-4a3b-411b-b8fe-806c33b071c2.png">

1. Test Case 1: `add_item`
<img width="247" alt="add_item" src="https://user-images.githubusercontent.com/124851791/229740066-fa650e39-245e-4262-9a43-4b12b44575ec.png">
As we can see, there will be additional products in the dictionary(cart). 
<img width="354" alt="check_order(add)" src="https://user-images.githubusercontent.com/124851791/229740152-9a20dbe8-aae1-4e14-ba33-d6bc687cbae1.png">

2. Test Case 2: `update_item`
<img width="289" alt="update" src="https://user-images.githubusercontent.com/124851791/229740469-52179b22-8a15-4342-ba8b-e149b69da806.png">
<img width="296" alt="update2" src="https://user-images.githubusercontent.com/124851791/229740495-b4442787-ae51-421a-8258-22ae6b66380d.png">
As we can see, there will be a change in the initial product to a new product in the dictionary(cart)
<img width="362" alt="check_order(update)" src="https://user-images.githubusercontent.com/124851791/229735588-b1eaea15-9dda-483b-b57a-9dae886fc02e.png">

3. Test Case 3: `delete_item`
<img width="276" alt="delete_item" src="https://user-images.githubusercontent.com/124851791/229740568-de9a0a5c-26ab-4222-a675-e8bcb7e363e0.png">
As we can see, product Pasta Gigi will be deleted from the dictionary(cart)
<img width="356" alt="check_order(delete)" src="https://user-images.githubusercontent.com/124851791/229740595-51a197a7-9daf-4b82-a44c-dddddfa31ce0.png">

4. Test Case 4: `reset_item`
After we delete all of product from the dictionary(cart), there will be no more products when we check it
<img width="244" alt="reset" src="https://user-images.githubusercontent.com/124851791/229740645-f659a9d0-08da-4a17-9fcb-5f4a45678c9c.png">

5. Test Case 6: `total_price`

Before `update_item`
<img width="332" alt="total_price" src="https://user-images.githubusercontent.com/124851791/229740957-59658b63-14d1-4fb8-8983-13f673ac409e.png">

After `update_item`
<img width="338" alt="total price after update" src="https://user-images.githubusercontent.com/124851791/229741034-48ad5643-0f4f-45b3-911d-8d2b9b6d1df1.png">

`Exit` from the program.

---
### **Future Expectation**
1. Changing the system appearance for better customer experience.
2. More additional and complicated methods for the transaction.
3. Product/ Item ID maybe usefull for big scale of transaction
