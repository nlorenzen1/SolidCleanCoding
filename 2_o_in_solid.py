'''
Single Responsiblity Principle
Open/Closed Principle
L
I
D

Extension without modification
'''


#Wrong:
class Discount(object):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'regular':
            return self.price * 0.2
        if self.customer == 'senior':
            return self.price * 0.4
        else:
            raise Exception("Unknown customer")



#Right:
class Discount2(object):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    
    def give_discount(self):
            return self.price * 0.2

class SeniorDiscount(Discount2):
    def __init__(self, customer, price):
        super().__init__(customer, price)
    
    def give_discount(self):
        super().give_discount() * 2
