print("""
1. Create list 
my_list = ['one', 1, 'two', 2, 'x']

2. Slicing list

 H   E   L   L   O
 0   1   2   3   4
-5  -4  -3  -2  -1

Ex:
my_list[-2]     # 2
my_list[:1]     # 'one'
my_list[1:]     # 1, 'two', 2, 'x' 
my_list[2:5]    # 'two', 2, 'x' 
my_list[::2]    # 'one', 'two', 'x'
my_list[::-1]   # 'x', 2, 'two', 1, 'one'

3. Basic list operations

Ex:
my_list = [1,2,3]
your_list=[3,4,5]
print(my_list+your_list)    #[1, 2, 3, 3, 4, 5]

my_list += [3,4,5,6]
print(my_list)    # [1, 2, 3, 3, 4, 5, 6]
print(my_list * 3)    # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

4. Methods

my_list.append(111)
print(my_list)  # [1, 2, 3, 111]

my_list.insert(5,'xyz')
print(my_list)

my_list.pop(2)
print(my_list)  # [1, 2, 'xyz']

my_list.remove('xyz')
print(my_list)  # [1, 2]

new_list=list(list_a)
print(new_list) # [1, 2, 3]

Rest of known methods:
.index
.count
.sort
.reverse
.join

5. Nesting lists

Ex:
list_a = [1,2,3]
list_b = ['a','b','c']

print([list_a,list_b])
list_c = [list_a,list_b]
print(list_c[1])

""")