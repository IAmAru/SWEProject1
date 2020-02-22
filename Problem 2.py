# Alejandro Jiménez Rocha - sai993 - @01689144
"""Problem 2: 20 points
Rewrite the following Python script without the use of the break or continue command

fruits=["apple","orange","banana","mango"]
for item in fruits:
    if item == "banana":
        continue #continue with next iteration
    else:
        print item
"""

fruits = ["apple", "orange", "banana", "mango"]  # Initializes the 'fruits' list with four items.
for item in fruits:
    if item == "banana":  # If the for loop iterates through banana, it ignores it and continues the loop.
        pass
    else:
        print(item)
