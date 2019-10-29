import pinject

# provider bindings, which let you inject args named provide_something with provider functions; and
# provider methods, which are methods of binding specs that provide instances of some arg name.
class Foo:
    def __init__(self):
        self.forty_two = 42


class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_class=Foo, in_scope=pinject.PROTOTYPE)


class NeedsProvider:
    def __init__(self, provide_foo):
        self.provide_foo = provide_foo


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
needs_provider = obj_graph.provide(NeedsProvider)
print(needs_provider.provide_foo() is needs_provider.provide_foo())
