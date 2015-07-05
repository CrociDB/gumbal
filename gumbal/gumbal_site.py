import yaml

import gumbal_info

class GumbalSite:
	def __init__(self, path):
		site_path = "%s/site.yaml" % path
		site_file = open(site_path)
		site_text = site_file.read()

		self.site_obj = yaml.load(site_text)
		self.parse()

	def parse(self):
		self.site_name = self.site_obj['site_name']
