import unittest
from lib.utils import *
from lib.movie import *
from lib.rental import *
from lib.customer import *
from lib.statement import *

class TestSystem(unittest.TestCase):

	""" Initialize instances for test """
	def setUp(self):
		self.movie = Movie("Test Movie", CLASSIC)

		self.customer = Customer("Scott")

		self.rental1 = Rental(self.movie, 1)
		self.rental2 = Rental(self.movie, 3)
	
	""" Test movie creation """
	def test_movie_entity(self):
		self.assertEqual(self.movie.title, "Test Movie", "Movie Title Error")
		self.assertEqual(self.movie.price_code, 3, "Movie Price Code Error")
		self.assertRaises(ValueError, Movie, "Error Movie", 4)

	""" Test rental creation """
	def test_rental_entity(self):
		self.assertEqual(self.rental1.movie.title, "Test Movie", "Rental Movie Error")
		self.assertEqual(self.rental1.days_rented, 1, "Rental Days Error")
		self.assertRaises(ValueError, Rental, self.movie, -4)

	""" Test billing computation """
	def test_rental_amount(self):	
		self.assertEqual(self.rental1.get_amount(),1, "Start Rewards Error")	
		self.assertEqual(self.rental2.get_amount(),3, "Start Rewards Error")

	""" Test rewards program computation """
	def test_rental_point(self):
		self.assertEqual(self.rental1.get_point(),1, "Start Rewards Error")
		self.assertEqual(self.rental2.get_point(),3, "Additonal Rewards Error")

	""" Test statement update """
	def test_statement_update(self):
		self.customer.add_rental(self.rental1)
		statement_content = Statement(self.customer).content
		self.assertEqual(statement_content[1],"\t Test Movie \t 1\n", "Add rental failed")
		self.customer.add_rental(self.rental2)
		statement_content = Statement(self.customer).content
		self.assertEqual(statement_content[2],"\t Test Movie \t 3\n", "Update rental failed")

	""" Test statement basics """
	def test_statement_basics(self):
		self.customer.add_rental(self.rental1)
		self.customer.add_rental(self.rental2)
		statement_content = Statement(self.customer).content
		self.assertEqual(statement_content[0],"Rental Record for Scott\n", "Customer Info Error")
		self.assertEqual(statement_content[3],"Amount owed is $4\n", "Billing Content Error")
		self.assertEqual(statement_content[4],"You earned 4 frequent renter points.\n", "Rewards Content Error")

if __name__ == '__main__':
	unittest.main()
