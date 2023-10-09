import os
import xml.etree.ElementTree as ET
import dicttoxml

datapharmacy = {
    "ibuprofen": {"name": "ibuprofen", "prescription": "No", "best_before": "2 years"},
    "Adderall": {"name": "Adderall", "prescription": "Yes", "best_before": "1 year"},
    "Morphine": {"name": "Morphine", "prescription": "Yes", "best_before": "6 months"},
    "Chloropyramine": {"name": "Chloropyramine", "prescription": "No", "best_before": "1 year"}
}

def serialize_to_xml(data, filename):
    xml = dicttoxml.dicttoxml(data, attr_type=False, custom_root='Pills')
    print(str(xml.decode()))
    with open(filename, 'wb') as write_file:
        write_file.write(xml)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}

    for ss in root:
        pill_data = {}
        for s in ss:
            # Добавляем данные о таблетке в словарь
            pill_data[s.tag] = s.text  
        # Добавляем данные о таблетке в общий словарь
        data[ss.tag] = pill_data

    # Возвращаем десериализованные данные
    return data


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    xml_filename = os.path.join(script_directory, "Pharmacy.xml")

    print("\nSerialization ... \n")
    serialize_to_xml(datapharmacy, xml_filename)

    print("\nDeserialization ... \n")
    deserialize_from_xml(xml_filename)

if __name__ == "__main__":
    main()

