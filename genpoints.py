import argparse
import random
import math
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)




n = None
mindist = None
rseed = None

# Create the parser
parser = argparse.ArgumentParser(description="Process some input.")

# Add arguments
parser.add_argument('input', type=str, help='Input string to be split')

# Parse the arguments
args = parser.parse_args()

# Split the input
split_input = args.input.split(" ")

for item in split_input:
    if item[0:3] == "-N=":
        n = int(item[3:])
    if item[0:9] == "-mindist=":
        mindist = int(item[9:])
    if item[0:7] == "-rseed=":
        rseed = int(item[7:])

print(f"{n} {mindist} {rseed}")
if rseed is not None:
    random.seed(rseed)

coordinates = []

for i in range(n):
    while True:
            random_x = random.randint(-50, 50)
            random_y = random.randint(-50, 50)
            if all(euclidean_distance((random_x, random_y), item) >= mindist for item in coordinates):
                coordinates.append((random_x, random_y))
                break

for i, item in enumerate(coordinates):
    print(f"Coordinate {i+1}: (x: {item[0]}, y: {item[1]})")





