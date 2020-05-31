import sublime
import sublime_plugin
from .vendor.darkdetect import isDark, isLight

def plugin_loaded():
	autodetectCommand = AutodetectCommand(sublime_plugin.TextCommand)

class AutodetectCommand(sublime_plugin.TextCommand):
	def __init__(self, edit):
		self.run(edit)

	def run(self, edit):
		if isDark():
			self.dark()
		else:
			self.light()

	def update(self, scheme):
		s = sublime.load_settings('Preferences.sublime-settings')
		s.set("color_scheme", scheme)
		sublime.save_settings("Preferences.sublime-settings")

	def dark(self):
		self.update('Packages/auto-color-scheme/themes/GitHub_Dark.tmTheme')

	def light(self):
		self.update('Packages/auto-color-scheme/themes/GitHub_Light.tmTheme')
		