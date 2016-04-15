"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Abstract class for global sales."""

    #AbstractMelonOrder is a Superclass.
    #DomesticMelonOrder and InternationalMelonOrder are the subclasses of AbstractMelonOrder.

    #The initialization for the subclasses have been removed because both subclases have some attributes that are the same. 

    #An initalization has been done under the superclass with the following attributes : self, species, qty, order_type, tax, and country_code. 
        #country_code is only relevant to the international subclass, therefore the country code parameter has been set to "None".

        #Note: constructor is AKA as __init__ dunder method.

    def __init__(self, species, qty, order_type=None, tax=None, country_code=None):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
       

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

#refactoring the subclases by adding the super method. NOTE: The __init__ for the subclass does not need to match the arguments in the super class __init__; however, it does need to match in the subclass super method. 

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17, country_code)



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