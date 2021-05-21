from lib.movie import Movie
from lib.rental import Rental
from lib.customer import Customer

""" Define the class of statement """
class Statement:

    def __init__(self, customer: Customer, amounts: float=0.0, points: int=0, content: list=[]):
        self.customer_name = customer.name
        self.amounts = amounts
        self.points = points
        self.content = content

        """ generate statement content in initialization """
        rentals = customer.rentals

        self.content = [f"Rental Record for {customer.name}\n"] # customer info
        self.content += [f"\t {each.movie.title} \t {each.get_amount()}\n"
                          for each in rentals] # rental infos
        total_amount = sum([each.get_amount() for each in rentals]) # total amount due
        renter_points = sum([each.get_point() for each in rentals]) # total rewards point

        self.content.append(f"Amount owed is ${total_amount}\n") # amount summary
        self.content.append(f"You earned {renter_points} frequent renter points.\n") # rewards summary

    def print_content(self):
        print("".join(self.content))
