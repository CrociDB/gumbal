import os

import gumbal_info
from gumbal_site import GumbalSite

class GumbalParser:
	def parse(self, args):
		gumbal_info.print_header()

		if len(args) < 2:
			gumbal_info.print_message("Ops, you forgot to tell me what you want...")

		command = args[1]

		if command == "status":
			self.status()
		else:
			gumbal_info.print_message("Ops, command *%s* is unknown. Sorry." % command)

	def status(self):
		try:
			gumbal_site = GumbalSite(os.getcwd())
			gumbal_info.print_message("Current site loaded: %s" % gumbal_site.site_name)
		except Exception:
			gumbal_info.print_message("Ops, that doesn't look like a real site.")
