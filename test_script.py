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
import PyQt4.QtGui

def run_script(iface):
    mapreg = QgsMapLayerRegistry.instance()
    mapreg.removeAllMapLayers()
    wb = QgsVectorLayer('/home/zia/Documents/Data/ITU/Campus ITU Shapefiles/campus_shp_4326/campus_info.shp', 'world_borders', 'ogr')
    mapreg.instance().addMapLayer(wb)
    renderer = wb.rendererV2()
    symb = renderer.symbol()
    symb.setColor(QColor(Qt.red))
    wb.setCacheImage(None)
    wb.triggerRepaint()
    iface.refreshLegend(wb)
