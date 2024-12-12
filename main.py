from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
import arabic_reshaper
from bidi.algorithm import get_display

# Load the KV file
Builder.load_file('yourfile.kv')

class FarsiLabelContainer(BoxLayout):
    # StringProperty to hold the processed text
    bidi_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Original Farsi text
        farsi_text = "سلام دنیا" # "Hello world" in Farsi
        # Reshape the text
        reshaped_text = arabic_reshaper.reshape(farsi_text)
        # Apply the bidi algorithm
        self.bidi_text = get_display(reshaped_text)

class YourApp(App):
    def build(self):
        return FarsiLabelContainer()

if __name__ == '__main__':
    YourApp().run()
