# This is a list called 'backpack' that holds different items.
backpack = ["knife", "antidote", "rope", "rations", "water"]

# This is a function named 'death' that prints a message when called.
def death():
    print("you die")  # Message when you die.
    print("urggggh!")  # Extra dramatic dying sound.

# This is another function called 'bite' that prints a message when a zombie bites you.
def bite():
    print("zombie bit you")  # Message for when a zombie bites you.

# This 'if' statement checks if the item "antidote" is in the backpack.
if "antidote" in backpack:
    print("you drink the antidote")  # If antidote is there, you drink it.
    print("phew.... you're still human")  # You're still human because of the antidote.
    backpack.remove("antidote")  # The antidote is used, so it's removed from the backpack.
else:
    print("im craving flesh")  # If there is no antidote, you're turning into a zombie.
    print("you are now a zombie")  # You officially become a zombie.
    backpack.remove("antidote")  # Trying to remove the antidote that isn't there, which will cause an error!

# Calling the 'death' function to simulate dying.
death()

# Calling the 'bite' function twice to show that you got bitten two times.
bite()
bite()

# Now you pick up another antidote after being bitten.
print("you pick up another antidote...phew")
backpack.append("antidote")  # Adding an antidote back to the backpack.

# The zombie bites you again, but you have another antidote in your backpack.
bite()
