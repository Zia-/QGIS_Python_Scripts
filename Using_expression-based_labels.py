# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    # No error but not working
    pth = '/home/zia/Documents/Test/QGIS_Python_Book/MS_UrbanAnC10/MS_UrbanAnC10.shp'
    lyr = QgsVectorLayer(pth, 'urban areas', 'ogr')
    palyr = QgsPalLayerSettings()
    palyr.readFromLayer(lyr)
    palyr.fieldName = 'CASE WHEN "POP" > 50000 THEN "NAME10" END'
    palyr.enabled = True
    palyr.writeToLayer(lyr)
    QgsMapLayerRegistry.instance().addMapLayer(lyr)
