
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def is_doc_exist(doc_num):
    """
    Проверка на существование документа
    :param doc_num:
    :return:
    """
    res_val = False

    for doc in documents:
        if doc["number"] == doc_num:
            res_val = True
            break

    return res_val

# добавление новой полки - as
def add_new_shelf_num():
    target_shelf_num = input('Введите новый номер полки: ')
    docs_num = []

    if target_shelf_num in directories.keys():
        # полка уже существует:
        print(f'Полка с номером {target_shelf_num} уже существует!')
        answer = input(f'Желаете добавить новую полку (Y/N)?')
        if answer == 'Y' or answer == 'y':
            print(f'Полка с номером {target_shelf_num} добавлена!')
            directories.setdefault(target_shelf_num, docs_num)
    else:
        print(f'Полка с номером {target_shelf_num} добавлена!')
        directories.setdefault(target_shelf_num, docs_num)


# переносит документа на целевую полку - m
def move_doc_by_num():
    doc_num = input('Введите номер документа: ')
    target_shelf_num = input('Введите новый номер полки: ')
    name = ''

    # ищем документ
    for docs in documents:
        if doc_num == docs["number"]:
            name = docs["name"]

    # результат поиска документа:
    if name != '':
        # документ найден!
        # проверяем полку
        shelf_num = get_shelf_by_doc_num(doc_num)
        if shelf_num == target_shelf_num:
            print(f'Документ №{doc_num} уже находится на полке {target_shelf_num}!')
            return
        else:
            if target_shelf_num in directories.keys():
                # полка существует: переносим!
                # вначале удаляем:
                for i, docs in enumerate(list(directories[shelf_num])):
                    if doc_num == docs:
                        del directories[shelf_num][i]
                # теперь ставим:
                directories[target_shelf_num].append(doc_num)
                print(f'Документ №{doc_num} перемещен на полку {target_shelf_num}!')
            else:
                # полка не существует!
                print(f'Полки с номером {target_shelf_num} нет!')
                answer = input(f'Желаете добавить новую полку (Y/N)?')
                if answer == 'Y' or answer == 'y':
                    print(f'Внимание! Документ будет поставлен на новую полку {target_shelf_num}!')
                    directories.setdefault(target_shelf_num, [doc_num])
                else:
                    return

    else:
        print(f'Документ c №{doc_num} в системе документооборота не значится!')
        answer = input(f'Желаете добавить документ №{doc_num} в систему (Y/N)?')
        if answer == 'Y' or answer == 'y':
            add_new_doc(doc_num)


# удаляет документ по заданому номеру - d
def del_doc_by_num():
    doc_num = input('Введите номер документа: ')
    doc_index = -1

    # ищем документ
    for i, docs in enumerate(documents):
        if doc_num == docs["number"]:
            doc_index = i

    # результат:
    if doc_index != -1:
        # удаляем документ из списка документов
        del documents[doc_index]
        # удаляем документ с полки
        shelf_num = get_shelf_by_doc_num(doc_num)

        for i, docs in enumerate(list(directories[shelf_num])):
            if doc_num == docs:
                del directories[shelf_num][i]

        print(f'Документ №{doc_num} успешно удален!')
        # возвращаем номер документа и номер полки
        return [doc_num, shelf_num]

    else:
        print(f'Документ c №{doc_num} в системе документооборота не значится!')
        answer = input(f'Желаете добавить документ №{doc_num} в систему (Y/N)?')
        if answer == 'Y' or answer == 'y':
            add_new_doc(doc_num)

# спрашиваем номер документа и выводим имя человека, которому он принадлежит - p
def get_doc_by_num():
    """
    Получить документ по номеру, который укажет пользователь:
    :return:
    """
    doc_num = input('Введите номер документа: ')
    name = ''

    # ищем документ
    for docs in documents:
        if doc_num == docs["number"]:
            name = docs["name"]

    # результат:
    if name != '':
        print(f'Документ №{doc_num} принадлежит {name}')
        value= {doc_num,name}
        return value
    else:
        print(f'Документ c №{doc_num} в системе документооборота не значится!')
        answer = input(f'Желаете добавить документ №{doc_num} в систему (Y/N)?')
        if answer == 'Y' or answer == 'y':
            add_new_doc(doc_num)


# спрашиваем номер документа и выводим номер полки, на которой он находится - s
def get_shelf_by_doc_num(doc_num=''):
    if doc_num == '':
        doc_num = input('Введите номер документа: ')
    shelf_num = ''

    # перебираем полки
    for num, shelfs in directories.items():
        # print(num, shelfs)
        if doc_num in shelfs:
            shelf_num = num

    # результат:
    if shelf_num != '':
        print(f'Документ №{doc_num} находится на полке № {shelf_num}.')
        return shelf_num
    else:
        print(f'Документ c №{doc_num} в системе документооборота не значится!')
        answer = input(f'Желаете добавить документ №{doc_num} в систему (Y/N)?')
        if answer == 'Y' or answer == 'y':
            add_new_doc(doc_num)


# вывод списка всех документов в формате passport "2207 876234" "Василий Гупкин" - l
# переделана для лучшего тестирования (вывод результат для проверки)
def get_doc_list():
    return_str=''
    #print('\nСписок всех документов:')
    return_str+='\nСписок всех документов:\n'
    for docs in documents:
        #print(f'{docs["type"]} \"{docs["number"]}\" \"{docs["name"]}\"')
        return_str +=f'{docs["type"]} \"{docs["number"]}\" \"{docs["name"]}\"\n'

    return return_str

# добавление нового документа в каталог и в перечень полок. Спрашиваем номер документа, тип, имя владельца и номер полки,
# на котором он будет храниться - a
def add_new_doc(doc_number=''):
    if doc_number == '':
        doc_number = input('Введите номер документа: ')

    #проверка на существование документа:
    if is_doc_exist(doc_number):
        print(f'Документ с номером {doc_number} уже существует!')
        return

    doc_type = input('Введите тип документа: ')
    name = input('Введите имя владельца: ')
    shelf_num = input('Введите номер полки: ')

    # проверка полки:
    # if shelf_num !='1' and shelf_num !='2' and shelf_num !='3':
    if not shelf_num in directories.keys():
        print(f'Полки с номером {shelf_num} нет!')
        answer = input(f'Желаете добавить новую полку (Y/N)?')
        if answer == 'Y' or answer == 'y':
            pass
        else:
            return

    # добавялем документ в список
    documents.append({"type": doc_type, "number": doc_number, "name": name})
    # работаем с полками
    if shelf_num in directories.keys():
        # полка существует: добавляем документ на полку
        directories[shelf_num].append(doc_number)
    else:
        # ставим на новую полку
        print(f'Внимание! Документ будет поставлен на новую полку {shelf_num}!')
        directories.setdefault(shelf_num, [doc_number])

    print(f'\nДокумент №{doc_number}, тип: {doc_type}, владелец: {name}, помещен на полку №{shelf_num}!')


# помощь - h
def help():
    print('\nОписание команд системы документооборота:')
    print('p - для получения имени владельца документа')
    print('s - для получения номера полки, на которой находится документ')
    print('l - для получения списка всех документов')
    print('а - для добавления новых документов')
    print('d - для удаления документов')
    print('m - для переноса документов на другую полку')
    print('as - для добавления новой полки для документов')


def exec_buch():
    print('Система документооборота.')
    while True:

        command = input(
            '\nВведите команду p, l, s, a, d, m, as или h (для помощи).\nКоманда q - для выхода из программы:')

        if command == 'p':
            get_doc_by_num()

        elif command == 's':
            get_shelf_by_doc_num()

        elif command == 'l':
            print(get_doc_list())

        elif command == 'a':
            add_new_doc()

        elif command == 'h':
            help()

        elif command == 'm':
            move_doc_by_num()

        elif command == 'as':
            add_new_shelf_num()

        elif command == 'q':
            print('\n')
            print('Проверка!')
            print('\n')
            print(documents)
            print('\n')
            print(directories)

            return

        elif command == 'd':
            del_doc_by_num()

        # если была введена неверная команда
        else:
            print('Введена неверная команда!')