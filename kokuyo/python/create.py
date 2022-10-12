#!/usr/local/opt/python@3.9/bin/python3.9
from PIL import Image
import time
import json
import sys

color = [[255,100,100],
         [100,100,255],
         [100,255,100]]

action = ["working","meeting","talking"]

count = 0
while True:
    R,G,B = color[count]
    img = Image.new("RGB", (320, 180), (R, G, B))
    img.save(f"test.png")
    
    
    # detect result
    result = action[count]
    # jsonObj = json.dumps(result) # jsonに変換
    
    # recieve = sys.stdin.readline()
    # recieve = recieve + "OK!"
    
    # print('Content-type: text/html\n')
    # print(result)
    
    with open("result.txt", mode='w') as f:
        f.write(result)
    
    count = (count+1)%len(color)
    time.sleep(1)

# R,G,B = color[0]
# img = Image.new("RGB", (320, 180), (R, G, B))
# img.save(f"red.png")

# R,G,B = color[1]
# img = Image.new("RGB", (320, 180), (R, G, B))
# img.save(f"blue.png")

# R,G,B = color[2]
# img = Image.new("RGB", (320, 180), (R, G, B))
# img.save(f"green.png")