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


def run_script(iface):
    pth = '/home/zia/Documents/Test/QGIS_Python_Book/ms_rails_mstm/ms_rails_mstm.shp'
    lyr = QgsVectorLayer(pth, 'railroads', 'ogr')
    total = 0
    for f in lyr.getFeatures():
        geom = f.geometry()
        total += geom.length()
    
    print '%0.2f total kilometers of rails' % (total/1000)
