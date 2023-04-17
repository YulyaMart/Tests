documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def name_search(document_data):
    doc_number = input('Введите номер документа: ')
    doc_availability = False
    for document in document_data:
        if document['number'] == doc_number:
            doc_availability = True
            break
    if doc_availability is True:
        return document.get('name')
    else:
        return str(f'Документ с номером {doc_number} не найден')

def shelf_search(document_storage):
    doc_number = input('Введите номер документа: ')
    doc_availability = False
    for k, v in document_storage.items():
        if doc_number in document_storage[k]:
            doc_availability = True
            shelf = k
            break
    if doc_availability is True:
        return shelf
    else:
        return str(f'Документ с номером {doc_number} не найден') 

def documents_list(document_data):
    data = str()
    for i in range(len(document_data)):
        data += str(f'{document_data[i]["type"]} "{document_data[i]["number"]}" "{document_data[i]["name"]}"\n')
    return data 

def new_document(document_data, document_storage, new_doc_type, new_doc_number, new_doc_name, new_doc_shelf):
    # new_doc_type = input('Введите тип документа: ')
    # new_doc_number = input('Введите номер документа: ')
    # new_doc_name = input('Введите ФИО: ')
    # new_doc_shelf = input('Введите номер полки для хранения документа: ')
    shelf_avalibility = False
    for shelf in document_storage:
        if new_doc_shelf == shelf:
            shelf_avalibility = True
    if shelf_avalibility == True:
        document_storage[new_doc_shelf].append(new_doc_number)
        document_data.append({'type': new_doc_type, 'number': new_doc_number, 'name': new_doc_name})
        return str(f'Документ номер {new_doc_number} был добавлен')
    else: 
        return str(f'Полки с номером {new_doc_shelf} в хранилище не сущетсвует')

def document_deletion(document_data, document_storage, doc_number):
    # doc_number = input('Введите номер документа: ')
    doc_availability = False
    for document in document_data:
        if document['number'] == doc_number:
            doc_availability = True
            document_data.remove(document)
            for k, v in document_storage.items():
                if doc_number in document_storage[k]:
                    v.remove(doc_number)
    if doc_availability is True:
        return str(f'Документ с номером {doc_number} удален')
    else:
        return str(f'Документ с номером {doc_number} не найден')

def move_document(document_storage):
    doc_number = input('Введите номер документа: ')
    new_doc_shelf = input('Введите номер полки для хранения документа: ')
    doc_availability = False
    shelf_avalibility = False
    for shelf in document_storage:
        if new_doc_shelf == shelf:
            shelf_avalibility = True
    for k, v in document_storage.items():
        if doc_number in document_storage[k]:
            doc_availability = True
            if shelf_avalibility is True:
                v.remove(doc_number)
                document_storage[new_doc_shelf].append(doc_number)
                break
    if doc_availability is True and shelf_avalibility is True:
        return str(f'Документ с номером {doc_number} перемещен на {new_doc_shelf} полку')
    if doc_availability is True and shelf_avalibility is False:
        return str(f'Полка под номером {new_doc_shelf} не найдена')
    if doc_availability is False and shelf_avalibility is True:
        return str(f'Документ с номером {doc_number} не найден')
    else: 
        return str(f'Документ с номером {doc_number} и полка под номером {new_doc_shelf} не найдены')


def new_shelf(document_storage):
    new_shelf_number = input('Введите номер новой полки: ')
    shelf_existence = False
    for k in document_storage.keys():
        if k == new_shelf_number:
            shelf_existence = True
    if shelf_existence is True:      
        return str(f'Полка с номером {new_shelf_number} уже существует')
    else:
        document_storage[new_shelf_number] = []
        return str(f'Полка с номером {new_shelf_number} успешно добавлена')
    
def document_handling(document_data, document_storage):
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            print(name_search(document_data))
        if command == 's':
            print(shelf_search(document_storage))
        if command == 'l':
            print(documents_list(document_data))
        if command == 'a':
            print(new_document(document_data, document_storage))
        if command == 'd':
            print(document_deletion(document_data, document_storage))
        if command == 'm':
            print(move_document(document_storage))
        if command == 'as':
            print(new_shelf(document_storage))

if __name__ == '__main__':
    document_handling(documents, directories)