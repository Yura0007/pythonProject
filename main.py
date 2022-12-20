
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.image import Image
from tkinter import *
from PIL import Image
from kivy.app import App
import numpy as np
import cv2





my_image = '66.jpg'

class WindowManager(ScreenManager):

    screen_two = StringProperty("screen_two")
    image_source = StringProperty('66.jpg')




    def build(self):

        my_image = Image.open(self.image_source)
        my_image.save('./66.jpg')

        image = cv2.imread('./66.jpg')

        filterd_image = cv2.medianBlur(image, 7)

        output = image.copy()
        gray = cv2.cvtColor(filterd_image, cv2.COLOR_BGR2GRAY)
        rows = gray.shape[0]
        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 50,
                                   param1=150, param2=50,
                                   minRadius=1, maxRadius=100)

        if circles is not None:

            circles = np.round(circles[0, :]).astype("int")

            font = cv2.FONT_HERSHEY_SIMPLEX
            height = 40

        for number, (x, y, r) in enumerate(sorted(circles, key=lambda v: v[0] + (v[1] / height) * image.shape[1]),
                                           start=1):
            text = str(number)
            (tw, th), bl = cv2.getTextSize(text, font, 0.5, 2)  # So the text can be centred in the circle
            tw /= 2
            th = th / 2 + 2

            cv2.circle(output, (x, y), r, (0, 255, 0), 3)
            cv2.rectangle(output, (x - 10, y - 10), (x + 10, y + 10), (0, 128, 255), -1)
            cv2.putText(output, text, (x, y), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)


        cv2.imwrite('./66.jpg', output)










    def selected(self, filename):
        try:
            self.image_source = filename[0]
            my_image = Image.open(self.image_source)
            my_image.save('./66.jpg')

        except:
            pass

class ImageSelector(Screen):
    pass
class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ClassificationResultWindow(Screen):
    pass

class CountObjectsApp(App):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_two = StringProperty("screen_two")

if __name__ == "__main__":
    CountObjectsApp().run()














