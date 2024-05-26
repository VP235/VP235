#  Shopping Cart Application

#### 1] Init File:
	Initial File which shows welcome msg, accepts the userType (admin or customer), gets the userName and UserPassword. After getting userName and userPassword triggers Login Page.

#### 2] LoginPage File:
	1] If holds the dummy database containing customer and admin login details
	2] After receiving the userName and userPass from the init page, it validates the login credentials of customer/admin. Once validated successfully it triggers dashboard process, if validation fails than it will display Invalid login error msg. Else, if it’s a new user than a row is added in the database.

#### 3] Dashboard File:
	-> This class is responsible for showing the product catalog to the Admin and Customer.
	-> call the functions and perform respected operation according to the specified user privileges/access.

#### 4] ProductCatalog File:
This Page shows the Product Catalog and based on the access privilege it shows specific actions:

   	If user is Admin then,
        -> Can view the Product catalog
        -> Add item to the catalog
        -> Remove item from the catalog
        -> Update item in the catalog
		
    Else if user is Customer then,
    	-> Can view the catalog
    	-> Add item to the cart
    	-> Remove item from the cart

#### 5] Cart File: 
This Page performs action on the cart based on the Customers input:

    1] If Customer wants to add item to the cart:
        -> fetch the idx of the product from the product catalog
        -> check if the Product Quantity of the specified product is in the stock or not, if yes:
            	i] check if cart is empty or not, if yes, create first entry in the cart
            	ii] else,  if cart is not empty, check if the product already exist in the cart, if yes update the existing row with modified quant and price.
            	iii] else, if it does not already exist, then create new entry for the product in the cart
        -> check the difference between the quantity of prod present in inventory and quant of prod requested by the customer
        -> if item out of stock:
				-> update the catalog and cart with valid quant and prices
            	-> update the cart prod_quant and prod_price to valid quant and price estimation
            	-> update the catalog prod_quant to 0
        -> else, update the catalog prod_quant with calculated difference between product present in the inventory - prod_quant
           requested by customer

      Else, item out of stock, display out of stock msg to the customer

    2] If Customer wants to remove the item from the cart:
        	-> check if the cart is not empty (this check is done in Dashboard class directly
           		-> if customer wants to remove the complete item from the cart than take the prodId as input and pop the item
            	-> else, if customer wants to just reduce the quantity of the product from the cart then fetch the prodId and
               prod count by which the prodQuant will be decreased and then adjust the prices
        -> else, if the cart is empty then ask user to add some item in cart before, this is done by redirecting customer to
           addToCart method

#### 6] Payment File:

	This class is responsible for:
  		-> generating invoice with calculation of total amount to be paid by the customer.
    	-> showing different payment gateway methods and taking the response.
    	-> redirecting to bill payment
    	-> ask customer to pay the bill and validate the amount paid by the customer:
        	-> if valid amount is paid by the customer, then display order placed msg with generated orderId and tracking Id.
       		 -> else, if invalid amount is paid then redirect the customer back to payment gateway method and ask customer to do the re-payment.





