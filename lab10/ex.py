import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve


def download_and_unzip(url, save_path):
    print("Downloading and extracting assets...", end=" ")

    urlretrieve(url, save_path)

    try:

        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])

        print("Done!")

    except Exception as e:
        print("Invalid file:", e)

URL = "https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

cb_img = cv2.imread("checkerboard_18x18.png", 0)

if cb_img is None:
    raise FileNotFoundError("checkerboard_18x18.png not found!")

print(cb_img)

print("Image size (H, W):", cb_img.shape)
print("Data type:", cb_img.dtype)

plt.figure(figsize=(5, 5))
plt.imshow(cb_img, cmap="gray")
plt.title("Checkerboard")
plt.axis("off")
plt.show()

print("First black pixel:", cb_img[0, 0])
print("First white pixel:", cb_img[0, 6])

cb_img_copy = cb_img.copy()

cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

plt.figure(figsize=(5, 5))
plt.imshow(cb_img_copy, cmap="gray")
plt.title("Modified Checkerboard")
plt.axis("off")
plt.show()


img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

if img_NZ_bgr is None:
    raise FileNotFoundError("New_Zealand_Lake.jpg not found!")

img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(img_NZ_rgb)
plt.title("New Zealand Lake")
plt.axis("off")
plt.show()

cropped_region = img_NZ_rgb[200:400, 300:500]

plt.figure(figsize=(5, 5))
plt.imshow(cropped_region)
plt.title("Cropped Region")
plt.axis("off")
plt.show()

resized_cropped_region_2x = cv2.resize(
    cropped_region,
    None,
    fx=2,
    fy=2
)

plt.figure(figsize=(6, 6))
plt.imshow(resized_cropped_region_2x)
plt.title("Resized 2x")
plt.axis("off")
plt.show()


desired_width = 100
desired_height = 200

dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(
    cropped_region,
    dsize=dim,
    interpolation=cv2.INTER_AREA
)

plt.figure(figsize=(4, 6))
plt.imshow(resized_cropped_region)
plt.title("Fixed Resize")
plt.axis("off")
plt.show()

img_horz = cv2.flip(img_NZ_rgb, 1)
img_vert = cv2.flip(img_NZ_rgb, 0)
img_both = cv2.flip(img_NZ_rgb, -1)

plt.figure(figsize=(18, 5))

plt.subplot(1, 4, 1)
plt.imshow(img_horz)
plt.title("Horizontal")

plt.subplot(1, 4, 2)
plt.imshow(img_vert)
plt.title("Vertical")

plt.subplot(1, 4, 3)
plt.imshow(img_both)
plt.title("Both")

plt.subplot(1, 4, 4)
plt.imshow(img_NZ_rgb)
plt.title("Original")

plt.show()

imageCircle = img_NZ_bgr.copy()

cv2.circle(
    imageCircle,
    (600, 500),
    90,
    (0, 0, 255),
    thickness=5,
    lineType=cv2.LINE_AA
)

plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(imageCircle, cv2.COLOR_BGR2RGB))
plt.title("Circle")
plt.axis("off")
plt.show()

imageText = img_NZ_bgr.copy()

cv2.putText(
    imageText,
    "View of a lake",
    (200, 400),
    cv2.FONT_HERSHEY_PLAIN,
    2.3,
    (0, 255, 0),
    2,
    cv2.LINE_AA
)

plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(imageText, cv2.COLOR_BGR2RGB))
plt.title("Text")
plt.axis("off")
plt.show()

vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Cannot open webcam")

else:
    while True:

        ret, frame = vid.read()

        if not ret:
            print("Failed to capture frame")
            break

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()