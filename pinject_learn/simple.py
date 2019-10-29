import pinject


class OuterClass:
    @pinject.copy_args_to_internal_fields
    def __init__(self, inner_class):
        pass


class InnerClass:
    def __init__(self):
        self.forty_two = 42


obj_graph = pinject.new_object_graph(modules=None, classes=[OuterClass, InnerClass])
outer_class = obj_graph.provide(OuterClass)
print(outer_class._inner_class.forty_two)
