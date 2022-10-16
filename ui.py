#Создать телефонный справочник с возможностью импорта и экспорта данных .
#Что должен уметь справочник?
#1) Добавить новый контакт
#2) Поиск контакта по имени

import model
import logger

#def get_input(value): # метод получения информации
   # return input(value)
#def show_phone(a): # метод вывода информации
   # print(a)


fnums = "phonebook.txt"
nums_list = logger.get_data_from_file(fnums)
list = model.search_phone(nums_list)

print(list)
new_data = model.enter_data()
new_list = logger.enter_data_to_file(fnums, new_data)
print(f' запись сохранена {new_data}')
