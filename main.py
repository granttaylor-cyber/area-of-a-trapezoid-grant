game.splash("Lets calculate the area of a trapazoid!")
base1 = game.ask_for_number("what is the base1(cm)?")
base2 = game.ask_for_number("what is the base2(cm)?")
height = game.ask_for_number("what is the height(cm)")
area = base1 + base2
area = area / 2
area = area * height
game.splash("the area of the trapazoid with base1 " + str(base1) + "cm and the base2 " + str(base2) + "cm and finally a height of " + str(height) + "cm" + ",gives us an area of  " + str(area) + "cm^2")