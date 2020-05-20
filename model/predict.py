from keras.preprocessing import image
from keras.models import model_from_json
import pandas as pd
import numpy as np
from os import walk

TARGET = 'img/barry.jpg'

def predictGenre(tar=TARGET):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    train = pd.read_csv('./train.csv')

    img = image.load_img(tar ,target_size=(200,200,3))
    img = image.img_to_array(img)
    img = img/255


    # Classes need to be hardcoded, no need for reading. Plus Drama needs to be removed.
    classes = np.array(train.columns[2:])
    proba = loaded_model.predict(img.reshape(1,200,200,3))
    top_3 = np.argsort(proba[0])[:-4:-1]
    for i in range(3):
        print("{}".format(classes[top_3[i]])+" ({:.3})".format(proba[0][top_3[i]]))

if __name__ == "__main__":
    for i in range(3):
        f = []
        print("Cluster", i)
        patho = "../processing/cluster-" + str(i)
        for (dirpath, dirnames, filenames) in walk(patho):
            f.extend(filenames)
            break
        print(f)
        for gg in f:
            pathImg = patho + '/' + str(gg)
            print(pathImg)
            predictGenre(pathImg)
