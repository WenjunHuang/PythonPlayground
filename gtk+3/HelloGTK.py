import gi
import sys

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Hello World')
        self.button = Gtk.Button(label='Click Here')
        handler_id = self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget: Gtk.Button):
        print('Hello World')


win = MyWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
sys.exit(Gtk.main())
