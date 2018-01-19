import gi

gi.require_version('Clutter', '1.0')
from gi.repository import Clutter
import sys

Clutter.init(sys.argv)

red = Clutter.Actor(x=0,
                    y=0,
                    width=200,
                    height=200,
                    background_color=Clutter.Color.new(255, 0, 0, 255))

green = Clutter.Actor(x=200,
                      y=0,
                      width=200,
                      height=200,
                      background_color=Clutter.Color.new(0, 255, 0, 255))

blue = Clutter.Actor(x=0,
                     y=200,
                     width=200,
                     height=200,
                     background_color=Clutter.Color.new(0, 0, 255, 255))

yellow = Clutter.Actor(x=200,
                       y=200,
                       width=200,
                       height=200,
                       background_color=Clutter.Color.new(255, 255, 0, 255))

container = Clutter.Actor(x=0,
                          y=0,
                          width=400,
                          height=400)
container.save_easing_state()
container.set_easing_mode(Clutter.AnimationMode.EASE_IN_OUT_CUBIC)
container.set_easing_duration(400)

for rec in [red, green, blue, yellow]:
    container.add_child(rec)

stage = Clutter.Stage(width=200,
                      height=200)
stage.add_child(container)


def on_stage_key_press(a, event: Clutter.KeyEvent):
    key = event.keyval
    if key == Clutter.KEY_Up:
        container.props.y = 0
    elif key == Clutter.KEY_Down:
        container.props.y = -200
    elif key == Clutter.KEY_Left:
        container.props.x = 0
    elif key == Clutter.KEY_Right:
        container.props.x = -200
    else:
        return False

    return True


stage.connect("key_press_event", on_stage_key_press)

stage.show_all()
stage.connect("delete-event", lambda s, e: Clutter.main_quit())
Clutter.main()
