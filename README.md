# tb-and-pneumonia-detection
 classify pneumonia ,tb and normal person xray image

## Overview

This kernel was made in response to "Dream Big Championship" held by "Internshala". Happy machine learning!

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

If my projects helped you save your time. You can give me a cup of coffee. :)

You can donate via BHIM UPI


![Super sub](https://raw.githubusercontent.com/SubrataSarkar32/subratasarkar32.github.io/master/images/Supersub(200x200).jpg)


[![Donate](https://raw.githubusercontent.com/SubrataSarkar32/subratasarkar32.github.io/master/images/bhimupi(100x15).jpg)](upi://pay?pn=Subrata%20Sarakar&pa=9002824700%40upi&tn=Donation&am=&cu=INR&url=http%3A%2F%2Fupi.link%2F)   [Donate](upi://pay?pn=Subrata%20Sarakar&pa=9002824700%40upi&tn=Donation&am=&cu=INR&url=http%3A%2F%2Fupi.link%2F)


OR

Scan this QR Code to open your UPI Payment App
![QR code](https://raw.githubusercontent.com/SubrataSarkar32/subratasarkar32.github.io/master/images/qrpay.png)
