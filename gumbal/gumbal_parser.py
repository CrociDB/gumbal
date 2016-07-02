import os

import gumbal_info
from gumbal_site import GumbalSite

class GumbalParser:
	def __init__(self, gumbal_path):
		self.gumbal_path = gumbal_path

	def parse(self, args):
		gumbal_info.print_header()

		if len(args) < 2:
			gumbal_info.print_error("Ops, you forgot to tell me what you want...")
			return;

		command = args[1]

		if command == "status":
			self.status()
		elif command == "build":
			self.build()
		elif command == "init":
			site_name = "gumbalsite"
			if len(args) > 2:
				site_name = args[2]

			self.init(site_name)
		else:
			gumbal_info.print_error("Ops, command *%s* is unknown. Sorry." % command)

	def status(self):
		site = self.load_site()

	def build(self):
		site = self.load_site()
		if site == None: return

		site.build()

	def init(self, name):
		site_path = os.getcwd()
		gumbal_path = os.path.dirname(self.gumbal_path)

		gumbal_info.print_message("Initializing site: %s" % name)

		try:
			GumbalSite.init(gumbal_path, site_path, name)
			gumbal_info.print_message("Site %s initialized!" % name)
		except Exception as e:
			gumbal_info.print_error("Ops, something went wrong while Initializing. More info: \n\n\t~> %s" % e)

	def load_site(self):
		gumbal_site = None

		try:
			gumbal_site = GumbalSite(os.getcwd())
			gumbal_info.print_message("Current site loaded: %s" % gumbal_site.site_name)
			gumbal_info.print_message(" ~ Using theme: %s" % gumbal_site.site_theme.theme_name)
		except Exception as e:
			gumbal_info.print_error("Ops, something went wront. Is this a real site? More info: \n\n\t~> %s" % e)

		return gumbal_site
