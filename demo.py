from lib.utils import *
from lib.movie import *
from lib.rental import *
from lib.customer import *
from lib.statement import *

""" Create movies """
movie1 = Movie('First Movie', REGULAR)
movie2 = Movie('Second Movie', NEW_RELEASE)
movie3 = Movie('Third Movie', CHILDRENS)
movie4 = Movie('Fourth Movie', CLASSIC)

""" Create a customer instance """
customer = Customer("Scott")

""" Update a customer's rental record and display """
rental1 = Rental(movie1, 3)
rental2 = Rental(movie2, 4)
rental3 = Rental(movie3, 5)
customer.add_rental(rental1)
customer.add_rental(rental2)
customer.add_rental(rental3)

statement1 = Statement(customer)
print("Print statement1:")
statement1.print_content()

print("Update rentals...\n")
""" Update a customer's rental record and display """
rental4 = Rental(movie4, 7)
customer.add_rental(rental4)

statement2 = Statement(customer)
print("Print statement2:")
statement2.print_content()
print("Print statement1:")
statement1.print_content()
