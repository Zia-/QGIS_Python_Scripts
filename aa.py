from PyQt4.QtCore import *
from PyQt4.QtGui import *
import qtiles
import random 
from QtCore import QFileInfo

def run_script(iface):
    def randomColor(mix=(255,255,255)):
        red = random.randrange(0,256)
        green = random.randrange(0,256)
        blue = random.randrange(0,256)
        r,g,b = mix
        red = (red+r)/2
        green = (green+g)/2
        blue = (blue+b)/2
        return (red,green,blue)
    
    def done():
        print 'finished'
    
    shp = '/home/zia/Documents/Test/QGIS_Python_Book/countries/countries.shp'
    dir = '/home/zia/Documents/Test/QGIS_Python_Book/countries/tiles'
    
    layer = QgsVectorLayer(shp, 'countries', 'ogr')
    field = 'CNTRY_NAME'
    features = layer.getFeatures()
    categories = []
    
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
    
    tt = qtiles.tilingthread.TilingThread(layers, extent, minzoom, maxzoom, width, height, transp, quality, format, outputPath, rootDir, antialiasing, tmsConvention, mapUrl, viewer)
    tt.processFinished.connect(done)
    tt.start()
    
    
