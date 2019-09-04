from flask import render_template, jsonify, Flask, redirect, url_for, request
from app import app

import numpy as np
import random,keras,cv2
import os

from keras.preprocessing import image
from keras.models import load_model

from keras.models import model_from_json
import json

@app.route('/')

#disease_list = ['Atelectasis', 'Consolidation', 'Infiltration', 'Pneumothorax', 'Edema', 'Emphysema', \
                  # 'Fibrosis', 'Effusion', 'Pneumonia', 'Pleural_Thickening', 'Cardiomegaly', 'Nodule', 'Mass', \
                  # 'Hernia']

@app.route('/upload')
def upload_file2():
   return render_template('index.html')
	
@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
      path = os.path.abspath(filename)
      json_file = open('model_4.json', 'r')

      loaded_model_json = json_file.read()
      json_file.close()
      model = model_from_json(loaded_model_json)

      # load weights into new model
      model.load_weights("model_4.h5")
      print("Loaded model from disk")
      
      img = cv2.imread(path)
      img = cv2.resize(img, (100, 100))
      pred = model.predict_classes(img.reshape(-1,100,100,3))
      class_label_list = ['TB','normal','pneumonia']
      print(pred[0])
      f.save(path)
      return render_template('uploaded.html', title='Success', predictions=class_label_list[pred[0]], user_image=path)


@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
