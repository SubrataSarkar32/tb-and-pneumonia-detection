#Convert keras model and weights to single file
import random,keras
import os

from keras.models import load_model

import numpy as np
from keras.models import model_from_json
import json

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout


from keras.utils.np_utils import to_categorical
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization,Activation,MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler

vgg_model = keras.applications.vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224,224, 3))
# Convert it to Sequential
model = Sequential()
for layer in vgg_model.layers:
    model.add(layer)


# Now, check the model type, its Sequential! 
print(type(model))
#keras.models.Sequential


# Verify the model details
model.summary()
# Now, that its sequential, we can perform usual operations.
model.layers.pop()


# Freeze the layers 
for layer in model.layers:
    layer.trainable = False


# Add 'softmax' instead of earlier 'prediction' layer.
model.add(Conv2D(512, kernel_size = 3, activation='relu'))
model.add(BatchNormalization())
model.add(Flatten())
#model.add(Dropout(0.4))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()
def convert_to_single_file(json_fname='',weight_file='',output_file=''):
            '''
            Call this function with json structure file name, weight file name and output file name(not necessary)
            to convert keras model to single file containing both model and weight 
            '''
            if json_fname!='' and weight_file!='':
                '''
                if output_file=='':
                    fn_list=json_fname.split('.')
                    output_file='.'.join([fn_list[0]+'converted','h5'])
                                         
                json_file = open(json_fname, 'r')

                loaded_model_json = json_file.read()
                json_file.close()
                model = model_from_json(loaded_model_json)
                model.trainable=True
                '''

                # load weights into new model
                model.load_weights(weight_file)
                print("Loaded model from disk")
                model.trainable=True
                model.summary()
                model.save(output_file)
                print("Saved model to ",output_file)
                
#just change parameters and run
convert_to_single_file(json_fname='model_4.json',weight_file="model_4.h5",output_file='model_4convertedvgg.h5')
#Now run this in cmd prompt opened at the location where the file has been saved
#>tflite_convert --output_file=pneutbinfer.tflite --keras_model_file=model_4converted.h5
#Now you have the tflite file
