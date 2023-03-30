## **SUPER CASHIER PROJECT**
---
Super cashier is a project which is the implementation of OOP and CRUD in fundamental python programming. 
___
### **Background and Goals of The Project**
It started with market owner who is upgrading his business. This owner wants an update to the market transaction system, so that users could do and experience of transaction by themselves anytime and anywhere, and we can call it as self-service cashier system.

Goals from super cashier project is to be able to create a simple and useful methods also functions for customer to do transactions by themselves.

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
   i. If above IDR 200,000 a discount of 5%
  ii. If above IDR 300,000 a discount of 8%
 iii. If above IDR 500,000 a discount of 10%
---
#### **Flowchart**
This flowchart illustrates how the program works during the transactions.
Flowcharts - Algorithm flowchart example.png
---
### **Program Demonstration**
Start the `menu`
1. Test Case 1: `add_item`
2. Test Case 2: `update_item`
3. Test Case 3: `delete_item`
4. Test Case 4: `reset_item`
5. Test Case 5: `show_order`
6. Test Case 6: `total_price`
Exit from the program.
---
### **Future Expectation**
1. Changing the system appearance for better customer experience.
2. More additional and complicated methods for the transaction.