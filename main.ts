game.splash("Lets calculate the area of a trapazoid!")
let base1 = game.askForNumber("what is the base1(cm)?")
let base2 = game.askForNumber("what is the base2(cm)?")
let height = game.askForNumber("what is the height(cm)")
let area = base1 + base2
area = area / 2
area = area * height
game.splash("the area of the trapazoid with base1 " + ("" + base1) + "cm and the base2 " + ("" + base2) + "cm and finally a height of " + ("" + height) + "cm" + ",gives us an area of  " + ("" + area) + "cm^2")
