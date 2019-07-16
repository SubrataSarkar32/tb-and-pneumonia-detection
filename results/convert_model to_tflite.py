#Convert keras model and weights to single file
import random,keras
import os

from keras.models import load_model

import numpy as np
from keras.models import model_from_json
import json

def convert_to_single_file(json_fname='',weight_file='',output_file=''):
            '''
            Call this function with json structure file name, weight file name and output file name(not necessary)
            to convert keras model to single file containing both model and weight 
            '''
            if json_fname!='' and weight_file!='':
                
                if output_file=='':
                    fn_list=json_fname.split('.')
                    output_file='.'.join([fn_list[0]+'converted','h5'])
                                         
                json_file = open(json_fname, 'r')

                loaded_model_json = json_file.read()
                json_file.close()
                model = model_from_json(loaded_model_json)

                # load weights into new model
                model.load_weights(weight_file)
                print("Loaded model from disk")
                model.save(output_file)
                print("Saved model to ",output_file)
                
#just change parameters and run
convert_to_single_file(json_fname='model_4.json',weight_file="model_4.h5",output_file='')
#Now run this in cmd prompt opened at the location where the file has been saved
#>tflite_convert --output_file=pneutbinfer.tflite --keras_model_file=model_4converted.h5
#Now you have the tflite file
