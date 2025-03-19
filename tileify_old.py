from PIL import Image
import numpy as np
from itertools import product
import sys
import os

if len(sys.argv) < 2:
    print('ERROR: Script needs image name as arg')
    exit()

if len(sys.argv) > 2:
    print('ERROR: What the hell are these extra args...')
    exit()

name = sys.argv[1]

if 'png' in name or 'jpg' in name or 'gif' in name:
    print('ERROR: Please don\'t include extension in image name')
    exit()

if not os.path.isfile(f'{name}.png'):
    print('ERROR: The image has to exist...')
    exit()

img = Image.open(f'{name}.png').convert('RGBA')

width, height = img.size

num_rows = height // 80
num_cols = width // 80

os.makedirs('./tiles', exist_ok=True)

data = np.array(img)
for r,c in product(range(num_rows), range(num_cols)):
    left = c * 80
    right = left + 80
    top = r * 80
    bottom = top + 80
    cropped_data = data[top:bottom,left:right]
    cropped = Image.fromarray(np.uint8(cropped_data))
    cropped.save(f'tiles/{name}_{r}_{c}.png')

for r in range(num_rows):
    for c in range(num_cols):
        print(f':{name}_{r}_{c}:', end='')
    print()
