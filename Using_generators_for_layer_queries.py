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
from query import query

def run_script(iface):
    pth = '/home/zia/Documents/Test/QGIS_Python_Book/MS_UrbanAnC10/MS_UrbanAnC10.shp'
    layer = QgsVectorLayer(pth, 'urban areas', 'ogr')
    q = (query(layer).where('POP > 50000').select('NAME10', 'POP', 'Arealand', 'POPDEN'))
    print q().next()