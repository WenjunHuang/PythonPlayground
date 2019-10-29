import random

import pinject


class Widget:
    def __init__(self, color, widget_polisher):
        self.color = color
        self.widget_polisher = widget_polisher


colors = ['red', 'green', 'blue']


class SomethingNeedingWidgets:
    def __init__(self, provide_widget):
        self.widget = provide_widget(colors[random.randint(0, 3)])


class SomeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    @pinject.inject(['widget_polisher'])
    def provide_widget(self, color, widget_polisher):
        return Widget(color, widget_polisher)

    def provide_widget_polisher(self):
        return 'widget-polisher'


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
obj1 = obj_graph.provide(SomethingNeedingWidgets)
obj2 = obj_graph.provide(SomethingNeedingWidgets)
print(obj1.widget.color, obj1.widget.widget_polisher)
print(obj2.widget.color, obj2.widget.widget_polisher)

print(obj1.widget is obj2.widget)
