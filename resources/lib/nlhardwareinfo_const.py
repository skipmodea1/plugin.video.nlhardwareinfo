import os
import xbmcaddon

#
# Constants
# 
__settings__    = xbmcaddon.Addon(id='plugin.video.nlhardwareinfo')
__language__    = __settings__.getLocalizedString
__images_path__ = os.path.join( xbmcaddon.Addon(id='plugin.video.nlhardwareinfo').getAddonInfo('path'), 'resources', 'images' )
__addon__       = "plugin.video.nlhardwareinfo"
__plugin__      = "NlHardwareInfo"
__author__      = "Skipmode A1"
__url__         = ""
__date__        = "17 march 2013"
__version__     = "1.0"