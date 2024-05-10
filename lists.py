def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)>0:
        if len(list_to_remove_elements)>=6:
            del list_to_remove_elements[0]
            del list_to_remove_elements[3]
            del list_to_remove_elements[3]
            return list_to_remove_elements
        elif len(list_to_remove_elements)<6 and len(list_to_remove_elements)>=5:
            del list_to_remove_elements[0]
            del list_to_remove_elements[3]
            return list_to_remove_elements
        elif len(list_to_remove_elements)<5:
            del list_to_remove_elements[0]ç
            return list_to_remove_elements
    else:
        return list_to_remove_elements
remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements
add_elements(['Red', 'Green', 'White', 'Black'])


def is_empty(list_to_check):
    if len(list_to_check)==0:
        return True
    else:
        return False
print(is_empty([]))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return True
    else:
        return False
check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'],['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink'])


def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify=[list_of_lists_to_modify[0][0:2]]+[list_of_lists_to_modify[1][1:4]]+[list_of_lists_to_modify[2][-2:]]
    return list_of_lists_to_modify
list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]])
