from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import PyQt4.QtGui
import urllib

def run_script(iface):
    params = {
        'service': 'WFS',
        'version': '1.0.0',
        'request': 'GetFeature',
        'typeName': 'topp:tasmania_state_boundaries',
    }
    uri = 'http://maps.itu.edu.tr:8082/geoserver/topp/ows?' + urllib.unquote(urllib.urlencode(params))
    vlayer = QgsVectorLayer( uri, "my_table", "ogr" )
    
    urlWithParams = "url=http://maps.itu.edu.tr:8082/geoserver/sf/wms&format=image/png&layers=sfdem&styles=&crs=EPSG:26713"
    rlayer = QgsRasterLayer(urlWithParams, 'DEM', 'wms')
    
    QgsMapLayerRegistry.instance().addMapLayers([rlayer, vlayer])