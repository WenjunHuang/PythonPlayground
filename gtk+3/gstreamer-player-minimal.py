import gi

gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst, GLib

import os

Gst.init()
mainloop = GLib.MainLoop()

pl = Gst.ElementFactory.make('playbin', 'player')
pl.set_property('uri', 'file://' + os.path.abspath('/Users/xxzyjy/Downloads/sintel.mkv'))
pl.set_property('volume', 0.2)
pl.set_state(Gst.State.PLAYING)
mainloop.run()
