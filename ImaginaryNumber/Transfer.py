# codes borrowed from https://github.com/stephencwelch/Imaginary-Numbers-Are-Real

import matplotlib.image as mpimg
from pylab import *
import cv2

img = mpimg.imread('res/input.jpg')

# show image
# image: (1000, 1000, 3)
figure(0, (6, 6))
imshow(img)
show()

# cut the right part of image
imgRight = img[:, img.shape[1] // 2:]
# range of z
inputBounds = np.array([0, 2, -2, 2])
# size of original image
inputResolution = imgRight.shape

# show right part of image
figure(0, (6, 6))
imshow(imgRight)
show()

# range of w
outputBounds = 6.5 * np.array([-1, 1, -1, 1])
# size of output image
outputResolution = [1200, 1200]

# Create x and y sampling vectors
xInput = np.linspace(inputBounds[0], inputBounds[1], inputResolution[1])
yInput = np.linspace(inputBounds[2], inputBounds[3], inputResolution[0])

# Put sampling vectors on 2d grid:
x, y = np.meshgrid(xInput, yInput)
z = x + 1j * y

# print(z[0:4, 0:4])

w = z ** 2

# calculate scalar of re and im
reSlope = float(outputResolution[1]) / (outputBounds[1] - outputBounds[0])
imSlope = float(outputResolution[0]) / (outputBounds[3] - outputBounds[2])

# build index of output image
reIndex = (w.real * reSlope + outputResolution[1] / 2).round().astype('int')
imIndex = (w.imag * imSlope + outputResolution[0] / 2).round().astype('int')

outputImageSize = outputResolution[:]
outputImageSize.append(3)

mappedImage = np.empty(outputImageSize)
mappedImage[:] = NAN


def nasty_loop_time():
    whiteThresh = 200

    for i in range(inputResolution[0]):
        for j in range(inputResolution[1]):
            # Only map pixels in the output range:
            if 0 < reIndex[i, j] < outputResolution[1]:
                if 0 < imIndex[i, j] < outputResolution[0]:
                    # Check if that pixel has been filled yet:
                    if isnan(mappedImage[imIndex[i, j], reIndex[i, j], 0]):
                        mappedImage[imIndex[i, j], reIndex[i, j], :] = imgRight[i, j, :]
                    # Check if non-white:
                    elif imgRight[i, j, 0] < whiteThresh or imgRight[i, j, 1] < whiteThresh or \
                            imgRight[i, j, 2:] < whiteThresh:
                        mappedImage[imIndex[i, j], reIndex[i, j], :] = imgRight[i, j, :]


nasty_loop_time()

# figure(0, (12, 12))
mappedImageInt = mappedImage.astype('uint8')
# imshow(mappedImageInt)
# show()

# inpainting
mask = np.zeros((outputResolution[0], outputResolution[1]), dtype='uint8')
mask[isnan(mappedImage[:, :, 0])] = 1

# figure(0, (7, 7))
# imshow(mask)
# show()

# use the central part of output image
maskCentral = mask.copy()[300:900, 300:900]
mappedImageCentral = mappedImageInt.copy()[300:900, 300:900, :]

# figure(0, (7, 7))
# imshow(mappedImageCentral)
# show()

finalImage = cv2.inpaint(mappedImageCentral, maskCentral, 3, cv2.INPAINT_NS)

figure(0, (10, 10))
imshow(finalImage)
show()
imsave('res/output.jpg', finalImage)
