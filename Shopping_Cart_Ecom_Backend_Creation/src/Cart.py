""" This Page performs action on the cart based on the Customers input:
    1] If Customer wants to add item to the cart:
        -> fetch the idx of the product from the product catalog
        -> check if the Product Quantity of the specified product is in the stock or not, if yes:
            -> check if cart is empty or not, if yes, create first entry in the cart
            -> else,  if cart is not empty, check if the product already exist in the cart, if yes update the existing row
               with modified quant and price
            -> else, if it does not already exist, then create new entry for the product in the cart
        -> check the difference between the quantity of prod present in inventory and quant of prod requested by the customer
        -> if item out of stock, update the catalog and cart with valid quant and prices
            -> update the cart prod_quant and prod_price to valid quant and price estimation
            -> update the catalog prod_quant to 0
        -> else, update the catalog prod_quant with calculated difference between product present in the inventory - prod_quant
           requested by customer

      Else, item out of stock, display out of stock msg to the customer

    2] If Customer wants to remove the item from the cart,
        -> check if the cart is not empty (this check is done in Dashboard class directly
            -> if customer wants to remove the complete item from the cart than take the prodId as input and pop the item
            -> else, if customer wants to just reduce the quantity of the product from the cart then fetch the prodId and
               prod count by which the prodQuant will be decreased and then adjust the prices
        -> else, if the cart is empty then ask user to add some item in cart before, this is done by redirecting customer to
           addToCart method
"""


class Cart:

    def __init__(self):
        self.cart = None
        self.catalog = None

    def addToCart(self, prodId, prodQuant):

        for i in range(len(prodId)):
            # get the index of the product to be added to the cart
            idx = self.catalog['prod_Id'].index(int(prodId[i]))

            # if item added in cart is more than present in stock or not, if yes
            if self.catalog['prod_Quant'][idx] > 0:
                # check if cart is empty or not, if yes, create first entry in the cart
                if len(self.cart) == 0:
                    self.cart['prod_Id'] = [int(prodId[i])]
                    self.cart['prod_Name'] = [self.catalog['prod_Name'][idx]]
                    self.cart['prod_Quant'] = [int(prodQuant[i])]
                    self.cart['prod_Price_Per_unit'] = [self.catalog['prod_Price_Per_unit'][idx]]
                    self.cart['tot_price'] = [int(prodQuant[i]) * self.catalog['prod_Price_Per_unit'][idx]]

                # if cart is not empty, check if the product already exist in the cart, if yes update the existing row
                # with modified quant and price
                elif self.catalog['prod_Id'][idx] in self.cart['prod_Id']:
                    self.cart['prod_Quant'][idx] = self.cart['prod_Quant'][idx] + int(prodQuant[i])
                    self.cart['tot_price'][idx] = self.cart['prod_Quant'][idx] * self.catalog['prod_Price_Per_unit'][idx]

                # if it does not already exist, then create new entry for the product in the cart
                else:
                    self.cart['prod_Id'].append(int(prodId[i]))
                    self.cart['prod_Name'].append(self.catalog['prod_Name'][idx])
                    self.cart['prod_Quant'].append(int(prodQuant[i]))
                    self.cart['prod_Price_Per_unit'].append(self.catalog['prod_Price_Per_unit'][idx])
                    self.cart['tot_price'].append(int(prodQuant[i]) * self.catalog['prod_Price_Per_unit'][idx])

                # check the difference between the quantity of prod present in inventory and quant of prod requested by
                # the customer
                update_catalog_quant = self.catalog['prod_Quant'][idx] - int(prodQuant[i])

                # if item out of stock, update the catalog and cart with valid quant and prices
                if update_catalog_quant < 0:

                    in_stock = self.catalog['prod_Quant'][idx]
                    print(f'Only {in_stock} pieces are in stock and are added to the cart, remaining {abs(update_catalog_quant)} are out of stock..!!')

                    # update the cart prod_quant and prod_price to valid quant and price estimation
                    self.cart['prod_Quant'][i] = self.catalog['prod_Quant'][idx]
                    self.cart['tot_price'][i] = self.catalog['prod_Quant'][idx] * self.catalog['prod_Price_Per_unit'][
                        idx]

                    # update the catalog prod_quant to 0
                    self.catalog['prod_Quant'][idx] = 0
                else:
                    # update the catalog prod_quant
                    self.catalog['prod_Quant'][idx] = update_catalog_quant
            else:
                # if item out of stock, display out of stock msg to the customer
                out_stock_item = self.catalog['prod_Name'][idx]
                print(f'{out_stock_item} are out of stocks...!!!')

        #         print(self.cart)
        return self.cart

    def removeFromCart(self,  prodId, prodQuant=None):
        idx = self.cart['prod_Id'].index(prodId)

        if prodQuant is None:
            # remove the complete item from the cart
            self.cart['prod_Id'].pop(idx)
            self.cart['prod_Name'].pop(idx)
            self.cart['prod_Quant'].pop(idx)
            self.cart['prod_Price_Per_unit'].pop(idx)
            self.cart['tot_price'].pop(idx)

        else:
            # remove some specific quantity of the item from the cart
            self.cart['prod_Quant'][idx] = self.cart['prod_Quant'][idx] - prodQuant
            self.cart['tot_price'][idx] = self.cart['prod_Quant'][idx] * self.cart['prod_Price_Per_unit'][idx]

        return self.cart
