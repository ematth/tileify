from PIL import Image, ImageSequence
import numpy as np
from itertools import product
import sys
import os


def tile_image(img: np.ndarray, name: str) -> None:
    """Tiles an image into 80x80 pixel tiles and saves them to a generated directory.

    Args:
        img (np.ndarray): image data to be processed
        name (str): name of the image file
    """
    assert img.shape[0] % 80 == 0 and img.shape[1] % 80 == 0, 'Image dimensions must be divisible by 80'
    os.makedirs(f'./{name}_tiles', exist_ok=True)

    for r,c in product(range(img.shape[1]//80), range(img.shape[0]//80)):
        cropped_data = img[(t:=c*80):t+80, (b:=r*80):b+80]
        cropped = Image.fromarray(np.uint8(cropped_data))
        cropped.save(f'{name}_tiles/{name}_{c}_{r}.png')

    for r in range(img.shape[1]//80):
        for c in range(img.shape[0]//80):
            print(f':{name}_{r}_{c}:', end='')
    print()
    return


def load_image(filename: str) -> np.ndarray:
    """Loads an image from disk and converts it to a numpy array.
    PIL accepts a wide range of image formats, including .png, .jpg, .bmp, etc.
    so don't complain if it doesn't work with YOUR niche format.

    Args:
        filename (str): path to the image file

    Returns:
        np.ndarray: image data as a numpy array
    """
    try:
        img = Image.open(filename).convert('RGBA')
    except Exception as e:
        print(f'Error loading image: {e}')

    w, h = img.size
    img = img.resize((w - w % 80, h - h % 80))
    return np.array(img).astype(np.uint8)    


def tile_gif(frames: list[Image], name: str, dur: float) -> None:
    assert frames[0].shape[0] % 80 == 0 and frames[0].shape[1] % 80 == 0, 'GIF dimensions must be divisible by 80'
    os.makedirs(f'./{name}_tiles', exist_ok=True)

    for r,c in product(range(frames[0].shape[1]//80), range(frames[0].shape[0]//80)):
        cropped_gif = []
        for f in frames:
            cropped_data = f[(t:=c*80):t+80, (b:=r*80):b+80]
            cropped_gif.append(Image.fromarray(np.uint8(cropped_data)).convert('RGBA'))
        cropped_gif[0].save(f'{name}_tiles/{name}_{c}_{r}.gif', save_all=True, append_images=cropped_gif[1:], loop=0, duration=dur)

    for r in range(frames[0].shape[1]//80):
        for c in range(frames[1].shape[0]//80):
            print(f':{name}_{r}_{c}:', end='')
    print()
    return


def load_gif(filename: str) -> tuple[list[Image], float]:
    gif = Image.open(filename)
    frames = [frame.copy().convert('RGBA') for frame in ImageSequence.Iterator(gif)]

    w, h = gif.size
    for i, frame in enumerate(frames):
        frames[i] = frame.resize((w - w % 80, h - h % 80))
    return [np.array(f).astype(np.uint8) for f in frames], gif.info['duration']


if __name__ == '__main__':
    """
    Usage: python tileify.py path/to/file.extension

    Example: python tileify.py example.png
    """
    filename = sys.argv[1]
    if filename.split('.')[-1] == 'gif':
        gif, dur = load_gif(filename)
        tile_gif(gif, filename.split('.')[0], dur)
    else: 
        img = load_image(filename)
        tile_image(img, filename.split('.')[0])
