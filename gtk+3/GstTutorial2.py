import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init()
source = Gst.ElementFactory.make("videotestsrc", "source")
filter1 = Gst.ElementFactory.make("vertigotv")
sink = Gst.ElementFactory.make("autovideosink", "sink")
pipeline: Gst.Pipeline = Gst.Pipeline.new("test-pipeline")

if not pipeline or not source or not sink:
    raise RuntimeError("Not all elements could be created")

pipeline.add(source)
pipeline.add(filter1)
pipeline.add(sink)
source.link(filter1)
filter1.link(sink)
# if source.link(sink) != True:
#     raise RuntimeError("Elements could not be linked")

source.set_property("pattern",0)
pipeline.set_state(Gst.State.PLAYING)

mainLoop = GLib.MainLoop()
mainLoop.run()
