def _get_list_from_str(_str):
    if _str.find(',') != -1:
        return _str.split(',')
    elif list_elements.find(';') != -1:
        return _str.split(';')
    elif list_elements.find('/') != -1:
        return _str.split('/')

list_elements = input('Input 1-st list elements')
l_1 = _get_list_from_str(list_elements)
print(l_1)

list_elements = input('Input 2-nd list elements')
l_2  = _get_list_from_str(list_elements)
print(l_2)

s_1 = set(l_1)
s_2 = set(l_2)

diff_s = s_1.difference(s_2)

l = []
for i in diff_s:
    l.append(i)

l.sort()
print(l)



