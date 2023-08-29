print("""
Use Tuple
If your data should or does not need to be changed. IMMUTABLE
Tuples are faster than lists. We should use a Tuple instead of a List if we are defining a constant set of values and all we are ever going to do with it is iterate through it.
If we need an array of elements to be used as dictionary keys, we can use Tuples. As Lists are mutable (unhashable type), they can never be used as dictionary keys.

1. Create tuple
my_tuple = ('one', 1, 'two', 2, 'x')
my_one_tuple = ('one',)    # !! comma !! must be

print(my_tuple[0])     # ('one')

2. Slicing tuple

H   E   L   L   O
 0   1   2   3   4
-5  -4  -3  -2  -1

Ex:
my_tuple[-2]     # (2)
my_tuple[:1]     # ('one')
my_tuple[1:]     # (1, 'two', 2, 'x')
my_tuple[2:5]    # ('two', 2, 'x') 
my_tuple[::2]    # ('one', 'two', 'x')
my_tuple[::-1]   # ('x', 2, 'two', 1, 'one')

3. Basic tuple operations

my_tuple = ('one', 1, 'two', 2, 'x')
my_tuple += (1,'asd')   # ('one', 1, 'two', 2, 'x', 1, 'asd')


4. Methods

my_tuple = ('one', 1, 'two', 2, 'x', 1)

print(my_tuple.index('one')     # 0
print(my_tuple.count(1)     # 2

""")