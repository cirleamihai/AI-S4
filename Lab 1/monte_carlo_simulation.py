import random
import math

R = 30  # Radius is 30 cm
l = 100  # Length of the square is 100 cm
b = 1  # radius of the ball is 1 cm
N = 1000000  # Number of iterations
hits = 0  # Number of hits

for _ in range(N):
    x = random.uniform(-l / 2, l / 2)
    y = random.uniform(-l / 2, l / 2)

    # check if the ball falls within the pipe
    if math.sqrt(x ** 2 + y ** 2) < R:
        hits += 1

# The probability is the ratio of the hits to the total number of iterations
probability = hits / N
print(round(probability, 5))

# The area of the square is l^2
# The area of the circle is pi * R^2
# The probability is the ratio of the area of the circle to the area of the square
theoretical_probability = math.pi * R ** 2 / l ** 2
print(round(theoretical_probability, 5))

