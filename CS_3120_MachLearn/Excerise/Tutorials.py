"""Basic data types
Like most languages, Python has a number of basic types including integers, floats,
booleans, and strings. These data types behave in ways that are familiar from other
programming languages.

Numbers: Integers and floats work as you would expect from other languages:
"""

x = 3
print(x ** 2)
t = True
f = False
print(t != f)

"""
Strings: Python has great support for strings:
"""

hello = 'hello'     # String Literals can use single quotes
world = 'world'
print(len(hello))
hw = hello + ' ' + world    # String concatenation
print(hw)   # prints "hello world"

"""String objects have a bunch of useful methods; for example:

CONTAINERS

Python includes several built-in container types:
    1. Lists
    2. Dictionaries
    3. Sets
    4. Tuples
    
LISTS
    A list is the Python equivalent of an array, but is resizable
    and can contain elements of different types:
"""

xs = [3, 1, 2]      # Create a list
print(xs, xs[2])    # Prints "[3, 1, 2] 2"
print(xs[-1])       # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'       # Lists can contain elements of different types
print(xs)           # Prints "[3, 1, 'foo']"

"""
SLICING
    In addition to accessing list elements one at a time, Python provides concise syntax
    to access sublsts; this is know as slicing
"""

nums = list(range(5))       # range is a built-in function that creates a list of integers
print(nums)                 # prints "[0, 1, 2, 3, 4]"
print(nums[2:4])            # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])             # Prints "[2, 3, 4]"
print(nums[:-1])            # Slice indices can be negative; prints "[0, 1, 2, 3]"

"""
We will see slicing again in the context of numpy arrays.

Loops
    You can loop over the elements of a list like this
"""

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)       # Prints "cat", "dog", "monkey", each on its own line.

"""
If you want access to the index of each element within the body of a loop
use the built-in enumerate function:
"""

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))  # Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

"""
Dictionaries
    A dictionary stores (key,value) pairs, similar to a map in java or an object in
    Javascript.
    
You can use it like this:
"""

d = {'cat': 'cute', 'dog': 'furry'}     # Create a new dictionary with some data
print(d['cat'])                         # prints "cute"

"""
TUPLES
    A tuple is an (immutable) ordered list of values. A tuple is in many ways similar
    to a list; one of the most important differences is that tuples can be used as keys
    in dictionaries and as elements of sets, while lists cannot.
    
    Here is a trivial example:
"""

d = {(x, x + 1): x for x in range(10)} # Create a dictionary with tuple keys
t = (5, 6)      # create a tuple
print(type(t))  # Prints "<class 'tuple'>"
print(d[t])     # Prints "5"
print(d[(1, 2)])    # Prints "1"

"""
Functions
    Python functions are defined using the def keyword.
    
    For Example
"""

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))      # Prints "negative", "zero", "positive"

"""
Numpy
    Is the core library for scientific in Python. It provides a high-performance
    multidimensional array object, and tools for working with these arrays

    Arrays
        A numpy array is a grid of values, all of the same type, and is indexed by
        a tuple of nonnegative integers. The number of dimensions is the rank of 
        the array; The shape of an array is a tuple of integers giving the size of
        the array along each dimensions.
        
        We can initialize numpy arrays from nested Python lists, and access elements
        using square brackets:
"""

import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6]])        # Create a rank 2 array
print(b.shape)                              # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])            # Prints "1 2 4"

"""
        Numpy also provies many functions to create arrays:
"""

a = np.zeros((2, 2))        # Create an array of all zeros
print(a)                    # Prints "[[0. 0.]
                            #          [0. 0.]]"
b = np.ones((1, 2))         # Create an array of all ones
print(b)

c = np.full((2, 2), 7)      # Create a constant array
print(c)

d = np.eye(2)               # Create a 2x2 identify matrix
print(d)

e = np.random.random((2, 2))    # Create an array filled with random values
print(e)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it will modify the
# original array.

print(a[0, 1])
b[0, 0] = 77
print(a[0, 1])

"""
Array Math
    Basic mathematical functions operate element wise on arrays, and are available
    both as operator overloads and as functions in the numpy module:
"""

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

print(x * y)
print(np.add(x, y))

v = np.array([9, 10])
print(x.dot(v))
print(np.dot(x, v))

"""
BROADCASTING
    Boardcasting is a powerful mechanism that allows numpy to work with arrays of 
    different shapes when performing arithmetic operations. Frequently we have a
    smaller array and a larger array, and we want to use the smaller array 
    multiple times to perform some operation on the larger array.
"""

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))
print(vv)
y = x + vv
print(y)
print(x + v)

