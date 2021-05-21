""" This file contains useful variables for the program """

""" Price codes for all kinds of movies """
REGULAR = 0;   
CHILDRENS = 1;
NEW_RELEASE = 2;
CLASSIC = 3;

"""
Logics for billing and rewards program:
For movies with varied additional day rates, 
threshold represents the divide for additional days,
the rates for additional days are also included.
For movies without varied additional day rates,
threshold is set to 0, and additional day rates equal to the start rate.
"""
logic = {"amount":{0:{"start":2,"threshold":2,"additional":1.5},
        1:{"start":1.5,"threshold":3,"additional":1.5},
        2:{"start":3,"threshold":0,"additional":3},
        3:{"start":1,"threshold":0,"additional":1}},

        "point":{0:{"start":1,"threshold":0,"additional":1},
        1:{"start":1,"threshold":0,"additional":1},
        2:{"start":1,"threshold":1,"additional":2},
        3:{"start":1,"threshold":0,"additional":1}}}