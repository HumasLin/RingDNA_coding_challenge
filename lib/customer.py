from lib.rental import Rental

""" Define the class of customer """
class Customer:

    def __init__(self, name: str, rentals: list=[]):
        self.name = name
        self.rentals = rentals

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)