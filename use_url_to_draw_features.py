import ast
import requests

response = requests.get('http://160.75.81.195:8080/postgis/pgr_aStarFromAtoB_without_SessionID/?long_st=28.4&lat_st=41.093&long_end=29.023&lat_end=41.0432')
print (response.status_code)

vectorLyr = QgsVectorLayer('LineString?crs=epsg:4326', 'Layer 1' , "memory")
vpr = vectorLyr.dataProvider()

#The following code will convert string response into a json content
geojson_dict = ast.literal_eval(response.content)

#points = []
for j in range(len(geojson_dict['features'])):
	points = []
	for i in range(len(geojson_dict['features'][j]['geometry']['coordinates'])):
		x = geojson_dict['features'][j]['geometry']['coordinates'][i][0]
		y = geojson_dict['features'][j]['geometry']['coordinates'][i][1]
		points.append(QgsPoint(x, y))
	line = QgsGeometry.fromPolyline(points)
	f = QgsFeature()
	f.setGeometry(line)
	vpr.addFeatures([f])

'''a = 1
points = []#
pointszz = []
for j in range(len(geojson_dict['features'])):
    if a == 1:
        for i in range(len(geojson_dict['features'][j]['geometry']['coordinates'])):
            x = geojson_dict['features'][j]['geometry']['coordinates'][i][0]
            y = geojson_dict['features'][j]['geometry']['coordinates'][i][1]
            z = [x, y]
            points.append(z)
            a += 1
    else:
        for i in range(len(geojson_dict['features'][j]['geometry']['coordinates'])):
            x = geojson_dict['features'][j]['geometry']['coordinates'][i][0]
            y = geojson_dict['features'][j]['geometry']['coordinates'][i][1]
            z = [x, y]
            pointszz.append(z)
        if set(points[len(points)-1]) == set(pointszz[0]):
            points = points + pointszz
        elif set(points[len(points)-1]) == set(pointszz[len(pointszz)-1]):
            pointszz.reverse()
            points = points + pointszz
        elif set(points[0]) == set(pointszz[0]):
            points.reverse()
            points = points + pointszz
        else:
            points.reverse()
            pointszz.reverse()
            points = points + pointszz'''


'''line = QgsGeometry.fromPolyline(points)
f = QgsFeature()
f.setGeometry(line)
vpr.addFeatures([f])'''

vectorLyr.updateExtents()
QgsMapLayerRegistry.instance().addMapLayer(vectorLyr)

def run_script(iface):
	print 'hi'