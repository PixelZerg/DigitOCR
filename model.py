import numpy as np
from keras import models, layers, utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
import random

# data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# flatten images
im_size = 28*28
x_train = x_train.reshape(x_train.shape[0], im_size).astype('float32')
x_train /= 255 # normalise

x_test = x_test.reshape(x_test.shape[0], im_size).astype('float32')
x_test /= 255 # normalise

# convert to one-hot
y_train = utils.to_categorical(y_train, 10).astype('float32')
y_test = utils.to_categorical(y_test, 10).astype('float32')

# model
model = models.Sequential([
    layers.Dense(512, activation='sigmoid', input_dim=im_size),
    layers.Dense(512, activation='sigmoid'),
    layers.Dense(10, activation='softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer='sgd')

# train
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# test
# loss = model.evaluate(x_test,y_test)
# print(f"Test loss: {loss:.3}")
# print(model.predict(np.array([x_test[0]])))
# print(f"Test accuracy: {accuracy:.3%}")