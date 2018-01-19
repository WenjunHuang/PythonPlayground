import gi
import sys

gi.require_version('Gtk', '3.0')
gi.require_version('Clutter', '1.0')
gi.require_version('GtkClutter', '1.0')
from gi.repository import GtkClutter, Gtk

GtkClutter.init(sys.argv)
window = Gtk.Window(title="Cluter Gtk Example")
embed = GtkClutter.Embed(width_request=640,
                         height_request=480)
window.add(embed)

edit = Gtk.TextView(width_request=640,
                    height_request=480,
                    wrap_mode=Gtk.WrapMode.CHAR)
edit.get_buffer().set_text("Edit me!")
embed.get_stage().add_child(GtkClutter.Actor.new_with_contents(edit))

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
