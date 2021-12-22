import cv2
import numpy as np

# path/name of the image
img_path = 'image.png'
# caption
caption = 'Wasted'

# font setting
font_face = cv2.FONT_HERSHEY_DUPLEX
font_scale = 1.0
# white color
font_color = (255, 255, 255)
font_thickness = 2

# read image (gray)
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# img: [H, W]
print(img.shape)

# get string size
font_size = cv2.getTextSize(caption, font_face, font_scale, font_thickness)
# font size: ((width, height), baseline)
print(font_size)

# caption background (black)
# string height * 3
bg_h = font_size[0][1] * 3
# image width
bg_w = img.shape[1]
# black background
bg = np.zeros((bg_h, bg_w)).astype(np.uint8)

# add caption
img_bg = np.concatenate([img, bg], 0)
img_cap = img_bg.copy()
cv2.putText(img_cap, caption, ((bg_w - font_size[0][0]) // 2, img.shape[0] + bg_h // 2 + font_size[1] // 2), font_face, font_scale, font_color, font_thickness)

cv2.imshow("img", img_cap)
cv2.waitKey()

# write to 'xxx_converted.xxx'
cv2.imwrite(img_path.split('.')[-2] + '_converted.' + img_path.split('.')[-1], img_cap)
