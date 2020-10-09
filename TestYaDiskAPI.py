import unittest
from unittest.mock import patch, Mock
from yadiskapi import YaDiskFolders

class TestGetData(unittest.TestCase):

    def setUp(self):
        self.ya_folder = YaDiskFolders()

    # декаратор patch получает доступ к подменяемой функции make_request
    # Внимание! Нужно обязательно указывать имя модуля!
    @patch('yadiskapi.YaDiskFolders.make_request')
    # передаем как аргумент функцию-пустышку, которая будет подменять в тесте make_request()
    def test_get_post(self, mock_make_request):
        # создаем объект Mock с нужными нам аттрибутами и их значениями
        mock_status_201=Mock(status_code=201, reason='CREATED', text='это тест!')
        # делаем так, чтобы в тесте make_request() = mock_make_request() возвращала наш Mock объект
        mock_make_request.return_value = mock_status_201

        # и вызываем тестируемую функцию:
        folder_name='testfolder6'
        resp = self.ya_folder.create_folder(folder_name)

        # проверки
        self.assertIsInstance(resp, list)
        self.assertEqual(resp[0],'CREATED')
        self.assertEqual(resp[1],folder_name)

# Запуск делается либо непосредственно из самой программы
if __name__ == '__main__':
    unittest.main()

# А можно из консоли:
# python -m unittest TestBuchProg.py