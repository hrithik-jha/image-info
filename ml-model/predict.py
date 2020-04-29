from keras.preprocessing import image
from keras.models import model_from_json
import pandas as pd
import numpy as np


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train = pd.read_csv('./dataset/train.csv')


img = image.load_img('barry.jpg',target_size=(200,200,3))
img = image.img_to_array(img)
img = img/255


classes = np.array(train.columns[2:])
proba = loaded_model.predict(img.reshape(1,200,200,3))
top_3 = np.argsort(proba[0])[:-4:-1]
for i in range(3):
    print("{}".format(classes[top_3[i]])+" ({:.3})".format(proba[0][top_3[i]]))
