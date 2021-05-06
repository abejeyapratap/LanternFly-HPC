# Sarah Malik

import random

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pickle

# datadir = r"/home/DREXEL/sm3658/Pictures/SLF"
datadir = r'C:\Users\sarah\OneDrive - Drexel University\TAMG_Intelligent Systems\14. Projects\SLF_2020'
categories = ['eggs_cropped', 'noegg']
#

# Single image, trying to figure out which image size is good

for category in categories:
    path = os.path.join(datadir, category)  # path to images
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img)) # convert to gray scale bc colored is 3 times the size, if gray then add to img_array: cv2.IMREAD_GRAYSCALE
        plt.imshow(img_array)
        plt.show()
        break
    break

print(img_array)

# Try to resize them
img_size = 500
new_array = cv2.resize(img_array, (img_size, img_size))
plt.imshow(new_array) # if gray scale, then add cmap='gray'
plt.show()


# Resizing images from path and adding categorical variable for labels

training_data = []
img_size = 500


def create_training_data():
    for category in categories:
        path = os.path.join(datadir, category)  # path to images
        class_num = categories.index(category)
        for img in os.listdir(path):
            # some images might be broken or read error, so try except block
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()
print(len(training_data))  # total images

# Now shuffling so we are not like 'no egg' and then 'egg'
random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])

# Lets pack to variables before NN
x = []
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)

# -1 because all features, and 1 is for gray scale. If color images, then change 1 value to 3#####
x = np.array(x).reshape(-1, img_size, img_size, 3)

# Now saving the pre-processing. We don't want to keep tweaking the resizing
pickle_out = open('x_intel_color.pickle', 'wb')
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open('y_intel_color.pickle', 'wb')
pickle.dump(y, pickle_out)
pickle_out.close()

# # reading it back in
# pickle_in = open('x.pickle', 'rb')
# x = pickle.load(pickle_in)
# is now the image
x[1]
# label for x1
y[1]

