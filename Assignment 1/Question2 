import math
def are_balls_touching(x1, y1, r1, x2, y2, r2):
    #Calculate the distance between the centers of the two balls
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    #Check if the balls are touching
    if distance <= (r1 + r2):
        return distance, True
    else:
        return distance, False

# Input: Get the coordinates and radii of the two balls

print("Enter details for Ball 1")

x1 = float(input("Enter x-coordinate of Ball 1: "))

y1 = float(input("Enter y-coordinate of Ball 1: "))

r1 = float(input("Enter radius of Ball 1: "))



print("\nEnter details for Ball 2")

x2 = float(input("Enter x-coordinate for Ball 2: "))

y2 = float(input("Enter y-coordinate for Ball 2: "))

r2 = float(input("Enter radius for Ball 2: "))

# Output the input values

print("\nBall 1 Details:")

print(f"Coordinates: ({x1}, {y1}), Radius: {r1}")



print("\nBall 2 Details:")

print(f"Coordinates: ({x2}, {y2}), Radius: {r2}")


#Calculate distance and check if balls are touching
distance, touching = are_balls_touching(x1, y1, r1, x2, y2, r2)

#Output the distance and whether the balls are touching
print(f"\nDistance between the centers of the balls: {distance:.2f}")
if touching:
    print("The balls are touching.")
else:
    print("The balls are not touching.")