import csv
from qgis.utils import iface

IN_FILE = "D:\\Alex\\Documents\\GIS\\res_local.csv"
SIRUTA_FIELD = "natCode"
OUT_FIELD = "prezenta_l"

layer = iface.activeLayer()
layer.startEditing()

for feature in layer.getFeatures():
    feature["dif_p"] = round(feature["prezenta_e"] - feature["prezenta_l"], 2)
