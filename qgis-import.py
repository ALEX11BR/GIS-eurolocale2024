import csv
from qgis.utils import iface

IN_FILE = "D:\\Alex\\Documents\\GIS\\res_local.csv"
SIRUTA_FIELD = "natCode"
OUT_FIELD = "prezenta_l"

with open(IN_FILE, "r") as in_file:
  in_reader = csv.reader(in_file)
  in_data = {line[0]: line[1] for line in in_reader}

  layer = iface.activeLayer()
  layer.startEditing()

  for feature in layer.getFeatures():
    try:
      feature[OUT_FIELD] = in_data[feature[SIRUTA_FIELD]]
      layer.updateFeature(feature)
    except:
      print(feature[SIRUTA_FIELD])
