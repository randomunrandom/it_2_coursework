import time
import const
import telegram as tg
import telegram.ext as tgext
import skimage
from skimage.io import imread
# import skimage.data
from skimage.feature import hog
import numpy as np
from sklearn.externals import joblib

cls = joblib.load('cls.pkl')
people_size = (62, 47)


def search(filepath):
    print('1')
    img = imread(filepath)
    print('2')
    rects = list()
    print('3')
    print(img)
    print('4')
    print(type(img))
    print('5')

    return cls.predict(hog(img[:, :, 2]))


search("photos\\3600-RandomDanil.png")
print(skimage.__version__)
