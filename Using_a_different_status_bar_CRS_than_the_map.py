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
    pth = '/home/zia/Documents/Test/QGIS_Python_Book/MSCities_Geo_Pts/MSCities_Geo_Pts.shp'
    lyr = QgsVectorLayer(pth, 'cities', 'ogr')
    QgsMapLayerRegistry.instance().addMapLayer(lyr)
    msg = 'Alternate crs (x : %s , y : %s)'
    iface.mainWindow().statusBar().showMessage(msg % ('--', '--'))
    def listenxy(point):
        crssrc = iface.mapCanvas().mapRenderer().destinationCrs()
        crsdest = QgsCoordinateReferenceSystem(3815)
        xform = QgsCoordinateTransform(crssrc, crsdest)
        xpoint = xform.transform(point)
        iface.mainWindow().statusBar().showMessage(msg % (xpoint.x(), xpoint.y()))
    QObject.connect(iface.mapCanvas(), SIGNAL('xyCoordinates(const QgsPoint &)'), listenxy)
        