import pinject


class SomeClass:
    @pinject.annotate_arg('foo', 12345)
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', annotated_with='annot', to_instance='foo-with-annot')

    @pinject.provides('foo',annotated_with=12345)
    def provide_12345_foo(self):
        return '12345-foo'


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo)
