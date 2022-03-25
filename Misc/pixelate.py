# Reference: https://github.com/useless-tools/pixelate
from PIL import Image
import os


def pixelate(img_in: str, img_out: str, pixel_size: int):
    """
    Create a pixel image from the original image

    Reference: https://github.com/useless-tools/pixelate

    Args:
        img_in (str): input image path
        img_out (str): output image path
        pixel_size (int): pixel size
    """
    if not os.path.exists(img_in):
        raise FileNotFoundError('cannot find input image')

    image = Image.open(img_in)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.save(img_out)


if __name__ == '__main__':
    img_in = input('input image path (str): ')
    img_out = input('output image path (str): ')
    pixel_size = int(input('pixel size (int): '))
    pixelate(img_in, img_out, pixel_size)
    print('Done!')
