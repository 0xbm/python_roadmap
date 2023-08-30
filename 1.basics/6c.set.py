print("""
Mutable
Nieuporządkowane kolekcja unikatowych elementów
nameSet = {"a", "a", "b"}
nameSet.add("c")
print(nameSet)      # {'a', 'c', 'b'}  # za drugim razem inna konfiguracja !!!! {'c', 'a', 'b'}

1. Create set
my_set = {"Geeks", "for", 10, 52.7, True}       # {True, 10, 'Geeks', 52.7, 'for'}  # pierwszy 


2. Slicing - NO SLICE

4. Methods

*add
my_set = {"a", "a", "b"}
my_set.add("c")
print(my_set)

*update
my_set = {"John", "Jane", "Doe"}
my_set2 = {"Jade", "Jay"}
my_set.update(my_set2)
print(my_set)       # {'Jade', 'John', 'Jane', 'Doe', 'Jay'} # za drugim razem inna konfiguracja !!!! 

Rest of known methods:
*pop
*remove
*intersection  # zwraca z dwoch setow te same dane (np. ten sam string, ktory wystepuje w dwoch setach)
*sorted # print(sorted(my_set))

""")