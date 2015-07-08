# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.
from django.db.models.lookups import Year

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    print 'hi'
    prefix = '/home/zia/Documents/Test/QGIS_Python_Book/ms_rails_mstm'
    rails = QgsVectorLayer(prefix + 'ms_rails_mstm.shp', 'Railways', 'ogr')
    rules = (
             ('heavily used', '"DEN09CODE" > 3', 'red', (0, 6000000)),
             ('moderatly used', '"DEN09CODE" > 1 AND "DEN09CODE" < 4', 'orange', (0, 1500000)),
             ('lightly used', '"DEN09CODE" < 2', 'grey', (0, 250000)),
            )
    sym_rails = QgsSymbolV2.defaultSymbol(rails.geometryType())
    rend_rails = QgsRuleBasedRendererV2(sym_rails)
    root_rule = rend_rails.rootRule()
    for label, exp, color, scale in rules:
        #create a clone of the default rule
        rule = root_rule.children()[0].clone()
        #set the label exp and color
        rule.setLabel(label)
        rule.setFilterExpression(exp)
        rule.symbol().SetColor(QColor(color))
        #set the scale limits if they have been specified 
        if scale is not None:
            rule.setScaleMinDenom(scale[0])
            rule.setScaleMaxDenom(scale[1])
        #append the rule to the list of rules
        root_rule.appendChild(rule)
        
    root_rule.removeChildAt(0)
    rails.setRendererV2(rend_rails)
    
    jax = QgsVectorLayer('/home/zia/Documents/Test/QGIS_Python_Book/jackson/jackson.shp', 'Jackson', 'ogr')
    jax_style = {}
    jax_style['color'] = '#ffff00'
    jax_style['name'] = 'regular_star'
    jax_style['outline'] = '#000000'
    jax_style['outline-width'] = '1'
    jax_style['size'] = '8'
    sym_jax = QgsSimpleMarkerSymbolLayerV2.create(jax_style)
    jax.rendererV2().symbols()[0].changeSymbolLayer(0, sym_jax)
    
    ms = QgsVectorLayer('/home/zia/Documents/Test/QGIS_Python_Book/Mississippi/mississippi.shp', 'Missi', 'ogr')
    ms_style = {}
    ms_style['color'] = '#F7F5EB'
    sym_ms = QgsSimpleFillSymbolLayerV2.create(ms_style)
    ms.rendererV2().symbols()[0].changeSymbolsLayer(0, sym_ms)
    
    QgsMapLayerRegistry.instance().addMapLayers([jax, rails, ms])
    
    