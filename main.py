import sublime
import sublime_plugin
from .vendor.darkdetect import isDark, isLight

def plugin_loaded():
	auto_color_scheme = AutoColorSchemeCommand(sublime_plugin.TextCommand)
	auto_color_scheme.run(sublime_plugin.TextCommand)

class AutoColorSchemeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if isDark():
			sublime.status_message('Change to dark theme.')
			self.dark()
		else:
			sublime.status_message('Change to light theme.')
			self.light()

	def update(self, scheme):
		s = sublime.load_settings('Preferences.sublime-settings')
		s.set("color_scheme", scheme)
		sublime.save_settings("Preferences.sublime-settings")

	def dark(self):
		self.update('Packages/auto-color-scheme/themes/GitHub_Dark.tmTheme')

	def light(self):
		self.update('Packages/auto-color-scheme/themes/Eleven_Light.tmTheme')
		