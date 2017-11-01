# modules
import os
import sys
import urllib
from splinter import Browser
from optparse import OptionParser

# parser options


parser = OptionParser(usage="%prog -u URL -t text [-d DRIVER][-q][-s]", version="%prog 1.0")
parser.add_option("-u", "--url", dest="url", help="url to test", )
parser.add_option("-t", "--text", dest="txt", help="text to search", )
parser.add_option("-d", "--driver", dest="driver", help="driver used", default='chrome')
parser.add_option("-s", "--headless", dest="headless",action="store_true",
                  default=False, help="headless")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

required="url txt".split()
for r in required:
    if options.__dict__[r] is None:
        parser.error("parameter %s required"%r)

# settings

url = options.url

# init
browser = Browser(options.driver,headless=options.headless)

# functions
def is_text_present(url,txt) :
    print url

    try :
        browser.visit(url)
        status = urllib.urlopen(url).getcode()
        return status,browser.is_text_present(txt)
    except :
        sys.exit("Server not found")

# main
# print "Testing..."
print "Options:",options
action = is_text_present(url,options.txt)
if action != (200,True) :
    sys.exit(action)
