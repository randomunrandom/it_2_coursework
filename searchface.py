import time
import const

import telegram as tg
import telegram.ext as tgext

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
from PIL import Image
import skimage
from skimage import transform
from skimage.io import imread
import skimage.data
from sklearn.externals import joblib
from skimage.feature import hog
from tqdm import tqdm

cls = joblib.load('cls.pkl')
window_size = (62, 47)
multiply = 0.75
im = Image.open("photos\\3666-Daniil.png")
nx, ny = im.size
im = im.resize((max(int(nx*multiply), window_size[0]), max(int(ny*multiply), window_size[1])), Image.BICUBIC)
im.save("photos\\3666-Daniil.png")

img = imread("photos\\3666-Daniil.png")


def search_window(img, scale=1, i_step=2, j_step=2):
    res = list()
    ii = int(scale * window_size[0])
    jj = int(scale * window_size[1])
    print(f'ii: {ii}, jj: {jj}')
    for i in tqdm(range(0, img.shape[0] - ii, i_step)):
        for j in range(0, img.shape[1] - jj, j_step):
            patch = img[i:i + ii, j:j + jj]
            if scale != 1.0:
                patch = transform.resize(patch, window_size)
            # orientations=8, pixels_per_cell=(6, 6), cells_per_block=(1, 1),feature_vector=True,
            hog_fv = hog(patch[:, :, 2], visualise=False)
            if cls.predict(np.expand_dims(hog_fv, 0)):
                res.append((i, j, ii, jj))
    res = np.asarray(res)
    return res


coord = search_window(img, scale=2, i_step=2, j_step=2)
print(coord)
print(coord.shape)

fig, ax = plt.subplots()
ax.imshow(img, cmap='gray')
ax.axis('off')
for i in coord:
    ax.add_patch(plt.Rectangle((i[0], i[1]), i[2], i[3], edgecolor='red', alpha=0.3, lw=2, facecolor='none'))
plt.show()
