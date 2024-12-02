import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from tensorflow.keras.preprocessing import image

label_map = {'Chicken Pox': 0, 'Measles': 1, 'Monkey Pox': 2}

def getType(id):
    return list(label_map.keys())[list(label_map.values()).index(id)]

# predict new images
def predictImagesClass(model_name, image_data, image_width, image_height):
    model = tf.keras.models.load_model(model_name)
    img = image.load_img(image_data, target_size=(image_width, image_height))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    res = getType(np.argmax(prediction))
    return res