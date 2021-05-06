import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import SGD
import time
from tensorflow import keras
# from tensorflow.keras.callbacks import TensorBoard

# name = "SLF_CNN_FirstModel-{}".format(int(time.time()))
# tensorboard = TensorBoard(log_dir='logs/{}'.format(name))

print(tf.__version__) # working with 2.1.0
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
# sess = tf.Session(tf.tf.compat.v1.ConfigProto(gpu_options=gpu_options))
# tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=.333)


x = pickle.load(open('x.pickle', 'rb'))
y = pickle.load(open('y.pickle', 'rb'))
y = np.array(y)

# Normalizing the data
# for images, we know the min is 0 and max is 255
x = x / 255.0

tf.random.set_seed(1234)

# first layer

model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('sigmoid'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# second layer

model.add(Conv2D(32, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('sigmoid'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(64, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('sigmoid'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# third layer

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('sigmoid'))

# output layer

model.add(Dense(1))
model.add(Activation('sigmoid'))

# opt = SGD(lr=0.01)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x, y, batch_size=10, validation_split=0.30, epochs=3)  # our dataset is 297 so 10 at a time
# add in callbacks = [tensorboard]
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.figure(4)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

## Testing out with previous code with example code:
#
#
# print(tf.test.is_gpu_available())
# print(tf.test.is_built_with_cuda())
# print(tf.__version__)
#
#
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(x.shape[1:])),
#     keras.layers.Dense(150, activation=tf.nn.relu),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# # training model
# model.fit(x, y, epochs=5)
#
# train_loss, train_acc = model.evaluate(x, y)
# print('Train Accuracy: ', train_acc)

