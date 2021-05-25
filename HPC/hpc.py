# Abe Jeyapratap
# 5/25/2021
# Modifications on TensorFlow MNIST Classification Model to be run on Picotte, the HPC Cluster

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import gzip
# import time
# import random

# Function to load data from /beegfs/Sample_TF_Datasets/ directory on Picotte
def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte.gz'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte.gz'
                               % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)

    return images, labels


print()
print(f"TensorFlow version = {tf.__version__}")
print()

if tf.test.gpu_device_name():
    print('Connected to GPU(s)', tf.test.gpu_device_name())
else:
    print('Not connected to GPU')
print()

# Load data
fashion_mnist = tf.keras.datasets.fashion_mnist
train_images, train_labels = load_mnist('/beegfs/Sample_TF_Datasets/Fashion_MNIST', kind='train')
test_images, test_labels = load_mnist('/beegfs/Sample_TF_Datasets/Fashion_MNIST', kind='t10k')

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Data Exploration: Check Shape
print(f'train_images.shape = {train_images.shape}')
print(f'train_labels.shape = {train_labels.shape}')
print(f'test_images.shape = {test_images.shape}')
print(f'test_labels.shape = {test_labels.shape}')
print()

# convert values to between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# instansitate the model by stacking the layers on top of each other
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # create network of 128 neurons
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)  # create network of 10
])

# create the model by passing in an optimizer, loss function and metric
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# fit the model with the data
model.fit(train_images, train_labels, epochs=10)

# save the model
tf.keras.models.save_model(model, 'recognition_model.hdf5')

# test the model
test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_accuracy)

probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()  # logits to find probabilities
])

# Make Predictions
predictions = probability_model.predict(test_images)
predicted_label = np.argmax(predictions)  # select max from the values returned
print(test_labels[0])  # actual labels for the values

# Graph


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()
