import time
from tabulate import tabulate
import random
import uuid

"""
This class is responsible for:
    -> generating invoice with calculation of total amount to be paid by the customer.
    -> showing different payment gateway methods and taking the response.
    -> redirecting to bill payment
    -> ask customer to pay the bill and validate the amount paid by the customer:
        -> if valid amount is paid by the customer, then display order placed msg with generated orderId and tracking Id.
        -> else, if invalid amount is paid then redirect the customer back to payment gateway method and ask customer to do the re-payment.
"""


class Payment:

    def __init__(self):
        self.cart = None

    def generateInvoice(self):

        print('\n\n' + '---*----Generated Invoice---*-----'.center(80))

        #         print(self.cart)

        total_amount = sum(self.cart['tot_price'])
        print(f'\nTotal Amount to be paid: Rs.{total_amount}/-')

        print(tabulate(self.cart, headers='keys', tablefmt='pretty', showindex=False))

        return total_amount

    @staticmethod
    def showPaymentOption():

        print("""\n\n Please select a payment option: \n 
        1] Net banking
        2] PayPal
        3] UPI
        4] Credit Card
        5] Debit Card
        6] Amex Card
        7] Cash On Delivery""")

        cutomersOpt = input("\nChoose the payment mode(choose the number): ")

        time.sleep(2)
        amount = input("\nEnter the amount to be paid: ")

        return amount

    def validatePayment(self, paid_amnt, total_amt):

        # check if amount paid by customer is what the total amount to be paid
        if int(paid_amnt) == int(total_amt):

            # generate order Id
            order_Id = random.randint(1000, 10000)
            # generate tracking Number
            trace_Id = str(uuid.uuid4())

            print(
                f"\nYour order with orderId= {order_Id} is successfully placed..!!..for tracking the order status use "
                f"tracking Id :{trace_Id}\n")

            print("Thank You! for shopping with us...".center(120))

        # if the paid amount and amount to be paid does not match than redirect back to payment page
        else:
            print("\nInvalid amount is given, redirecting back to payment page....")

            time.sleep(3)
            paid_amnt = self.showPaymentOption()

            time.sleep(2)
            self.validatePayment(paid_amnt, total_amt)

    #         return True

    def getPayment(self, cart):
        self.cart = cart

        # show the invoice to the customer
        total_amount = self.generateInvoice()

        time.sleep(1)

        # redirect the customer to payment gateway page
        print(
            f"\n\n You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs.{total_amount}")

        time.sleep(3)
        # show the payment options
        paid_amnt = self.showPaymentOption()

        time.sleep(2)
        # validate the paid amount and total amount to be paid
        self.validatePayment(paid_amnt, total_amount)

# pay = Payment()
# cart = {
#             'prod_Id': [1, 3],
#             'prod_Name': ['Boots', 'Caps'],
#             'prod_Quant': [5, 4],
#             'prod_Price_Per_unit': [200, 100],
#             'tot_price': [1000, 400]
#            }
# pay.getPayment(cart)
