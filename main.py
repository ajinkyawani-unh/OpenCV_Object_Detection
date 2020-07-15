import numpy as np
import cv2


img = cv2.imread("fuzzy.png", 1);
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
blur = cv2.GaussianBlur(gray, (3,3), 0)

cv2.imshow("Gray", gray);
cv2.imshow("Blur", blur);


cv2.waitKey(0);
cv2.destryAllWindows();