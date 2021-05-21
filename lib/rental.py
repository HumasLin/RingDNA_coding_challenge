from lib.utils import *
from lib.movie import Movie

class Rental:

    def __init__(self, movie: Movie, days_rented: int=0):
        self.movie = movie
        """ avoid negative rented days """
        if days_rented < 0:
        	raise ValueError("Rented days can't be negative!")
        self.days_rented = days_rented

    def get_amount(self):
        """ acquire the logic for billing """
        logic_amout = logic["amount"][self.movie.price_code]
        """ compute the amount due for the rental """
        amount = logic_amout["start"] * min(self.days_rented, logic_amout["threshold"]) + \
                 logic_amout["additional"] * max(0, self.days_rented-logic_amout["threshold"])
        return amount

    def get_point(self):
        """ acquire the logic for rewards """
        logic_point = logic["point"][self.movie.price_code]
        """ compute the rewards point from the rental """
        point = logic_point["start"] * min(self.days_rented,logic_point["threshold"]) + \
                logic_point["additional"] * max(0, self.days_rented-logic_point["threshold"])
        return point
