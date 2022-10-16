def get_data_from_file(nums):
    data = open(nums,'r', encoding='utf-8')
    dlist = data.read()# + ' '
    data.close()
    return dlist
def enter_data_to_file(nums, items):
    data = open(nums,'a', encoding='utf-8')
    data.write(items)# + ' '
    data.close()