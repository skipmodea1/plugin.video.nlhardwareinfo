#
# Imports
#
from BeautifulSoup import BeautifulSoup
from nlhardwareinfo_const import __settings__, __language__, __images_path__, __addon__, __plugin__, __author__, __url__, __date__, __version__
from nlhardwareinfo_utils import HTTPCommunicator
import os
import re
import sys
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

#
# Main class
#
class Main:
    def __init__( self ):
        #
        # Videos
        #
        parameters = {"action" : "list-play", "plugin_category" : __language__(30000), "url" : "http://nl.hardware.info/tv/rss/podcast-video", "next_page_possible": "False"}
        url = sys.argv[0] + '?' + urllib.urlencode(parameters)
        listitem = xbmcgui.ListItem( __language__(30000), iconImage="DefaultFolder.png" )
        folder = True
        xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ] ), url = url, listitem=listitem, isFolder=folder)

        # Disable sorting...
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		
        # End of list...
        xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )