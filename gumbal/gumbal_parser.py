import os

import gumbal_info
from gumbal_site import GumbalSite

class GumbalParser:
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
		else:
			gumbal_info.print_error("Ops, command *%s* is unknown. Sorry." % command)

	def status(self):
		site = self.load_site()

	def build(self):
		site = self.load_site()
		if site == None: return

		site.build()

	def load_site(self):
		gumbal_site = None

		try:
			gumbal_site = GumbalSite(os.getcwd())
			gumbal_info.print_message("Current site loaded: %s" % gumbal_site.site_name)
			gumbal_info.print_message(" ~ Using theme: %s" % gumbal_site.site_theme.theme_name)
		except Exception as e:
			gumbal_info.print_error("Ops, something went wront. Is this a real site? More info: \n\n\t~> %s" % e)

		return gumbal_site
