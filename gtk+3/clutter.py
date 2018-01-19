from gi.repository import GLib, Gtk, GtkClutter, Clutter, Gdk, GdkPixbuf

import sys


from random import random

BROWSERS = 42

class ClutterBrowser(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, title='ClutterBrowser', application=app)

        self.build_treeview()

        self.embed = GtkClutter.Embed()

        container = Clutter.Actor()
        self.embed.get_stage().add_child(container)

        self.actors = []

        for i in range(BROWSERS):
            actor = GtkClutter.Actor()
            #actor.set_x(i * 700)

            da = Gtk.DrawingArea()
            da.connect('draw', self.on_draw)

            actor.get_widget().add(da)
            container.add_child(actor)
            self.actors.append(actor)

        scw = Gtk.ScrolledWindow()
        scw.set_size_request(200, -1)
        scw.add(self._treeview)

        pane = Gtk.Paned()
        pane.add1(scw)
        pane.add2(self.embed)

        container.save_easing_state()
        container.set_easing_mode(Clutter.AnimationMode.EASE_IN_OUT_CUBIC)
        container.set_easing_duration(1500)

        self._container = container

        self.add(pane)

    def build_treeview(self):
        self._treemodel = Gtk.ListStore(str, str, int)
        self._treeview = Gtk.TreeView()
        self._treeview.set_model(self._treemodel)
        self._treeview.set_headers_visible(False)
        self._treeview.get_selection().connect('changed', self.on_changed)

        def select_first(*args):
            self._treeview.get_selection().select_path('0')
            self.on_changed(self._treeview.get_selection())
            return False

        GLib.timeout_add(500, select_first)

        self._treeview.append_column(
            Gtk.TreeViewColumn('Icon', Gtk.CellRendererPixbuf(), stock_id=0)
        )
        self._treeview.append_column(
            Gtk.TreeViewColumn('Name', Gtk.CellRendererText(), text=1)
        )

        for i in range(BROWSERS):
            self._treemodel.append([Gtk.STOCK_ABOUT, str('Browser #' + str(i)), i])

    def on_changed(self, selection):
        model, iterator = selection.get_selected()
        if iterator is not None:

            cr = self.embed.get_allocation()
            for idx, actor in enumerate(self.actors):
                actor.set_x(idx * cr.width)
                actor.set_width(cr.width)
                actor.set_height(cr.height)

            idx = model[iterator][2]
            self._container.set_x(idx * -cr.width)

    def on_draw(self, area, ctx):
        ctx.set_source_rgb(random(), random(), random())
        ctx.paint()


class ClutterBrowserApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
        GtkClutter.init(sys.argv)

    def do_activate(self):
        win = ClutterBrowser(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    app = ClutterBrowserApp()
    app.run(sys.argv)