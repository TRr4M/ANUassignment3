#Code by David Josipovic

#matrix.py needs to be in this folder for this to work

import matrix
Matrix = matrix.Matrix
from PIL import Image
import random

w,h = 8000,8000
img = Image.new("RGB", (w,h), (255,255,255))

F = [
    lambda m : Matrix([
        [-0.7,0],
        [0,0.7]
    ]).times(m).plus(Matrix([[0.85],[0]])),
    lambda m : Matrix([
        [0.15,-0.15],
        [0,0.3]
    ]).times(m).plus(Matrix([[0.15],[0.7]])),
    lambda m : Matrix([
        [-0.15,0.15],
        [0,0.3]
    ]).times(m).plus(Matrix([[0.85],[0.7]])),
    lambda m : Matrix([
        [0,0.3],
        [0.3,0]
    ]).times(m).plus(Matrix([[0.35],[0.7]]))
]
colors = [
    (0,0,0),
    (255,0,0),
    (0,0,255),
    (0,255,0)
]
P = [0.49/0.67,0.045/0.67,0.045/0.67,0.09/0.67]

pos = Matrix([[0],[0]])
color = (255,255,255)
blend = 0.5
initialIterations = 10000
actualIterations = 2000000

blend_ = 1-blend
for _ in range(initialIterations):
    p = random.random()
    i = -1
    while p >= 0:
        i += 1
        p -= P[i]
    f = F[i]
    color = (
        (color[0]*blend_) + (colors[i][0]*blend),
        (color[1]*blend_) + (colors[i][1]*blend),
        (color[2]*blend_) + (colors[i][2]*blend)
    )
    pos = f(pos)
q = 0
while True:
    for _ in range(actualIterations):
        p = random.random()
        i = -1
        while p >= 0:
            i += 1
            p -= P[i]
        f = F[i]
        color = (
            (color[0]*blend_) + (colors[i][0]*blend),
            (color[1]*blend_) + (colors[i][1]*blend),
            (color[2]*blend_) + (colors[i][2]*blend)
        )
        pos = f(pos)
        img.putpixel((round(min(pos.matrix[0][0]*w,w-1)),round(h-(max(pos.matrix[1][0]*h,1)))),(round(color[0]),round(color[1]),round(color[2])))
    q += 1
    img.save("chaos.png")
    print(f"{q*actualIterations} iterations complete")