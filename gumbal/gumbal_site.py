import yaml
import os
import shutil
import re

import markdown2

from os.path import isfile, join

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

	def create_menu(self):
		pages_directory = "%s/%s" % (self.site_root_path, self.site_pages_directory)
		files = [f for f in os.listdir(pages_directory) if isfile(join(pages_directory, f))]

		self.pages = []

		index_page = join(self.site_root_path, self.site_home)
		self.pages.append(self._load_and_parse_page(self.site_home, index_page))

		for f in files:
			filepath = join(pages_directory, f)
			page = self._load_and_parse_page(f, filepath)
			self.pages.append(page)

		self.menu_html = self.site_theme.build_menu(self.pages)

	def _load_and_parse_page(self, filename, filepath):
		page = self.load_markdown_page(filepath)

		page['header'] = yaml.load(page['header'])
		page['content'] = markdown2.markdown(page['content'])
		page['filename'] = filename
		page['filename_free'] = filename.split('.')[0]

		return page

	def create_template_table(self):
		self.template_table = {
			GumbalThemeConstants.SITE_TITLE: self.site_name,
			GumbalThemeConstants.SITE_MENU: self.menu_html
		}

	def build(self):
		if os.path.isdir(self.site_build_dir):
			shutil.rmtree(self.site_build_dir)

		gumbal_info.print_message("\n")
		gumbal_info.print_message(" ~> Creating directory: \n\t%s" % self.site_build_dir)
		os.makedirs(self.site_build_dir)

		self.create_menu()
		self.create_template_table()
		self._parse_pages()

	def _parse_pages(self):
		for p in self.pages:
			file_dir = "%s/%s.html" % (self.site_build_dir, p['filename_free'])
			gumbal_info.print_message(" ~> Creating *%s* page: \n\t%s" % (p['header']['page_name'], file_dir))

			page_table = {
				GumbalThemeConstants.PAGE_TITLE: p['header']['page_name'],
				GumbalThemeConstants.PAGE_CONTENT: p['content']
			}

			contents = self.site_theme.get_page()
			replaced = self.parse_all_page(contents, page_table)

			try:
				pfile = open(file_dir, "w")
				pfile.write(replaced)
				pfile.close()
			except IOError:
				gumbal_info.terminate("Error while creating file: %s" % file_dir)

	def parse_all_page(self, content, page_table={}):
		reg = re.compile(r"\{%[\s]{0,}gumbal::?([^%}]*)%\}")

		all_constants = reg.finditer(content)

		for c in all_constants:
			if c.group(1) in self.template_table:
				content = re.sub(c.group(0), self.template_table[c.group(1)], content)
			if c.group(1) in page_table:
				content = re.sub(c.group(0), page_table[c.group(1)], content)

		return content

	def _parse_constant_value(self, content, constant, value):
		rcontent = re.sub(r"\{%%[\s]{0,}gumbal:%s%%\}" % constant, value, content)
		return rcontent

	def load_markdown_page(self, filename):
		fcontent = self.read_file(filename)
		page_data = re.split(r"[\s]{0,}content:[\s]{0,}[\r]{0,}[\n]{1,}[~]{3,}[\s]{0,}[\r]{0,}[\n]{1,}", fcontent, 1)

		retobj = {
			'header': page_data[0],
			'content': page_data[1]
		}

		return retobj

	def read_file(self, filename):
		try:
			ofile = open(filename)

			contents = ofile.read()
			ofile.close()
		except IOError:
			gumbal_info.terminate("Couldn't read file at: %s" % filename)

		return contents
