"""
shellboard - cross-platform framework that facilitates the development of a graphical interface for the command shell
            Credits:
        Author - highofolly
        Source - https://github.com/highofolly/shellboard
         Email - sw3atyspace@gmail.com
        GitHub - https://github.com/highofolly
Discord Server - https://discord.com/invite/jchJKYqNmK
       Youtube - https://www.youtube.com/@sw3aty702
"""

__version__ = "0.5.0a1"

from pkg_resources import iter_entry_points


def load_plugins():
    plugins = []
    for entry_point in iter_entry_points('shellboard.plugins'):
        plugin_class = entry_point.load()
        plugin_instance = plugin_class()
        plugins.append(plugin_instance)
    return plugins

