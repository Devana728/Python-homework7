def enter_data():
    fio = input('введите ФИО => ')
    number = input ('введите номер телефона =>')
    data = fio + '  ' + number
    return  '\n' + data
def search_phone(f):
    search =  input('введите поисковый критерий =>')
    my_find = list(filter(lambda x : search  in x.split(), f.split('\n')))
    return '\n'.join(my_find)

