GUMBAL_VERSION = 0.01

GUMBAL_HEADER = """ Gumbal v{0} - Static Website Generator 
"""

def print_header():
	print get_header()

def get_header():
	return GUMBAL_HEADER.format(GUMBAL_VERSION)

def print_message(message):
	print " %s" % message