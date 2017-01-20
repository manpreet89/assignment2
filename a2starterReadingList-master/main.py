"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder

# Create your main program in this file, using the ReadingListApp class

class ReadingListApp(App):
    def build(self):
        self.title = " Reading list 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root
    pass

ReadingListApp().run()
