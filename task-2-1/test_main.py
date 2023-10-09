import unittest
import os
import tempfile

from main import *

class TestSerializationAndDeserialization(unittest.TestCase):
    #Настройки для теста
    def setUp(self):
        self.data = {
            "ibuprofen": {"name": "ibuprofen", "prescription": "No", "best_before": "2 years"},
            "Adderall": {"name": "Adderall", "prescription": "Yes", "best_before": "1 year"},
            "Morphine": {"name": "Morphine", "prescription": "Yes", "best_before": "6 months"},
            "Chloropyramine": {"name": "Chloropyramine", "prescription": "No", "best_before": "1 year"}
        }

        self.temp_dir = tempfile.mkdtemp()
        self.xml_filename = os.path.join(self.temp_dir, "Pharmacy.xml")

    #Удаление временного файла .xml
    def tearDown(self):
        os.remove(self.xml_filename)
    
    def test_serialize_to_xml(self):
        #Тестирование сериализации, проверка на наличие файла
        serialize_to_xml(self.data, self.xml_filename)
        self.assertTrue(os.path.exists(self.xml_filename))
    
    def test_deserialize_from_xml(self):
        #Сериализуем в .xml, тестируем и проверяем результаты
        serialize_to_xml(self.data, self.xml_filename)
        deserialized_data = deserialize_from_xml(self.xml_filename)
        self.assertEqual(deserialized_data, self.data)

if __name__ == '__main__':
    unittest.main()