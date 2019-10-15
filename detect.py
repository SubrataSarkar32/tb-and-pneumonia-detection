import pip
def install():
    if hasattr(pip, 'main'):
        pip.main(['install', 'keras', 'tensorflow','opencv-python','numpy'])
    else:
        pip._internal.main(['install', 'keras', 'tensorflow','opencv-python','numpy'])

try:
    import random,keras,cv2
    import os

    from keras.preprocessing import image
    from keras.models import load_model

    import numpy as np
    from keras.models import model_from_json
    import json
except:
    install()
def give_prediction(filename=''):
            '''
            Call this function with a filename of an image to get predictions
            '''
            path = os.path.abspath(filename)
            json_file = open('results/model_4.json', 'r')

            loaded_model_json = json_file.read()
            json_file.close()
            model = model_from_json(loaded_model_json)

            # load weights into new model
            model.load_weights("results/model_4.h5")
            #print("Loaded model from disk")
            
            img = cv2.imread(path)
            img = cv2.resize(img, (100, 100))
            pred = model.predict_classes(img.reshape(-1,100,100,3))
            class_label_list = ['TB','normal','pneumonia']
            #print(class_label_list[pred[0]])
            return class_label_list[pred[0]]

if __name__=="__main__":
    fname=input("Enter file name: ")
    resulty=give_prediction(fname)
    print(resulty)
