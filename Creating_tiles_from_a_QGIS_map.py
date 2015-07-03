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
import qtiles
import random 

#function to generate random colors
def randomColor(mix=(255,255,255)):
    red = random.randrange(0,256)
    green = random.randrange(0,256)
    blue = random.randrange(0,256)
    r,g,b = mix
    red = (red+r)/2
    green = (green+g)/2
    blue = (blue+b)/2
    return (red,green,blue)

def run_script(iface):
    shp = '/home/zia/Documents/Test/QGIS_Python_Book/countries/countries.shp'
    dir = '/home/zia/Documents/Test/QGIS_Python_Book/countries/tiles'
    
    layer = QgsVectorLayer(shp, 'countries', 'ogr')
    field = 'CNTRY_NAME'
    features = layer.getFeatures()
    categories = []
    
    #generate color symbols
    for feature in features:
        country = feature[field]
        sym = QgsSymbolV2.defaultSymbol(layer.geometryType())
        r,g,b = randomColor()
        sym.setColor(QColor(r,g,b,255))
        category = QgsRendererCategoryV2(country, sym, country)
        categories.append(category)
        
    renderer = QgsCategorizedSymbolRendererV2(field, categories)
    layer.setRendererV2(renderer)
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    
    #prepare variables for qtiles method
    canvas = iface.mapCanvas()
    layers = canvas.mapSettings().layers()
    extent = canvas.extent()
    minzoom = 0
    maxzoom = 5
    width = 256
    height = 256
    transp = 255
    quality = 70
    format = 'PNG'
    outputPath = QFileInfo(dir)
    rootDir = 'countries'
    antialiasing = False
    tmsConvention = True
    mapUrl = False
    viewer = True
    
    #this message is not poping up though after the tiling execution
    def done():
        #print 'finished'
        QgsMessageLog.logMessage("This is a message from the Python Console", "Python Console")
    
    tt = qtiles.tilingthread.TilingThread(layers, extent, minzoom, maxzoom, width, height, transp, quality, format, outputPath, rootDir, antialiasing, tmsConvention, mapUrl, viewer)
    tt.processFinished.connect(done)
    tt.start()
    