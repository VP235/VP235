import time

from src.Cart import Cart
from src.Payment import Payment
from src.ProductCatlog import ProdCatalog

"""
    -> This class is responsible for showing the product catalog to the Admin and Customer.
    -> call the functions and perform respected operation according to the specified user privileges/access.
"""


class Dashboard(ProdCatalog, Cart):

    def __init__(self):
        super().__init__()
        self.userType = None

    def performAdminAction(self, selectedOpt):
        if selectedOpt == '1':
            prod_Id = int(input("Enter Product Id: "))
            prod_Name = input("\nEnter Product Name: ")
            prod_Quant = int(input("\nEnter number of pieces/quantity: "))
            prod_Price = int(input("\nEnter price of the per unit: "))

            if int(prod_Id) in self.catalog['prod_Id'] or prod_Name in self.catalog['prod_Name']:
                print('\nProduct already present in the inventory...Please try update option instead.\n')
            else:
                # call addCatalog method
                self.getUserAndAction(self.userType, 'add', prodId=prod_Id, prodName=prod_Name, prodQuant=prod_Quant,
                                      prodPrice=prod_Price)

        elif selectedOpt == '2':
            prod_Id = int(input("Enter Product Id: "))

            # call removeCatalog method
            self.getUserAndAction(self.userType, 'remove', prodId=prod_Id)

        elif selectedOpt == '3':
            prod_Id = int(input("Enter Product Id: "))

            # ask choice
            choice = input("What would you like to modify (1. Prod Name, 2. Prod Quant, 3. Prod Price)? ")

            if choice == '1':
                name = input("Enter new name for the product: ")

                # call updateCatalog method
                self.getUserAndAction(self.userType, 'update', prodId=prod_Id, prodName=name)

            elif choice == '2':
                quant = int(input("Enter modified quantity for the product: "))

                # call updateCatalog method
                self.getUserAndAction(self.userType, 'update', prodId=prod_Id, prodQuant=quant)

            elif choice == '3':
                price = int(input("Enter modified price per unit for the product: "))

                # call updateCatalog method
                self.getUserAndAction(self.userType, 'update', prodId=prod_Id, prodPrice=price)

        else:
            print("Invalid option is selected...")

    def performCustomerAction(self, selectedOpt):
        if selectedOpt == '1':
            prod_Id = input("\nEnter Product Id (eg, [1, 2, 3]: ")
            prod_Quant = input("\nEnter number of pieces/quantity: ")

            # call addCart method
            self.cart = self.getUserAndAction(self.userType, 'add', prodId=prod_Id.split(','),
                                              prodQuant=prod_Quant.split(','))

        elif selectedOpt == '2':
            # print(self.cart)

            if len(self.cart) != 0:
                choice = input("\n Do you want to remove complete item or reduce the quantity of an item (choose: "
                               "1/2)? ")
                prod_Id = input("Enter Product Id : ")
                if choice == '1':

                    # call removeCart method
                    self.getUserAndAction(self.userType, 'remove', prodId=int(prod_Id))

                elif choice == '2':
                    # call removeCart method
                    prod_Quant = input("\nEnter number of pieces/quantity : ")
                    self.getUserAndAction(self.userType, 'remove', prodId=int(prod_Id), prodQuant=int(prod_Quant))

            else:
                print("Cart is empty... Pleas add items to the cart")
                time.sleep(2)

                print("Add to the cart\n")
                time.sleep(1)
                self.performCustomerAction('1')

    def showDashboard(self):

        print(f'Product Catalog'.center(60))

        self.getUserAndAction(self.userType, 'view')

        # display the dashboard on the basis of userType
        if self.userType == 'admin':
            print(""" \n Admin Dashboard:
            1] Add item to the catalog.
            2] Remove item from the catalog.
            3] Update item in the catalog.
            """)

            selectedOpt = input("What would you like to explore (choose digit) : ".center(20))
            self.performAdminAction(selectedOpt)

        else:
            print(""" \n Customer Dashboard:
            1] Add item to the cart.
            2] Remove item from the cart.
            """)

            selectedOpt = input("What would you like to explore (choose digit) : ".center(20))
            self.performCustomerAction(selectedOpt)

        ask = input("Would you like to continue shopping (y/n)? ")
        if ask.lower() == "y":
            self.showDashboard()

        elif self.userType == 'customer':
            self.getUserAndAction(self.userType, 'payment')

        else:
            print('\n' + 'Thank You...!!'.center(120))
