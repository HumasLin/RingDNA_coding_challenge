Given the reorganization of the codes, I think it's good to talk a little bit about my ideas behind the changes:

- The main idea of me refactoring the code is to make it a program easy to maintain and update. That's why I transformed the computation of billing and rewards information into a more generalized formula instead of prolonged `if-else` sentences. With this, modifying or updating how rentals for certain kinds of movies are computed can be realized by simply changing the variables `logic` defined in `lib\utils.py`. This is a lot more convenient than rewriting the `if-else` sentences. If the system grows into a large-scale one, this structure can also pave the path for using configuration files to define the logics in the system.  

- I made Statement an independent class, that's because I vision the program as a system that can be running as a database system, so there will be updates in a customer's records. Making statements an independent class can make it easier to create logs for a customer, which makes checking history records possible. 

- I removed the get_ functions (e.g, `get_name()` in the original version for Customer), as it's sufficient now to just source the attribute of the certain object in Python. The get_ functions acutally can make the code more messy. If API in further development would need those functions, it can also be easily recreated.

I'll be glad to further discuss more about my decisions in transforming the codes if you have any questions!