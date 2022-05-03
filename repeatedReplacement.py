#Code by David Josipovic

#matrix.py needs to be in this folder for this to work

import matrix
Matrix = matrix.Matrix
from PIL import Image
import os

#dir_path = os.path.dirname(os.path.realpath(__file__))
#L = Image.open(f"{dir_path}/L.png")
L = Image.open(f"Start.png")
w,h = L.width, L.height
img = Image.new("RGB", (w,h), (0,0,0))

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
q = 0
while True:
    q += 1
    for i in range(w):
        for j in range(1,h+1):
            for n in range(len(F)):
                f = F[n]
                p = f(Matrix([[i/w],[j/h]]))
                x, y = round(p.matrix[0][0]*w), round(p.matrix[1][0]*h)
                if x >= 0 and x < w and h >= y and y > 0:
                    c = L.getpixel((i,h-j))
                    if c[0] > 128:
                        img.putpixel((x,h-y), (255,255,255))
    input("Ready...")
    img.save("RR.png")
    L = img
    img = Image.new("RGB", (w,h), (0,0,0))
    print(f"{q} iterations complete")