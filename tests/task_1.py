import unittest
from unittest.case import TestCase
from unittest.mock import patch
from secretary_data import documents, directories, documents_list, new_document, document_deletion

# Тест основных функций по получению информации о документах, добавлении и удалении элементов из словаря
class TestFunctions(TestCase):
    def test_document_list(self):
        expected = ('passport "2207 876234" "Василий Гупкин"\ninvoice "11-2" "Геннадий Покемонов"\ninsurance "10006" "Аристарх Павлов"\n')
        result = documents_list(documents)
        self.assertEqual(result, expected)

    def test_new_document(self):
        new_doc_type = 'passport'
        new_doc_number = '7777'
        new_doc_name = 'Иванов'
        new_doc_shelf = '1'
        expected = (f'Документ номер {new_doc_number} был добавлен')
        result = new_document(documents, directories, new_doc_type, new_doc_number, new_doc_name, new_doc_shelf)
        self.assertEqual(result, expected)

    def test_document_deletion(self):
        doc_number = '333'
        expected = (f'Документ с номером {doc_number} не найден')
        result = document_deletion(documents, directories, doc_number)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()