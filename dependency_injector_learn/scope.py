import pinject

class SomeClass:
    def __init__(self,foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope = pinject.PROTOTYPE)
    def provide_foo(self):
        return object()

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
print(some_class_1 is some_class_2)
