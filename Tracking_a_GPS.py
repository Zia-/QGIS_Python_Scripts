import ast
import requests



response = requests.get('http://160.75.81.195:8080/postgis/pgr_aStarFromAtoB_without_SessionID/?long_st=28.4&lat_st=41.093&long_end=29.023&lat_end=41.0432')
print (response.status_code)

vectorLyr = QgsVectorLayer('Point?crs=epsg:4326', 'Layer 1' , "memory")
vpr = vectorLyr.dataProvider()

#The following code will convert string response into a json content
geojson_dict = ast.literal_eval(response.content)

for j in range(len(geojson_dict['features'])):
	x = geojson_dict['features'][j]['geometry']['coordinates'][0][0]
	y = geojson_dict['features'][j]['geometry']['coordinates'][0][1]
	pnt = QgsGeometry.fromPoint(QgsPoint(x, y))
	f = QgsFeature()
	f.setGeometry(pnt)
	vpr.addFeatures([f])

vectorLyr.updateExtents()
QgsMapLayerRegistry.instance().addMapLayer(vectorLyr)


