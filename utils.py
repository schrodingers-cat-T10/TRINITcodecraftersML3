# prompt: write a python function to read images as a RGB format from cv2 and convert total feature array to numpy

import cv2
import numpy as np
from rich.progress import track
import os
import pickle
from tqdm.notebook import tqdm

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add


import tensorflow as tf
from tensorflow.keras.models import load_model

# load vgg16 model
vgg_model = VGG16()
# restructure the model
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)
# summarize


def vgg_predict_image(image: np.array) -> np.array:
    image = image.reshape((1, 224, 224, 3))
    return vgg_model.predict(image, verbose=0)


def read_images_as_rgb(image: np.array) -> np.array:
    """
    Reads images from a list of paths as RGB format and converts them to a numpy array.

    Args:
    image_paths: A list of paths to images.

    Returns:
    A numpy array containing the images as RGB format.
    """

    #image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))
    # Convert the image from BGR to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None


def predict_caption(model, image, tokenizer, max_length):
    # add start tag for generation process
    in_text = 'startseq'
    # iterate over the max length of sequence
    for i in range(max_length):
        # encode input sequence
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        # pad the sequence
        sequence = pad_sequences([sequence], max_length)
        # predict next word
        yhat = model.predict([image, sequence], verbose=0)
        # get index with high probability
        yhat = np.argmax(yhat)
        # convert index to word
        word = idx_to_word(yhat, tokenizer)
        # stop if word not found
        if word is None:
            break
        # append word as input for generating next word
        in_text += " " + word
        # stop if we reach end tag
        if word == 'endseq':
            break

    return in_text
import json

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

def load_tokenizer_and_model(tokenizer_path, model_path):
    with open(tokenizer_path, 'r') as f:
        tokenizer_config = json.load(f)

    tokenizer = Tokenizer()
    tokenizer.set_config(tokenizer_config)

    # Load your model
    custom_objects = {'Embedding': tf.keras.layers.Embedding}  # Add custom objects if needed
    model = load_model(model_path, custom_objects=custom_objects)

    return tokenizer, model







