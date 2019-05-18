import numpy as np
import glob as gb
from PIL import Image
from itertools import product

S = np.zeros((256**3), dtype=np.float64)
NS = np.zeros((256**3), dtype=np.float64)

realImage = [f for f in gb.glob("ibtd/*.jpg")]
maskImage = [f for f in gb.glob("ibtd/mask/*.bmp")]


for i in range(len(realImage)):
    
    img = Image.open(realImage[i])
    mask = Image.open(maskImage[i])
    
    pixel1 = img.load()
    pixel2 = mask.load()
    
    [w, h] = img.size
    
    for x,y in product(range(w), range(h)):
        
        [r, g, b] = pixel1[x, y]
        [r1, g1, b1] = pixel2[x, y]
        
        q = r1 * (256**2) + (g1 * 256) + b1
        
        if(q >= 16777215):
            
            p = r * (256**2) + (g * 256) + b
            NS[p] += 1
            
        else:
            S[q] += 1
            

p1 = S / float(np.sum(S))
p2 = NS / float(np.sum(NS))


file = open("skin.txt", "w")

for i in range(256**3):
    
    t = 0.0
    
    if(p2[i] > 0):
        t = float(p1[i]) / float(p2[i])
        print(t)
    
    file.write(str(t) + str('\n'))
    

file.close()


    
test_image = 'test.JPG'

img = Image.open(test_image)

pixel = img.load()

[w, h] = img.size


for x,y in product(range(w), range(h)):
    
    [r, g, b] = pixel[x, y]
     
    rgb = r * (256**2) + (g * 256) + b
    
    
    with open('skin.txt') as f:
        
        lines = f.read().split('\n')[rgb]
        
        print(float(lines))
    
        
        if(float(lines) > 0.4):
            
            pixel[x, y] = (255, 255, 255)
            
        else:
            pixel[x, y] = (0, 0, 0)
            
       
img = Image.new( 'RGB', (w, h), "black")        
img.save('test_detected','JPEG')
 

f.close()