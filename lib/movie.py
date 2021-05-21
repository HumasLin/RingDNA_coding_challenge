from lib.utils import *

class Movie:

    def __init__(self, title: str, price_code: int):
      self.title = title
      """ avoid invalid price code """
      if price_code not in logic["amount"]:
        raise ValueError("Movie type doesn't exist!")
      self.price_code = price_code

    def set_price_code(price_code: int):
        self.price_code = price_code