#!/usr/bin/env python3

import csv
from collections import defaultdict
import os

CSV_FILE = os.getenv("CSV_FILE", "presence_euro.csv")
OUT_FILE = os.getenv("OUT_FILE", "rw.csv")

SIRUTA_FIELD = os.getenv("SIRUTA_FIELD", "Siruta")
REGISTERED_FIELD = os.getenv("REGISTERED_FIELD", "Înscriși pe liste permanente")
VOTED_FIELD = os.getenv("VOTED_FIELD", "LT")

with open(CSV_FILE, "r", encoding="utf-8-sig") as csv_file, open(OUT_FILE, "w") as out_file:
    csv_data = csv.DictReader(csv_file)

    result = defaultdict(lambda: [0, 0])

    for row in csv_data:
        siruta = row[SIRUTA_FIELD]

        result[siruta][0] += int(row[REGISTERED_FIELD])
        result[siruta][1] += int(row[VOTED_FIELD])

    for loc_siruta in result:
        try:
            presence = round(result[loc_siruta][1] / result[loc_siruta][0] * 100, 2)

            print(f"{loc_siruta},{presence}", file=out_file)
        except:
            pass
            #out_file.write(f"{loc_siruta},NaN")
