from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phonebook = ["Nick Barty", "Jacob Madeley", "David Plummer"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widget.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.phonebook:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()

DynamicWidgetsApp().run()
