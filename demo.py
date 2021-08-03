from tensorflow import keras
import cv2
import urllib
import numpy as np

model=keras.models.load_model('skincancer.hdf5')
req = urllib.request.urlopen('https://media.istockphoto.com/photos/basal-cell-carcinoma-benign-skin-cancer-basalcell-cancer-on-human-picture-id1221602178?k=6&m=1221602178&s=170667a&w=0&h=be8bB8BEXZTVz1EdkkVNGV2lUgSh5JY7j7YznCBzS58=')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)
img=cv2.resize(img,(224,224),interpolation = cv2.INTER_AREA)
img=img.reshape(1,224,224,3)
pre=model.predict(img)
print(np.argmax(pre,axis=1)==0)