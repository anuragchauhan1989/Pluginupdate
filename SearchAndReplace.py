import os
import sys

from filereader import search_replace

var_name = sys.argv[1]
var_value = sys.argv[2]

os.environ[var_name] = var_value
plugin_name = os.environ['plugin_name']
search_replace(plugin_name)





