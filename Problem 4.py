# Alejandro Jiménez Rocha - sai993 - @01689144

"""Problem 4: 30 Points
Part A: Create Python function called displayFruits that will
 take in a Python list of fruits
 add a ‘mango’ to the end of the list
 prints, “There are” SizeOfList “fruits in the list containing [ fruit1,
fruit2,….fruitN, mango]”
o SizeOfList must be the number of unique names in the list irrespective of
the case (e.g. orange and Orange and ORAnge are not uniqe)"""


fruit_list = ['apple', 'orange', 'banana', 'cherries', 'Cherries']

# This assumes that all fruits are spelled the same way (albeit without the same capitalization).
# Note the capital C in the second 'Cherries'!


def displayFruits():
    fruit_list.append('mango')  # First, it adds 'mango'.
    fruit_list2 = []  # Separate second list, where I'm taking all the values in fruit_list and filtering them.
    for x in fruit_list:
        fruit_name = x.lower()  # Sets everything to lower case so we can compare them.
        if fruit_name not in fruit_list2:  # If it's in the list already (after being put in lower case) it skips it.
            fruit_list2.append(fruit_name)
        else:
            pass
    print(f'There are {len(fruit_list2)} fruits in the list, containing {fruit_list2}')

# This wouldn't filter out "Cherry" from "Cherries", but again, I'm assuming all the strings in the list are uniquely
# spelled out.
