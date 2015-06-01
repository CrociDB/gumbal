import gumbal_info

class GumbalParser:
	def parse(self, args):
		gumbal_info.print_header()

		if len(args) < 2:
			gumbal_info.print_message("Ops, you forgot to tell me what you want...")
