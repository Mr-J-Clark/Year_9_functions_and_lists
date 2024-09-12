backpack = ["knife", "antidote", "rope", "rations", "water"]
def death():
    print("you die")
    print("urggggh!")
def bite():
    print("zombie bit you")
if "antidote" in backpack:
    print("you drink the antidote")
    print("phew.... you're still human")
    backpack.remove("antidote")
else:
    print("im craving flesh")
    print("you are now a zombie")
    backpack.remove("antidote")

death()
bite()
bite()
print("you pick up another antidote...phew")
backpack.append("antidote")
bite()
