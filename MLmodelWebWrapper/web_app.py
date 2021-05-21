import tensorflow as tf
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import cv2
import os

model = tf.keras.models.load_model('recognition_model.hdf5')
prediction_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

st.write("SLF eggs classification model")
imgFile = st.file_uploader("Please upload an image", type=["jpg", "png"])

def import_and_predict(image, model):
  img_size = 500
  #img=ImageOps.grayscale(image)
  #img=np.array(img)
  #img=np.array(image)
  img=np.array(image)
  img=cv2.resize(img, (img_size, img_size))
  #img=img.reshape((img_size,img_size))
  img=np.array(img).reshape(-1, img_size, img_size, 3)
  img=(img/255.0)               
  img=1-img
  return model.predict(img)


if imgFile is None:
  st.text("Upload an image for detection to work")
else:
  image = Image.open(imgFile)
  st.image(image, use_column_width=True)
  prediction = import_and_predict(image, model)
  print(prediction)
  print(prediction.shape)
  st.write(prediction)