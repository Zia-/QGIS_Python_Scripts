params = {
    'service': 'WFS',
    'version': '1.0.0',
    'request': 'GetFeature',
    'typeName': 'topp:tasmania_state_boundaries',
}
uri = 'http://maps.itu.edu.tr:8082/geoserver/topp/ows?' + urllib.unquote(urllib.urlencode(params))
vlayer = QgsVectorLayer( uri, "my_table", "ogr" )