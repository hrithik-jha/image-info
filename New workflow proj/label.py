from predict import predictGenre
from keras.preprocessing import image
import os
from keras.models import model_from_json
import pandas as pd
import numpy as np
import csv


images = []
for name in os.listdir("out/MI3"):
    p="out/MI3/"+name
    img = image.load_img(p ,target_size=(200,200,3))
    img = image.img_to_array(img)
    img = img/255

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    train = pd.read_csv('dataset/train.csv')

    # img = image.load_img(picture ,target_size=(200,200,3))
    # img = image.img_to_array(img)
    # img = img/255
    

    # Classes need to be hardcoded, no need for reading. Plus Drama needs to be removed.
    classes = np.array(train.columns[2:])
    proba = loaded_model.predict(img.reshape(1,200,200,3))
    top_3 = np.argsort(proba[0])[:-4:-1]
    result={}
    rows=[]

    for i in range(3):
        print("{}".format(classes[top_3[i]])+" ({:.3})".format(proba[0][top_3[i]]))
        result[classes[top_3[i]]]=proba[0][top_3[i]]
        if(i==0):
            continue
        else:
            rows.append([p,classes[top_3[i]]])
    with open('MI3.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)