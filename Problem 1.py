# Alejandro Jiménez Rocha - sai993 - @01689144

"""Problem 1: 20 Points
Rewrite the following Python script without the use of the break or continue command

y=1
for x in range(4,256,4):
    y = y*x
    if y > 512:
        break
    print y
"""

y = 1  # Initializes y at 1.

for x in range(4, 256, 4):  # Starts x at 4, ends at 256, and has an increment of 4 (4, 8, 12...)
    y = y * x  # HAS to be before the if statement so that it uses a new value each iteration of the loop.
    if y > 512:
        pass  # Pass defines the state of the iterations I'm ignoring / don't want.
    else:
        print(y)
