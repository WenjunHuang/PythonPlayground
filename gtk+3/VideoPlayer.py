import gi
import sys

gi.require_version('Gtk', '3.0')
gi.require_version('GdkQuartz', '3.0')
gi.require_version('Gst', '1.0')
from gi.repository import Gtk
from gi.repository import Gst
from gi.repository import Clutter

MRL = ""


class ApplicationWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Python-Vlc Media Player')

        self.playback_button = Gtk.Button()
        self.stop_button = Gtk.Button()
        self.play_image = Gtk.Image.new_from_icon_name(
            'gtk-media-play',
            Gtk.IconSize.MENU
        )
        self.pause_image = Gtk.Image.new_from_icon_name(
            'gtk-media-pause',
            Gtk.IconSize.MENU
        )
        self.stop_image = Gtk.Image.new_from_icon_name(
            'gtk-media-stop',
            Gtk.IconSize.MENU
        )
        self.playback_button.set_image(self.play_image)
        self.stop_button.set_image(self.stop_image)

        self.playback_button.connect('clicked', self.toggle_player_playback)
        self.stop_button.connect('clicked', self.stop_player)

        self.hbox = Gtk.Box(spacing=6)
        self.hbox.pack_start(self.playback_button, True, True, 0)
        self.hbox.pack_start(self.stop_button, True, True, 0)

        self.player = Gst.ElementFactory.make('playbin','player')
        # self.player.set_property
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)
        self.vbox.pack_start(self.player, True, True, 0)
        self.vbox.pack_start(self.hbox, False, False, 0)

        self.show_all()

    def toggle_player_playback(self):
        pass

    def stop_player(self):
        pass


MRL = sys.argv[1]
window = ApplicationWindow()
window.connect('delete-event', Gtk.main_quit)
Gtk.main()
