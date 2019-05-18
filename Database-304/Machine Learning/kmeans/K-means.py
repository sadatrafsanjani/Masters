import math
import operator
from PIL import Image
from itertools import product


[r1, g1, b1] = [0, 0, 255]
[r2, g2, b2] = [0, 255, 0]
[r3, g3, b3] = [255, 255, 255]

im = Image.open("input.jpg")
pixel = im.load()
[xm, ym] = im.size
img = Image.new( 'RGB', (xm, ym), "black")
pixels = img.load()

#while(1):
c1 = 1
c2 = 1
c3 = 1

[sr1, sg1, sb1] = [0, 0, 0]
[sr2, sg2, sb2] = [0, 0, 0]
[sr3, sg3, sb3] = [0, 0, 0]

for x,y in product(range(xm), range(ym)):
    
    [r, g, b] = pixel[x, y]
	
    d1 = math.sqrt(((r-r1) ** 2) + ((g-g1)**2) + ((b-b1)**2))
    d2 = math.sqrt(((r-r2) ** 2) + ((g-g2)**2) + ((b-b2)**2))
    d3 = math.sqrt(((r-r3) ** 2) + ((g-g3)**2) + ((b-b3)**2))
    
    if ((d1 <= d2) and (d1 <= d3)):
        [sr1, sg1, sb1] = [(sr1+r), (sg1+g), (sb1+b)]
        c1 += 1
        pixels[x, y] = (int(r1), int(g1), int(b1))
    elif ((d2 <= d1) and (d2 <= d3)):
        [sr2, sg2, sb2] = [(sr2+r), (sg2+g), (sb2+b)]
        c2 =+ 1
        pixels[x, y] = (int(r2), int(g2), int(b2))
    else:
        [sr3, sg3, sb3] = [(sr3+r), (sg3+g), (sb3+b)]
        c3 += 1
        pixels[x, y] = (int(r3), int(g3), int(b3))

	
p1 = operator.abs((r1-(sr1/c1))) + operator.abs((g1-(sg1/c1))) + operator.abs((b1-(sb1/c1)))
p2 = operator.abs((r2-(sr2/c2))) + operator.abs((g2-(sg2/c2))) + operator.abs((b2-(sb2/c2)))
p3 = operator.abs((r3-(sr3/c3))) + operator.abs((g3-(sg3/c3))) + operator.abs((b3-(sb3/c3)))
	

#if(p1 <= .5 and p2 <= .5 and p3 <= .5):
 #   break

[r1, g1, b1] = [(sr1/c1), (sg1/c1), (sb1/c1)]
[r2, g2, b2] = [(sr2/c2), (sg2/c2), (sb2/c2)]
[r3, g3, b3] = [(sr3/c3), (sg3/c3), (sb3/c3)]

img.save('test.png')
img.show()
