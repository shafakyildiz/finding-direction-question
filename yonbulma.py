# Path string
path = "LRGLRGLRGLRLGLRLLRLRLRGGGGLLLLLRRRRGG"

x = int(input("initial x-coordinate: "))
y = int(input("initial y-coordinate: "))

# Directions
# 1- North
# 2- East
# 3- South
# 4- West

# initial direction is north
direction = 1

# converting path string to array
path.split()

for i in path:
    if i == "L":
        direction = (direction + 3) % 4
    if i == "R":
        direction = (direction + 1) % 4
    if i == "G":
        if direction == 1:
            y += 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            y -= 1
        elif direction == 0:
            x -= 1

if direction == 1:
    directionString = "North"
elif direction == 2:
    directionString = "East"
elif direction == 3:
    directionString = "South"
elif direction == 0:
    directionString = "West"

print("arrow direction is: ", directionString)
print("final x-coordinate is: ", x)
print("final y-coordinate is: ", y)
