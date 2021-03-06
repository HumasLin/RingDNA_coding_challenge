Given the reorganization of the codes, I think it's good to talk a little bit about my ideas behind the changes:

- The main idea of me refactoring the code is to make it a program easy to maintain and update. That's why I transformed the computation of billing and rewards information into a more generalized formula instead of prolonged `if-else` sentences. With this, modifying or updating how rentals for certain kinds of movies are computed can be realized by simply changing the variables `logic` defined in `lib\utils.py`. This is a lot more convenient than rewriting the `if-else` sentences. If the system grows into a large-scale one, this structure can also pave the path for using configuration files to define the logics in the system.  

- I made Statement an independent class, that's because I vision the program as a system that can be running as a database system, so there will be updates in a customer's records. Making statements an independent class can make it easier to create logs for a customer, which makes checking history records possible. 

- I chose to only put customer name in the statement object as I believe it's better to save the space for statement object. Storing numerous duplicate customer objects in statements can lead to severe space occupation when the system goes large. Also, as the system expands with more data, a unique identifier of a certain customer can be a better option than the name.

- I removed the get_ functions (e.g, `get_name()` in the original version for Customer), as it's sufficient now to just source the attribute of the certain object in Python. The get_ functions acutally can make the code more messy. If API in further development would need those functions, it can also be easily recreated.

- In the test file, I only include one kind of movie as for current tests, it's more reasonable to run only one movie instance, so that the test can find out if the computation on one specific logic of billing and rewards works. This makes sure the error can be pinpointed easily. Also, if only one movie is tested each time, it'll be simple to modify the test based on the instance of interest. 

I'll be glad to further discuss more about my decisions in transforming the codes if you have any questions!