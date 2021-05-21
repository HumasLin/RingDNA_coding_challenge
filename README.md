Description
-------------
This program is a statement generation system for movie rental business, which includes billing and rewards program sections:

The logic for billing is:
 - Regular movies cost $2.00 for the first two days of the rental, and cost $1.50 for each additional day
 - Children’s movies cost $1.50 for the first 3 days of the rental, and cost $1.50 for each additional day
 - New Releases cost $3.00 per day
 - Classic movies cost $1.00 per day

The existing logic for the rewards program is:
 - Regular movie rentals earn 1 reward point per rental
 - Children’s movie rentals earn 1 reward point per rental
 - New releases earn 1 point if the rental is for 1 day, and 2 points if the rental is longer than 1 day
 - Classic movies earn 1 reward point per rental

In the program, the structure of information is shown as:
```
|-- Customer
|  |-- Rentals
|  |  |-- Movie
```
By assembling the information contained in a customer's record, the program can generate a statement containing the specific information of rentals and the account summary information of the customer.

The codes in the `lib/` directory are:
 - `customer.py`: define the `Customer` object with name and rental records
 - `movie.py`: define the `Movie` object with title and price code
 - `rental.py`: define the `Rental` object with associated movie and rented days, with computation on billing and rewards based on predefined logics
 - `statement.py`: define the `Statement` object that assembles customer records 
 - `utils.py`: contain variables that define the logic of billing and rewards

Demonstration
-------------
There are two programs that demonstrate the functionalily of the code:

* `demo.py`: In this program, a customer instance is created first, with three rental instances associated with three movies added to his record. Then the first statement is generated and displayed. Then, with a new rental instance associated with a new movie added to customer record, a new statement is generated and displayed. This program demonstrates that statement is independent of the customer.

* The demonstration code can be run by:
```
	python3 demo.py
```

* `system_test.py`: In this test, the program tests the creation of movies and rentals (function 1 and 2), the computation of billing and rewards (function 3 and 4), and the generation of statement (function 5 and 6). There are 6 tests in total.

* To test the modules in the program, the unit test program can be run by:
```
	python3 -m unittest system_test.py
```
*python3 can be replaced by python if necessary*