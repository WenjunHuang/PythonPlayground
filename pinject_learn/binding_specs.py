import pinject


class SomeClass:
    def __init__(self, long_name):
        self.long_name = long_name


class SomeReallyLongClassName:
    def __init__(self):
        self.foo = 'foo'


class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('long_name', to_class=SomeReallyLongClassName)


obj_graph = pinject.new_object_graph(binding_specs=[MyBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.long_name.foo)
