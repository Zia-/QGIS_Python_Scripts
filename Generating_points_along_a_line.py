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
import processing

def run_script(iface):
    line = QgsVectorLayer('/home/zia/Documents/Test/QGIS_Python_Book/path/path.shp', 'Line', 'ogr')
    QgsMapLayerRegistry.instance().addMapLayer(line)
    
    # The following grass function cant be executed. But the same can be viewed from processing toolbox.
    #processing.runandload('grass:v.to.points', line, '1000', False, False, True, '435727.015026, 458285.819185, 5566442.32879, 5591754.78979', -1, 0.0001, 0, None)
    processing.runandload('qgis:randompointsinextent', '435727.015026, 458285.819185, 5566442.32879, 5591754.78979', 100, 100, None)
    
