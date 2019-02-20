import numpy as np
from keras import models, layers
from keras.datasets import mnist
import matplotlib.pyplot as plt
import random

# data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

while True:
    i = random.randint(0,x_train.shape[0])
    print(y_train[i])
    plt.imshow(x_train[i], cmap='gray_r')
    plt.show()
