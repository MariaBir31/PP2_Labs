#SETS
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others

