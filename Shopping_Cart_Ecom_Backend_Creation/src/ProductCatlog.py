from tabulate import tabulate
from src.Cart import Cart
from src.Payment import Payment

""" This Page shows the Product Catalog and based on the access privilege it shows specific actions:
    If user is Admin then,
        -> Can view the Product catalog
        -> Add item to the catalog
        -> Remove item from the catalog
        -> Update item in the catalog
        
    Else if user is Customer then,
    -> Can view the catalog
    -> Add item to the cart
    -> Remove item from the cart
"""


class ProdCatalog(Cart, Payment):

    def __init__(self):
        super().__init__()
        self.catalog = {
            'prod_Id': [1, 2, 3, 4],
            'prod_Name': ['Boots', 'Coats', 'Caps', 'Pants'],
            'prod_Quant': [5, 4, 10, 12],
            'prod_Price_Per_unit': [200, 500, 100, 300]
        }

        # initialize an empty cart
        self.cart = {}

    def viewCatalog(self):
        return self.catalog

    def addToCatalog(self, **kwargs):

        for key in kwargs.keys():
            self.catalog[key].append(kwargs[key])

        return self.catalog

    def removeFromCatalog(self, prod_Id):
        idx = self.catalog['prod_Id'].index(prod_Id)

        self.catalog['prod_Id'].pop(idx)
        self.catalog['prod_Name'].pop(idx)
        self.catalog['prod_Quant'].pop(idx)
        self.catalog['prod_Price_Per_unit'].pop(idx)

        return self.catalog

    def updateToCatalog(self, prodId, **kwargs):

        # get the index of the product to be updated
        idx = self.catalog['prod_Id'].index(prodId)

        for key in kwargs.keys():
            if kwargs[key] is not None:
                self.catalog[key][idx] = kwargs[key]

        return self.catalog

    #   -------------- Get the user and its action -----------------
    def getUserAndAction(self, userType, userAction, prodId=None, prodName=None, prodQuant=None, prodPrice=None):

        # check userType
        if userAction == 'view':
            print(tabulate(self.catalog, headers='keys', tablefmt='pretty', showindex=False))

        elif userType == 'admin':
            if userAction == 'add':
                self.catalog = self.addToCatalog(prod_Id= prodId, prod_Name=prodName, prod_Quant= prodQuant,
                                                 prod_Price_Per_unit= prodPrice)
                # if flag:
                print(tabulate(self.catalog, headers='keys', tablefmt='pretty', showindex=False))

            elif userAction == 'remove':
                self.catalog = self.removeFromCatalog(prodId)
                print(tabulate(self.catalog, headers='keys', tablefmt='pretty', showindex=False))

            elif userAction == 'update':

                self.catalog = self.updateToCatalog(prodId, prod_Name= prodName, prod_Quant=prodQuant,
                                                    prod_Price_Per_unit=prodPrice)
                print(tabulate(self.catalog, headers='keys', tablefmt='pretty', showindex=False))

        elif userType == 'customer':

            if userAction == 'add':
                print('\n' + "Added to the Cart".center(80) + '\n')
                self.cart = self.addToCart(prodId, prodQuant)
                print(tabulate(self.cart, headers='keys', tablefmt='pretty', showindex=False))

            elif userAction == 'remove':
                print("Remove from the Cart".center(80) + '\n')
                self.cart = self.removeFromCart(prodId, prodQuant)
                print(tabulate(self.cart, headers='keys', tablefmt='pretty', showindex=False))

            elif userAction == 'payment':
                print('\n'+"--*---Payment Page--*--".center(120))
                if len(self.cart):

                    # select payment mode
                    self.getPayment(self.cart)
                else:
                    print("cart is empty...!")

            return self.cart
