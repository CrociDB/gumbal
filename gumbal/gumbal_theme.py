import yaml

import gumbal_info

class GumbalTheme:
	def __init__(self, root_path, theme_name):
		theme_path = "%s/themes/%s/theme.yaml" % (root_path, theme_name)
		theme_file = open(theme_path)
		theme_text = theme_file.read()

		self.theme_obj = yaml.load(theme_text)
		self.parse()

	def parse(self):
		self.theme_name = self.theme_obj['theme_name']
