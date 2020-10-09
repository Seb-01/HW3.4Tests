import unittest
from unittest.mock import patch
import appmod
import builtins

class TestBuch(unittest.TestCase):
    # добавляем несколько методов, начинающихся со слова test.
    # Каждый из этих методов будет тестировать функции по получению информации о документах,
    # добавлении и удалении элементов из словаря

    # запускается перед выполнением каждого теста в классе
    def setUp(self):
        print("method setUp")

    # запускается после каждого теста в классе
    def tearDown(self):
        print("method tearDown")

    """
    В этом блоке тестируем функции, которые принимают аргументы и возвращают результаты.
    """
    #тестируем функцию, которая возвращает полку, на которой находится заданный документ
    def test_shelfes1_of_doc2207_876234(self):
    # третий аргумент (не обязательный) - это текст сообщения, который выводится при поднятии исключения
        self.assertEqual(appmod.get_shelf_by_doc_num('2207 876234'),'1','Не верно указана полка документа!')
    def test_shelfes1_of_doc2207_11_2(self):
    # третий аргумент (не обязательный) - это текст сообщения, который выводится при поднятии исключения
        self.assertEqual(appmod.get_shelf_by_doc_num('11-2'),'1','Не верно указана полка документа!')
    def test_shelfes2_of_doc10006(self):
    # третий аргумент (не обязательный) - это текст сообщения, который выводится при поднятии исключения
        self.assertEqual(appmod.get_shelf_by_doc_num('10006'),'2','Не верно указана полка документа!')


    """
    В этом блоке тестируем функции, которые НЕ принимают аргументы и НЕ возвращают результаты.
    Но есть пользовательский ввод и вывод из/в консоль, который мы подменяем. 
    Не используем unittest (не нашел нормальной документации :-(( )
    """
    # тестируем функцию добавления документов
    def test_add_doc(self):
        #вводимые значения
        input_values = ["456790", "invoice", "Иван Грозный", "2"]
        # клонируем список (пригодится для проверки итогового вывода)
        input_data=input_values.copy()
        #выводимые в консоль значения
        output=[]

        # функция-имитация пользовательского ввода input
        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        #подменяем input в тестируемой функции
        builtins.input=mock_input
        # подменяем print в теcтируемой функции: Каждый раз, когда код в функции вызывает print,
        # лямбда-функция будет добавлять значение в список с именем output
        builtins.print = lambda s: output.append(s)

        # запускаем тестируемую функцию
        appmod.add_new_doc()

        # ожидаемый результат добавления документа
        result_str=f'\nДокумент №{input_data[0]}, тип: {input_data[1]}, владелец: {input_data[2]}, помещен на полку №{input_data[3]}!'
        # ожидаемый вывод appmod.add_new_doc()
        result_print_list=[
            'Введите номер документа: ',
            'Введите тип документа: ',
            'Введите имя владельца: ',
            'Введите номер полки: ',
            result_str
        ]

        # проверка
        assert output == result_print_list

    # тестируем функцию удаления документа по заданому номеру
    def test_del_doc(self):
        # вводимые значения
        input_values = "456790"
        # выводимые в консоль значения
        output = []

        # функция-имитация пользовательского ввода input
        def mock_input(s):
            output.append(s)
            return input_values

        # подменяем input в тестируемой функции
        builtins.input = mock_input
        # подменяем print в теcтируемой функции: Каждый раз, когда код в функции вызывает print,
        # лямбда-функция будет добавлять значение в список с именем output
        builtins.print = lambda s: output.append(s)

        # запускаем тестируемую функцию
        result=appmod.del_doc_by_num()

        # ожидаемый результат и вывод appmod.del_doc_by_num()
        result_list = [
            'Введите номер документа: ',
            f'Документ №{input_values} находится на полке № {result[1]}.',
            f'Документ №{input_values} успешно удален!'
        ]
        # ожидаемый

        # проверка
        assert output == result_list



    # тестируем вывод списка всех документов
    # с помощью MOCK имитируем return функции
    # @patch('appmod.get_doc_list', return_value='\nСписок всех документов:\npassport "2207 876234" "Василий Гупкин"\ninvoice "11-2" "Геннадий Покемонов"\ninsurance "10006" "Аристарх Павлов"\n')
    # def test_print_all_docs(self,get_doc_list):
    #     self.assertEqual((get_doc_list),'\nСписок всех документов:\npassport "2207 876234" "Василий Гупкин"\ninvoice "11-2" "Геннадий Покемонов"\ninsurance "10006" "Аристарх Павлов"\n')


# Запуск делается либо непосредственно из самой программы
    if __name__ == '__main__':
        unittest.main()

# А можно из консоли:
# python -m unittest TestBuchProg.py