# tb-and-pneumonia-detection
 classify pneumonia ,tb and normal person xray image

## Overview

This kernel was made in response to speed up the diagnosis by technicians. Happy deep learning!

To install dependencies run >pip install -r requirements.txt

Link to kaggle kernel : https://www.kaggle.com/subratasarkar32/normal-pneumonia-and-tb-classification

Link to datasets : https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia, https://www.kaggle.com/kmader/pulmonary-chest-xray-abnormalities, https://www.kaggle.com/maxjeblick/bert-pretrained-models

## Usage

### -detector.py
   Fork the repository

   Paste your file in the same directory as the script.

   run the script and input the file name.

   You get back the result.

   Enjoy the power of machine learning.

### - normal-pneumonia-and-tb-classification.ipynb
   Fork the repository.

   Power up jupyter notebook for python and open the .ipynb file provided.

   Then, just change the data preprocessing parts of the code to load and format your own data to match the preprocessing specifications and then run your notebook.

   If you lack hardware resources on your machine, then just run your notebook on kaggle/colab.Just upload your dataset seperately. It is a pretty unexpensive option. Trust me ;D

## How the project was built and how it works?

First we built a neural network model and then we trained it on dataset.

We used keras with python for building the model and training it.

Then we stored the keras model structure and weights to a hdf5 file.

We used kaggle for training our model as hardware resources for training the model were not available to us

Now , predictions can be made using the the hdf5 file.

We also made a tflite file from the hdf5 file so that in future the predictions can be made on mobile devices.

## Donation

If our project helped you save your time. You can give us a cup of coffee. :)

You can donate via PayPal


![Super sub](https://raw.githubusercontent.com/SubrataSarkar32/subratasarkar32.github.io/master/images/Supersub(200x200).jpg)


[![Donate](https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png)](https://paypal.me/subratasarkar32)   [Donate](https://paypal.me/subratasarkar32)
