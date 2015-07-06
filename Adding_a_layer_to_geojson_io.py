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
from tempfile import mkstemp
import os
from qgisio import geojsonio

def run_script(iface):
    layer = QgsVectorLayer('/home/zia/Documents/Test/QGIS_Python_Book/union/building.shp', 'Building', 'ogr')
    name = layer.name()
    print name   
    handle, tmpfile = mkstemp(suffix='.geojson')
    os.close(handle)
    print handle, tmpfile
    crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.PostgisCrsId)
    error = QgsVectorFileWriter.writeAsVectorFormat(layer, tmpfile, 'utf-8', crs, 'Geojson', onlySelected = False)
    if error != QgsVectorFileWriter.NoError:
        print 'Unable to write geoJson'
    with open(str(tmpfile), 'r') as f:
        contents = f.read()
    os.remove(tmpfile)
    url = geojsonio._create_gist(contents, 'Layer exported from QGIS', name + '.geojson')
    QDesktopServices.openUrl(QUrl(url))
