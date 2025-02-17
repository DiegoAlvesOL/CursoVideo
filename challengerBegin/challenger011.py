print("="*17)
print("==CHALLENGER011==")
print("="*17)
print("the purpose of this programme is to receive size of wall and show how much ink you need to paint everything")
print("="*17)

#height =  altura  width = largura

width = int(input("Please enter with width of the wall: "))
height = int(input("Please enter with height of the wall: "))

totalArea = width*height

print("The total area is", totalArea)

inkArea = 2
inkNeed = totalArea/inkArea

print("You need ",inkNeed, "liters of ink to paint all the wall")