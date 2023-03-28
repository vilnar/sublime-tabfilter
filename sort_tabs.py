import sublime
import sublime_plugin
import time

SORT_TABS_KEY = "sort_tabs_key"

class SortTabs(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        view.settings().set(SORT_TABS_KEY, time.time())


def compare_tab_by_last_activation(t1, t2):
    x = t1.settings().get(SORT_TABS_KEY, 0)
    y = t2.settings().get(SORT_TABS_KEY, 0)
    return y - x