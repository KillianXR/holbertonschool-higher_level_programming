import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    function that serialize a Python dictionary into XML.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Function that deserialize XML data, into a python dictionnary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except Exception:
        return None