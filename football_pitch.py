import cv2
import numpy as np

# Define the dimensions of the array
width, height = 700, 400

# Generate random RGB values for each pixel
grand = np.full((height, width, 3), (13,148,27), dtype=np.uint8)

R , C, _ = grand.shape
total_sections = C // 20

c = 1
section = 0
while c < total_sections:
  if c % 2 == 0:
    grand[:, (c-1) * total_sections: c * total_sections] = [1,140,15]
  c+= 1

x , y = 10 , 10
w, h = 680, 380
color = (255, 255, 255)
thickness = 2
cv2.rectangle(grand, (x, y), (x+w, y+h), color, thickness)
cv2.line(grand, (350, 10), (350,390), color, thickness)

cv2.rectangle(grand, (10, 80), (120, 320), color, thickness)
cv2.rectangle(grand, (580, 80), (690, 320), color, thickness)

cv2.rectangle(grand, (10, 120), (60, 280), color, thickness)
cv2.rectangle(grand, (640, 120), (690, 280), color, thickness)

cv2.circle(grand, (C//2, R//2), 100, color, thickness)
cv2.circle(grand, (C//2, R//2), 5, color, -1)
cv2.imshow("pitch", grand)
cv2.waitKey()