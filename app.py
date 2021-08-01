from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=1        
        self.input_field=TextInput(text='Nhập url')
        self.add_widget(self.input_field)
        self.image_field=AsyncImage(source='https://images.unsplash.com/photo-1559028012-481c04fa702d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=635&q=80')
        self.add_widget(self.image_field)
        self.add_widget(Button(text='Load Image'))
        self.input_field.bind(text=self.change)
        
    def change(self,instance, text):
        self.image_field.source=text
        
        
class MyKivyApp(App):
    
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()

    def load_image(self):
        print('This mehtor on start is fired!!!')

MyKivyApp().run()