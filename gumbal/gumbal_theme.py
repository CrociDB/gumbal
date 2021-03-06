import yaml
import sys

from os.path import isfile, join

import gumbal_info

class GumbalThemeConstants:
	SITE_TITLE='site_title'
	SITE_MENU='site_menu'

	PAGE_TITLE='page_title'
	PAGE_CONTENT='page_content'

class GumbalTheme:
	def __init__(self, root_path, theme_name):
		self.theme_root_path = "%s/themes/%s" % (root_path, theme_name)

		theme_path = "%s/themes/%s/theme.yaml" % (root_path, theme_name)
		theme_file = open(theme_path)
		theme_text = theme_file.read()

		self.theme_obj = yaml.load(theme_text)
		self.parse()

	def parse(self):
		self.theme_name = self.theme_obj['theme_name']
		self.theme_index = self.theme_obj['theme_index']
		self.theme_page = self.theme_obj['theme_page']

	def get_page(self):
		page_filename = join(self.theme_root_path, self.theme_page)
		return self.read_file(page_filename)

	def read_file(self, filename):
		try:
			ofile = open(filename)

			contents = ofile.read()
			ofile.close()
		except IOError:
			gumbal_info.terminate("Couldn't read file at: %s" % filename)

		return contents

	def build_menu(self, pages):
		menu_items = []

		for p in pages:
			menu_items.append('<li><a href=/%s.html>%s</a></li>' % (p['filename_free'], p['header']['page_name']))

		menu_html = '<ul>%s</ul>' % ''.join(menu_items)
		return menu_html

	def copy_assets(self): pass
