#our web app framework!

#you could also generate a skeleton from scratch via
#http://flask-appbuilder.readthedocs.io/en/latest/installation.html

#Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the
#HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine
#for you automatically.
#requests are objects that flask handles (get set post, etc)
from flask import render_template, jsonify, Flask, redirect, url_for, request, flash
#scientific computing library for saving, reading, and resizing images
#from scipy.misc import imsave, imread, imresize
#for matrix math
#import numpy as np
from werkzeug.utils import secure_filename
#for importing our keras model
#import keras.models
#for regular expressions, saves time dealing with string data
import re
import cv2
#system level operations (like loading files)
import sys
#for reading operating system data
import os
os.environ['KERAS_BACKEND'] = 'theano'
import keras
#from keras.models import load_model

from keras.models import model_from_json
#tell our app where our saved model is
sys.path.append(os.path.abspath("./model"))
#from load import *
#initalize our flask app
app = Flask(__name__)
#from scipy.misc import imread, imresize,imshow
#global vars for easy reusability
#global model, graph
#initialize these variables
#model, graph = init()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg','jpeg','png']

#decoding an image from base64 into raw representation
def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))


@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")

@app.route('/contact/',methods=['GET'])
def contact():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("contact.html")

@app.route('/about/',methods=['GET'])
def about():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("about.html")


@app.route('/predictly/',methods=['GET','POST'])
def predictly():
    if request.method == 'POST':
            f = request.files['file']
            if f.filename=='':
                   flash('No file part')
                   return redirect(request.url)
            if f and allowed_file(f.filename):
                  filename = secure_filename(f.filename)
                  f.save(os.path.join('keras-simple-webapp','static', 'xrayimgs', filename))
                  path = os.path.join('static','xrayimgs', filename)
                  #path = 'app/static/xrayimgs/'+filename

                  json_file = open('/home/subrata32/keras-simple-webapp/model/model_4.json', 'r')

                  loaded_model_json = json_file.read()
                  json_file.close()
                  model = model_from_json(loaded_model_json)

                  # load weights into new model
                  model.load_weights("/home/subrata32/keras-simple-webapp/model/model_4.h5")
                  print("Loaded model from disk")
                  print(path)
                  #out = model.predict(x)
                  img = cv2.imread(os.path.join('keras-simple-webapp','static', 'xrayimgs', filename), cv2.IMREAD_UNCHANGED)
                  img = cv2.resize(img, (100, 100))
                  if len(img.shape) > 2 and img.shape[2] == 4:
                      #convert the image from RGBA2RGB
                      img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                  pred = model.predict_classes(img.reshape(-1,100,100,3))
                  class_label_list = ['TB','normal','pneumonia']
                  print(pred[0])
                  '''
                  with graph.as_default():
                      #perform the prediction
                      out = model.predict(x)
                      img = cv2.imread(os.path.join('keras-simple-webapp','static', 'xrayimgs', filename), cv2.IMREAD_UNCHANGED)
                      img = cv2.resize(img, (100, 100))
                      pred = model.predict_classes(img.reshape(-1,100,100,3))
                      class_label_list = ['TB','normal','pneumonia']
                      print(pred[0])
                  '''

                  return render_template('predictly.html', title='Success', predictions=class_label_list[pred[0]], user_image=path)
            return render_template('index.html', title='Unsuccessful')
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 500

if __name__ == "__main__":
	#decide what port to run the app in
	#port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	#app.run(host='0.0.0.0', port=port)
        app.run()
	#optional if we want to run in debugging mode
	#app.run(debug=True)
