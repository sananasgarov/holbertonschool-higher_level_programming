#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # I create the root element for the XML structure
    root = ET.Element("data")

    # I iterate through the dictionary and add each key-value pair as a child element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # I write the XML tree to the specified file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    # I parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    # I iterate through the XML elements and rebuild the dictionary
    for child in root:
        result[child.tag] = child.text

    # I return the reconstructed dictionary
    return result

