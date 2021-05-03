import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multilne=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Fav Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multilne=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Fav Color: "))
        # Add Input Box
        self.color = TextInput(multilne=False)
        self.add_widget(self.color)




class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()