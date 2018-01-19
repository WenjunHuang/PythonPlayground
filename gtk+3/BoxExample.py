import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class BoxExample(Gtk.Window):
    def __init__(self):
        super().__init__(title='Box Example')
        self.box = Gtk.Box(spacing=16)
        self.add(self.box)

        self.button1 = Gtk.Button(label='Hello')
        self.button1.connect('clicked', self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label='Goodbye')
        self.button2.connect('clicked', self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget: Gtk.Widget):
        print("Hello")

    def on_button2_clicked(self, widget: Gtk.Widget):
        print("Goodbye")


win = BoxExample()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
