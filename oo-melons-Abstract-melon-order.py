"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Abstract class for global sales."""

    #AbstractMelonOrder is a Superclass.
    #DomesticMelonOrder and InternationalMelonOrder are the subclasses of AbstractMelonOrder.

    #The initialization for the subclasses have been removed because both subclases have some attributes that are the same. However, those that are different such as order_type and tax have been left under the subclasses. 

    #Therefore, an initalization has been done under the superclass with the following attributes : species, qty, shipped, country_code. 
        #country_code is only relevant to the international subclass, therefore the country code constructor has been set to "None".

    def __init__(self, species, qty, order_type=None, tax=None):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        # self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty, order_type=None, tax=None):
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08)
    # order_type = "domestic"
    # tax = 0.08


# class InternationalMelonOrder(AbstractMelonOrder):
#     """An international (non-US) melon order."""

#     # country_code = country_code
#     order_type = "international"
#     tax = 0.17


#     def get_country_code(self):
#         """Return the country code."""

# return self.country_code




"""def mult (num1, num2):
    return num1 * num2

product = mult(8, 7)
my_num = num1


class AbstractOrder(object):

    def __init__(self, qty, melon_type, order_type, country_code=None):
        self.name = name

  

class InternationalMelonOrder(AbstractOrder):
    
    def __init__(self, qty, melon_type, country_code):
        super(InternationalMelonOrder, self).__init__(qty, melon_type, 'international', country_code)
"""