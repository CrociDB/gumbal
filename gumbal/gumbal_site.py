import yaml
import os
import shutil
import re

import gumbal_info
from gumbal_theme import GumbalTheme
from gumbal_theme import GumbalThemeConstants

class GumbalSite:
	def __init__(self, path):
		self.site_root_path = path;
		self.site_build_dir = "%s/site" % self.site_root_path

		site_path = "%s/site.yaml" % path
		site_file = open(site_path)
		site_text = site_file.read()

		self.site_obj = yaml.load(site_text)
		self.parse()

	def parse(self):
		self.site_name = self.site_obj['site_name']
		self.site_theme = GumbalTheme(self.site_root_path, self.site_obj['site_theme'])

		self.site_home = self.site_obj['site_home']
		self.site_pages_directory = self.site_obj['site_pages']

	def build(self):
		if os.path.isdir(self.site_build_dir):
			shutil.rmtree(self.site_build_dir)

		gumbal_info.print_message("\n")
		gumbal_info.print_message(" ~> Creating directory: \n\t%s" % self.site_build_dir)
		os.makedirs(self.site_build_dir)

		self._parse_index()

	def _parse_index(self):
		file_dir = "%s/index.html" % self.site_build_dir
		gumbal_info.print_message(" ~> Creating Index file: \n\t%s" % file_dir)

		index_contents = self.site_theme.get_index()
		index_replaced = self._parse_constant_value(index_contents, GumbalThemeConstants.SITE_TITLE, self.site_name)

		try:
			index_file = open(file_dir, "w")
			index_file.write(index_replaced)
			index_file.close()
		except IOError:
			gumbal_info.terminate("Error while creating file: %s" % file_dir)

	def _parse_constant_value(self, content, constant, value):
		rcontent = re.sub(r"\{%%[\s]{0,}gumbal:%s%%\}" % constant, value, content)
		return rcontent
