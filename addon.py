#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from builtins import str
import sys
import xbmc

from resources.lib.nlhardwareinfo_const import ADDON, DATE, VERSION

xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGDEBUG)
xbmc.log("[ADDON] %s v%s (%s) is starting, ARGV = %s" % (ADDON, VERSION, DATE, repr(sys.argv)),
             xbmc.LOGDEBUG)

from resources.lib import nlhardwareinfo_list_play as plugin

plugin.Main()
