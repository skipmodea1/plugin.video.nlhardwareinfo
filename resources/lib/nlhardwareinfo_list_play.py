#
# Imports
#
from BeautifulSoup import BeautifulSoup
from nlhardwareinfo_const import __addon__, __settings__, __language__, __images_path__, __date__, __version__
from nlhardwareinfo_utils import HTTPCommunicator
import os
import re
import sys
import urllib, urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

#
# Main class
#
class Main:
	

			
	#
	# Init
	#
# 	def __init__( self ) :
# 		# Get plugin settings
# 		self.DEBUG = __settings__.getSetting('debug')
# 		
# 		if (self.DEBUG) == 'true':
# 			xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s, %s = %s" % ( __addon__, __version__, __date__, "ARGV", repr(sys.argv), "File", str(__file__) ), xbmc.LOGNOTICE )
# 
# 		# Parse parameters...
# 		if len(sys.argv[2]) == 0:
# 			self.plugin_category = __language__(30000)
# 			self.video_list_page_url = "http://nl.hardware.info/tv/rss-private/streaming"
# 			self.next_page_possible = "False"
# 		else:
# 			self.plugin_category = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['plugin_category'][0]
# 			self.video_list_page_url = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['url'][0]
# 			self.next_page_possible = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['next_page_possible'][0]
# 		
# 		if self.next_page_possible == 'True':
# 		# Determine current item number, next item number, next_url
# 			pos_of_page		 			 	 = self.video_list_page_url.rfind('?page=')
# 			if pos_of_page >= 0:
# 				page_number_str			     = str(self.video_list_page_url[pos_of_page + len('?page='):pos_of_page + len('?page=') + len('000')])
# 				page_number					 = int(page_number_str)
# 				page_number_next			 = page_number + 1
# 				if page_number_next >= 100:
# 					page_number_next_str = str(page_number_next)
# 				elif page_number_next >= 10:
# 					page_number_next_str = '0' + str(page_number_next)
# 				else:				
# 					page_number_next_str = '00' + str(page_number_next)
# 				self.next_url = str(self.video_list_page_url).replace(page_number_str, page_number_next_str)
# 			
# 				if (self.DEBUG) == 'true':
# 					xbmc.log( "[ADDON] %s v%s (%s) debug mode, %s = %s" % ( __addon__, __version__, __date__, "self.next_url", str(urllib.unquote_plus(self.next_url)) ), xbmc.LOGNOTICE )
# 	
# 		#
# 		# Get the videos...
# 		#
# 		self.getVideos()
# 	
# 	#
# 	# Get videos...
# 	#
# 	def getVideos( self ) :
		#
		# Init
		#
# 		titles_and_thumbnail_urls_index = 0
		
	# 
	# Get HTML page...
	#
	video_list_page_url = "http://www.armlook.com/episode/armenia-tv/harazat-tshnami/episode-414-anons/3222"
	html_source = HTTPCommunicator().get( video_list_page_url )

	# Parse response...
	soup = BeautifulSoup( html_source )
	
	#<iframe width="853" height="480" src="//www.youtube.com/embed/4ALIehnpw8M" frameborder="0" allowfullscreen></iframe>
	items = soup.findAll('iframe', attrs={'src': re.compile("www.youtube.com/embed/")}, limit=1)
	for item in items :
		src = str(item["src"])	
		pos_of_last_slash = src.rfind("/")
		youtubeID = src[pos_of_last_slash + 1:]
		print "youtubeID:" + youtubeID
		youtube_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % youtubeID

		playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
		playlist.clear()
	
		title = ""
		thumbnail_url = ""
		plot = ""
		genre = ""
		video_url = "plugin://plugin.video.youtube/?action=play_video&videoid=85jxv_jO9mk"
 		listitem = xbmcgui.ListItem( title, iconImage="DefaultVideo.png", thumbnailImage=thumbnail_url )
 		xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listitem)
 		listitem.setInfo( "video", { "Title": title, "Studio" : "Dumpert", "Plot" : plot, "Genre" : genre } )
 		playlist.add( video_url, listitem )
		
#		 Close wait dialog...
		dialogWait = xbmcgui.DialogProgress()
 		dialogWait.close()
 		del dialogWait
		
		# Play video...
		xbmcPlayer = xbmc.Player()
		xbmcPlayer.play( playlist )