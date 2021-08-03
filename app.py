from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from tensorflow import keras
import cv2
import urllib
import numpy as np

Window.clearcolor=(0.5,0.5,0.5,0.5)

model=keras.models.load_model('skincancer.hdf5')

class MyLayout(BoxLayout):
        
    def predict(self):
        try:
            self.img.source= self.txt_input.text
            req = urllib.request.urlopen(self.img.source)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            img=cv2.resize(img,(224,224),interpolation = cv2.INTER_AREA)
            img=img.reshape(1,224,224,3)
            pre=model.predict(img)
            self.kq.text="Lành tính" if np.argmax(pre,axis=1)==0 else "Ác tính"
        except:
            print('Có lỗi xảy ra')
        
        
class MyKivyApp(App):
    
    def build(self):
        return MyLayout()

MyKivyApp().run()