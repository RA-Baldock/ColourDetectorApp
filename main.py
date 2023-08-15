import kivy_ios as kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
import cv2
import pickle
import numpy as np

class Logistic(Widget):
    Logistic_model = pickle.load(open('Logistic_model.sav', 'rb'))

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 100
        self.spacing = 50

        # create a label widget
        label = Label(text='Colour Detector App', font_size=40, bold=True, color=(0,0,1,1))
        self.add_widget(label)

        # create a button widget
        button = Button(text='Launch Camera', font_size=32, size_hint=(1, 0.1))
        button.bind(on_press=self.launch_app)
        self.add_widget(button)

        # create a stop button widget
        button = Button(text='Close App', font_size=32, size_hint=(1, 0.1))
        button.bind(on_press=self.close_app)
        self.add_widget(button)

    def launch_app(self, instance):
        self.clear_widgets()
        self.add_widget(ColourDetectorApp())

    def close_app(self, *args):
        App.get_running_app().stop()

class ColourDetectorApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50

        self.img=Image()
        self.add_widget(self.img)

        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 720)  # sets window to HD
        Clock.schedule_interval(self.update, 1.0 / 33.0)  # sets the update rate for the image

        close_button = Button(text="Close App", size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_app)
        self.add_widget(close_button)

    def update(self, dt):
        # display image from cam in opencv window
        _, frame = self.capture.read()
        height1, width1, _ = frame.shape

        cx = int(width1 / 2) # centres detection point
        cy = int(height1 / 2)

        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)  #creates circle around detected pixels

        pixel_center = frame[cy, cx]
        colour = Logistic.Logistic_model.predict(np.uint8(np.flip(pixel_center.reshape(-1, 3)))) #makes classification
        #print(pixel_center, colour)

        cv2.putText(frame, str(colour), (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (1, 1, 1), thickness=8) #prints classification

        # convert image to texture
        buf = cv2.flip(frame, 0).tobytes()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = texture1 # display texture (i.e. image)

    def close_app(self, instance):
        App.get_running_app().stop()

#Run application
class ColourDetector(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    ColourDetector().run()

