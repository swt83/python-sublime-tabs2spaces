import sublime, sublime_plugin

# class ExampleCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#       self.view.insert(edit, 0, "Hello, World!")

class ConvertTabsToSpaces(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        edit = view.begin_edit()
        view.run_command('expand_tabs', {"set_translate_tabs": True})
        view.end_edit(edit)
        #sublime.message_dialog("Converted endings.")