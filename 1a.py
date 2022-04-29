from PIL import Image

iterations = 4

w,h = 3**(iterations + 1),2*(iterations + 1) + 1

img = Image.new("RGB", (w,h), (255,255,255))

for i in range(w):
    img.putpixel((i,1), (0,0,0))

for i in range(iterations):
    y = 2 * (i + 1) + 1
    for j in [0,2]:
        for x in range(w//3):
            x1 = j*(w//3) + x
            x2 = 3 * x
            img.putpixel((x1,y),img.getpixel((x2,y-2)))

img.save("1a.png")