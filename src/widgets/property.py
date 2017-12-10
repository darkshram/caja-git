#!/usr/bin/python2
"""
Caja git pluging to show useful information under any
git directory

Author : Bilal Elmoussaoui (bil.elmoussaoui@gmail.com)
Website : https://github.com/bil-elmoussaoui/nautilus-git
Licence : GPL-3.0
caja-git is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
caja-git is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with caja-git. If not, see <http://www.gnu.org/licenses/>.
"""
from imp import load_source
from os import environ, path

from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk


git = load_source("git", path.join(environ["MODELS_DIR"], "git.py"))
watchdog = load_source("watchdog", path.join(environ["MODELS_DIR"],
                                             "watchdog.py"))
branch = load_source("branch", path.join(environ["WIDGETS_DIR"],
                                         "branch.py"))
compare = load_source("compare", path.join(environ["WIDGETS_DIR"],
                                           "compare.py"))


class CajaPropertyPage:
    """Property page main widget class."""

    def __init__(self, git_uri):
        self._git = git.Git(git_uri)
        self._watchdog = watchdog.WatchDog(self._git.dir)
        self._watchdog.connect("refresh", self._refresh)

        self._builder = Gtk.Builder()
        self._builder.add_from_resource('/com/caja/git/ui/property.ui')
        self._build_widgets()

    @property
    def main(self):
        return self._builder.get_object("main")

    def _build_widgets(self):
        """Build needed widgets."""
        self._builder.get_object("branch").set_text(self._git.get_branch())
        status = self._git.get_status()

        status_widgets = ["added", "removed", "modified"]
        for widget_name in status_widgets:
            count = str(len(status[widget_name]))
            widget = self._builder.get_object(widget_name)
            widget.set_text(_("{0} file.").format(count))

    def _refresh(self, event):
        branch = self._builder.get_object("branch")
        branch.set_text(self._git.get_branch())
        branch.show()
