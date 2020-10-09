import pytest
import unittest
import appmod
from unittest.mock import patch, Mock

class TestBuchPyTest:
    """
    Тестируем функции с аргументами
    """

    #перед запуском тестового класса
    def SetUpClass(self):
        #открытие файлов и загрузка тестовых данных
        pass

    def TearDownClass(self):
        #закрытие файлов с данными
        pass

    def SetUp(self):
        print("method setup")

    def TearDown(self):
        print("method teardown")

    # тестируем функцию, которая возвращает полку, на которой находится заданный документ
    @pytest.mark.parametrize('arg, result',[('10006','2'), ('11-2','1')])
    def test_shelfes_of_doc2(self, arg, result):
        assert appmod.get_shelf_by_doc_num(arg) == result

    move_fixture = ['10006', '3']

    # еще один вариант "подмены" ввода/вывода в консоли
    # помним, что @patch требует указать 'модуль.функцию', которую заменяет
    # второй аргумент декаратора - источник "подставных" данных
    @patch('builtins.input', side_effect=move_fixture)
    # второй аргумент - отловщик вывода в консоль
    def test_move_doc_to_shelf(self, capsys):
        # запускаем тестируемую функцию
        appmod.move_doc_by_num()

        user_doc_number, user_shelf_number = TestBuchPyTest.move_fixture

        out, err = capsys.readouterr()
        assert out == f'Документ номер "{user_doc_number}" был перемещен на полку номер "{user_shelf_number}"\n'



tst=TestBuchPyTest()
tst.test_move_doc_to_shelf()

# вызываем тесты из командной строки:
# pytest -v TestBuchProgPytest.py
