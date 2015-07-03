from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import PyQt4.QtGui
import urllib

def run_script(iface):
    #Vector layer 
    params = {
        'service': 'WFS',
        'version': '1.0.0',
        'request': 'GetFeature',
        'typeName': 'topp:tasmania_state_boundaries',
    }
    uri = 'http://maps.itu.edu.tr:8082/geoserver/topp/ows?' + urllib.unquote(urllib.urlencode(params))
    vlayer = QgsVectorLayer( uri, "my_table", "ogr" )
    
    #Raster layer
    urlWithParams = "url=http://maps.itu.edu.tr:8082/geoserver/localhost/wms&format=image/png&layers=final&styles=&crs=EPSG:4326"
    rlayer = QgsRasterLayer(urlWithParams, 'DEM', 'wms')
    
    #Adding layers to the map
    QgsMapLayerRegistry.instance().addMapLayers([vlayer, rlayer])