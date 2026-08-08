# main.py
#
# Copyright 2026 yiannis ioannides
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

from gettext import gettext as _

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import ThrowdownWindow


class ThrowdownApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='dev.yioannides.Throwdown',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/dev/yioannides/Throwdown')
        self.create_action('quit', lambda *_: self.quit(), ['<control>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('shortcuts', self.on_shortcuts_action, ['<control>question'])
        self.set_accels_for_action('win.next-trick', ['space'])

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ThrowdownWindow(application=self)
        win.present()

    def on_about_action(self, *args):
        about = Adw.AboutDialog(application_name='Throwdown',
                                application_icon='dev.yioannides.Throwdown',
                                developer_name='yiannis ioannides',
                                version='0.1.0',
                                issue_url='https://gitlab.com/yioannides/throwdown/issues/',
                                translator_credits=_('translator-credits'),
                                developers=['yiannis ioannides'],
                                copyright='© 2026 yiannis ioannides')
        about.present(self.props.active_window)

    def on_shortcuts_action(self, *args):
        builder = Gtk.Builder.new_from_resource('/dev/yioannides/Throwdown/shortcuts-dialog.ui')
        dialog = builder.get_object('shortcuts_dialog')
        dialog.present(self.props.active_window)

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    app = ThrowdownApplication()
    return app.run(sys.argv)
