import time
import const
import telegram as tg
import telegram.ext as tgext
import skimage
# from skimage import io
# from skimage.io import imread
# import skimage.data
from skimage.feature import hog
import numpy as np
from sklearn.externals import joblib
import cv2

cls = joblib.load('cls.pkl')
people_size = (62, 47)


def search(filepath):
    img = cv2.imread(filepath)
    rects = list()
    print(img.shape)
    print(type(img))

    # return cls.predict(hog(img[:, :, 2]))


print(skimage.__version__)
search("photos\\3600-RandomDanil.png")

