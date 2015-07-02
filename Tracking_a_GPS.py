import ast
import requests
import qgis.core
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import PyQt4.QtGui

def run_script(iface):
	#Collect http response 
	response = requests.get('http://160.75.81.195:8080/postgis/pgr_aStarFromAtoB_without_SessionID/?long_st=28.4&lat_st=41.093&long_end=29.023&lat_end=41.0432')
	#Create a vector layer inside the memory
	vectorLyr = QgsVectorLayer('Point?crs=epsg:4326', 'Layer 1' , "memory")
	#Collect vector layer data provider for editing
	vpr = vectorLyr.dataProvider()
	#The following code will convert string response into a json content
	geojson_dict = ast.literal_eval(response.content)
	#Following two list variables will collect the features 
	node_features = []
	nodes = []
	
	#Loop through the json to create point features
	for j in range(len(geojson_dict['features'])):
		x = geojson_dict['features'][j]['geometry']['coordinates'][0][0]
		y = geojson_dict['features'][j]['geometry']['coordinates'][0][1]
		pnt = QgsPoint(x, y)
		nodes.append(pnt)
		
	#Create multi point feature from list of point features	
	geom = QgsGeometry.fromMultiPoint(nodes)
	f = QgsFeature()
	f.setGeometry(geom)
	#One cannot add directly f QgsFeature into vector data provider
	node_features.append(f)
	vpr.addFeatures(node_features)
	vectorLyr.updateExtents()
	QgsMapLayerRegistry.instance().addMapLayer(vectorLyr)
	
	