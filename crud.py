import json
from json.decoder import JSONDecodeError
from settings import DB

from datetime import datetime


"""
list_ = [
    {
        "id": 1,
        "title": "LG",
        "price": 50000,
        "description": "refrigirator",
        "creation_date": "24.08.22 19:05"
    },
    {
        "id": 2,
        "title": "Samsung",
        "price": 10000,
        "description": "vacuum cleaaner",
        "creation_date": "24.08.22 19:07"
    }
]
"""



def get_all_data():
    """
    Reads all data available in the database
    """
    with open(DB) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []



def create_data():
    """
    Creates a new item in the list
    """
    id_ = datetime.now().strftime('%H%M%S')
    try:
        data = {
            'id': id_,
            'title': input('Введите название: '),
            'price': int(input('Введите цену: ')),
            'description': input('Введите описание: '),
            'creation_date': datetime.now().strftime('%d.%m.%y %H:%M')
        }
        json_data: list = get_all_data()
        json_data.append(data)
        with open(DB, 'w') as f:
            json.dump(json_data, f, indent=4)
    except ValueError:
        print('Неправильно введены данные. Проверьте правильность и повторите попытку')
        data = {
            'id': id_,
            'title': input('Введите название: '),
            'price': int(input('Введите цену: ')),
            'description': input('Введите описание: '),
            'creation_date': datetime.now().strftime('%d.%m.%y %H:%M')
        }
        json_data: list = get_all_data()
        json_data.append(data)
        with open(DB, 'w') as f:
            json.dump(json_data, f, indent=4)



def check_id():
    """
    Shows ids of available items and checks if an id is in the list
    """
    available_id()
    global id_
    id_ = input('Введите id: ')
    global data
    data = get_all_data()
    global obj
    for obj in data:
        if obj['id'] == id_:
            return True
    else:
        return False





def get_data_by_id():
    """
    Retrieves an item from a list by id
    """
    while check_id() == False:
        print(f'{id_} нет в списке. Проверьте правильность ввода')
        continue
    else:
        return obj



def delete_data():
    """
    Deletes items from the list by id
    """
    # id_ = input('Введите id: ')
    # data = get_all_data()
    while check_id() == False:
        print(f'{id_} нет в списке. Проверьте правильность ввода')
        continue
    else:
        data.remove(obj)
        with open(DB, 'w') as f:
            json.dump(data, f, indent=4)
        return True



def update():
    """
    Updates info about items
    """
    while check_id() == False:
        print(f'{id_} нет в списке. Проверьте правильность ввода')
        continue
    else:
        try:
            obj['title'] = input('Введите новое название: ') or obj['title']
            obj['price'] = int(input('Введите новую цену: ')) or obj['price']
            obj['description'] = input('Введите новое описание: ') or obj['description']
        except ValueError:
            obj['price'] = obj['price']
            obj['description'] = input('Введите новое описание: ') or obj['description']
        finally:
            print('-' * 80 + f'\nДанные товара обновлены:\n{obj}')
        with open(DB, 'w') as f:
            json.dump(data, f, indent=4)



def available_id():
    """
    Prints all available ids
    """
    with open(DB, 'r') as f:
        f.seek(0)
        python_data = json.load(f)
        list_of_keys = []
        for item in python_data:
            list_of_keys.append(item['id'])
        print(f'Доступные id:{list_of_keys}')



def clear():
    """
    Clears the list of items
    """
    with open(DB, 'w+') as f:
        try:
            json.load(f)
            print(type(f))
            f.clear()
        except:
            return []
        finally:
            print('Список товаров пуст')



def interface():
    """
    Interface of the app. It is called in the main.py to run the program
    """
    while True:
        operation = str(input("""
            Выберите операцию, которую хотите совершить:
                1. Create - создать новый товар
                2. Read - получить список всех товаров
                3. Retrieve - получить подробную информацию по определнному товару
                4. Delete - удалить товар
                5. Clear - очистить список
                6. Update - обновить товар
                7. Exit - выйти из программы
        """)).strip().lower()

        if operation == '1' or operation == 'create':
            create_data()
        elif operation == '2' or operation == 'read':
            for item in get_all_data():
                print('-' * 109)
                print(item)
                print('-' * 109)
        elif operation == '3' or operation == 'retrieve':
            print(f'Ваши данные: {get_data_by_id()}')
        elif operation == '4' or operation == 'delete':
            delete_data()
        elif operation == '5' or operation == 'clear':
            clear()
        elif operation == '6' or operation == 'update':
            update()
        elif operation ==  '7' or operation == 'exit':
            print('Всего доброго!')
            break
        else:
            print('Такой операции не существует. Проверьте правильность ввода.')
            continue