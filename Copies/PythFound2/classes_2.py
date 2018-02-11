#Edit this file to complete the exercises in
#'Extending Class Functionality with Polymorphism and Inheritance'

class CreditCard(object):
    '''
    This class provides a template for a
    personal credit card. It has already been
    completely filled out for you.
    '''

    def __init__(self,name,card_number,apr_percent,limit):
        '''
        Initialize an instance of the class.
        
        Arguments:
        name: The name of the account holder
        card_number: The credit card number
        apr_percent: The APR, as a percentage (i.e. 20
            instead of 0.2 for a 20 percent APR).
        limit: The limit on the card.

        Returns:
        None
    
        Sets the following class attributes:
        name = name argument
        card_number = card_number argument
        apr_percent = apr_percent argument
        limit = limit argument
        balance = 0
        fees = 0
    
        For instance, the command to set the first attribute is:
        self.name = name
        '''
        self.name = name
        self.card_number = card_number
        self.apr_percent = apr_percent
        self.limit = limit
        self.balance = 0
        self.fees = 0

    def make_purchase(self,purchase_price):
        '''
        Take in a purchase dollar amount, make sure it won't put the
        card over limit, and do one of the following:
        1. If under/at limit, add dollar amount to balance and return True
        2. If over limit, return False
    
        Arguments:
        purchase_price: The dollar amount to be charged to the card.
    
        Returns:
        purchase_approved: True if purchase_price + self.balance + self.fees <= self.limit,
            False otherwise.
        '''
        if purchase_price + self.balance + self.fees > self.limit:
            return False
        else:
            self.balance += purchase_price
            return True

    def pay_card(self,payment_amount):
        '''
        Take in the dollar amount of a potential payment to the card,
        verify that the payment is both greater than 0 and is less than or
        equal to the balance + fees, then apply that payment to first any fees
        and then the balance.
    
        Arguments:
        payment_amount: The dollar amount to be paid on the card.
    
        Returns:
        payment_approved: True if payment_amount > 0 and
            payment_amount <= self.balance + self.fees, False otherwise
        '''
        if payment_amount > 0 and payment_amount <= self.balance + self.fees:
            if payment_amount >= self.fees:
                payment_amount -= self.fees
                self.fees = 0
            else:
                self.fees -= payment_amount
                payment_amount = 0
            self.balance -= payment_amount
            return True
        else:
            return False

    def compute_interest(self):
        '''
        Compute the daily interest by dividing the apr_percent by 365,
        summing up the balance and fees, and then multiplying the daily
        percentage by this sum. If the daily interest is greater than zero,
        add it to the balance. Otherwise, do nothing.
    
        Arguments:
        None
    
        Returns:
        None
        '''
        daily_interest_fraction = self.apr_percent/365./100.
        daily_interest = (self.balance + self.fees)*daily_interest_fraction
        if daily_interest > 0:
            self.balance += daily_interest

class VentureCard(CreditCard):
    '''
    A class for the Venture Card, a subclass of CreditCard.
    '''

    #Add an __init__ method to this class that meets the
    #specifications laid out in this docstring:
    '''
    Initialize an instance of this class.

    Arguments:
    name: The name of the account holder
    card_number: The credit card number
    apr_percent: The APR, as a percentage (i.e. 20
        instead of 0.2 for a 20 percent APR).
    limit: The limit on the card.
    points_per_dollar_spent: The amount of points earned per
        dollar spent on the card.

    Returns:
    None

    Sets the following class attributes:
    name = name argument
    card_number = card_number argument
    apr_percent = apr_percent argument
    limit = limit argument
    points_per_dollar_spent = points_per_dollar_spent argument
    balance = 0
    points_balance = 0
    fees = 0
    '''
    def __init__(self,name, card_number, apr_percent, limit, points_per_dollar_spent):
        self.points_per_dollar_spent=points_per_dollar_spent
        self.points_balance=0
        super(VentureCard,self).__init__(name, card_number, apr_percent, limit)

    #Add a make_purchase method to this class that
    #meets the specifications laid out in this docstring:
    '''
    Run the make_purchase function in the CreditCard class,
    and if that purchase is successful add to points_balance
    based on purchase_price*self.points_per_dollar_spent

    Arguments:
    purchase_price: The dollar amount to be charged to the card.

    Returns:
    purchase_approved: True if purchase_price + self.balance + self.fees <= self.limit,
        False otherwise.

    Examples:
    card_account = VentureCard('Lee Cardholder', 1234567891011121, 20, 1000,2)
    card_account.make_purchase(35) -> returns True, card_account.balance is now 35,
        card_account.points_balance is now 70
    card_account.fees = 900
    card_account.make_purchase(65) -> returns True, card_account.balance is now 100,
        card_account.points_balance is now 200
    card_account.make_purchase(1) -> returns False, card_account.balance is still 100,
        card_account.points_balance is still 200
    '''
    def make_purchase(self,purch_amount):
        if super(VentureCard,self).make_purchase(purch_amount) == True: 
        #class variables are changed by the method call in the 'if' statement
        #so no need to call again after the 'if' block; just update points
            self.points_balance+= self.points_per_dollar_spent*purch_amount
            return True
        else:
            return False
            
if __name__ == "__main__":
    pass
