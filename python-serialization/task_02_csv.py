#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data = []

        # CSV faylını oxu
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data.append(row)

        # JSON faylına yaz
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
