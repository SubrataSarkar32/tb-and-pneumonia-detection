# How to Deploy a Keras Model to Production


## Overview

We have designed and trained a convolutional neural network using keras. This will provide people with the required information before contacting the doctor and significantly speed up the process of diagnosis. We take the patient's x-ray image of the chest and then run our model and give the prediction. We have implemented a desktop app ,android app and flask web app.  Developed using [Theano](http://www.deeplearning.net/software/theano/) and the super simple [Keras](http://keras.io/) Library. Wrapped into a Webapp using [Flask](http://flask.pocoo.org/) Micro Framework.

## Dependencies

```sudo pip install -r requirements.txt```

## Usage

Once dependencies are installed, just run this to see it in your browser. 

```python app.py```

That's it! It's serving a saved Keras model to you via Flask. 

## Credits

The credits for this code go to [moinudeen](https://github.com/moinudeen). I've merely created a wrapper to get people started.

