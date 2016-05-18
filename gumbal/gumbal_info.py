import sys

GUMBAL_VERSION = 0.01

GUMBAL_HEADER = """
   ___  __  __  __  __  ____    __    __
  / __)(  )(  )(  \/  )(  _ \  /__\  (  )
 ( (_-. )(__)(  )    (  ) _ < /(__)\  )(__    v{0} - Static Website Generator
  \___/(______)(_/\/\_)(____/(__)(__)(____)

 ============================================================================
                                            https://github.com/CrociDB/gumbal

"""

def print_header():
	print get_header()

def get_header():
	return GUMBAL_HEADER.format(GUMBAL_VERSION)

def print_message(message):
	print " %s" % message

def print_error(message):
	print " [ERR] %s" % message

def terminate(message):
	print_error(message)
	sys.exit()
