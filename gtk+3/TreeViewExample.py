import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

software_list = [("Firefox", 2002, "C++"),
                 ("Eclipse", 2004, "Java"),
                 ("Pitivi", 2004, "Python"),
                 ("Netbeans", 1996, "Java"),
                 ("Chrome", 2008, "C++"),
                 ("Filezilla", 2001, "C++"),
                 ("Bazaar", 2005, "Python"),
                 ("Git", 2005, "C"),
                 ("Linux Kernel", 1991, "C"),
                 ("GCC", 1987, "C"),
                 ("Frostwire", 2004, "Java")]


class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title='Treeview Filter Demo')
        self.set_border_width(10)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        self.software_liststore = Gtk.ListStore(str, int, str)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        self.language_filter = self.software_liststore.filter_new()
        self.language_filter.set_visible_func(self.language_filter_func)

        self.treeview: Gtk.TreeView = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(['Software', 'Release Year', 'Programming Language']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.buttons = []
        for prog_language in ['Java', 'C', 'C++', 'Python', 'None']:
            button = Gtk.Button(prog_language)
            self.buttons.append(button)
            button.connect('clicked', self.on_selection_button_clicked)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attch_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        for i, button in enumerate(self.butotns[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def language_filter_func(self, model, iter, data):
        if self.current_filter_language is None or self.current_filter_language == 'None':
            return True
        else:
            return
