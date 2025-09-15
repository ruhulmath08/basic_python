"""

In Python, an iterator is an object that allows you to traverse through a sequence of data (like lists, tuples,
strings, etc.) one element at a time.

It follows the iterator protocol, which means the object must implement two methods:
	1.	__iter__() → Returns the iterator object itself.
	2.	__next__() → Returns the next item in the sequence. If there are no more items, it raises a StopIteration
	    exception.

"""


## Custom Iterator class
class CountDown:
    # Constructor method: initializes the starting value
    def __init__(self, start):
        # store the initial value in 'current'
        self.current = start

    # __iter__ method: must return the iterator object itself
    def __iter__(self):
        return self

    # __next__ method: called each time next() is used
    def __next__(self):
        # If the current is 0 or less, no more items to return
        if self.current <= 0:
            # signal that iteration is finished
            raise StopIteration

        # Decrease current by 1
        self.current -= 1
        # Return the value before it was decreased
        return self.current + 1


# Using the custom iterator
# create a CountDown object and loop over it
for i in CountDown(5):
    # each iteration calls __next__() to get the next value
    print(i)
