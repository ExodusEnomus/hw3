list_elements = input('Input list elements')

if list_elements.find(',') != -1:
    l = list_elements.split(',')
elif list_elements.find(';') != -1:
    l = list_elements.split(';')
elif list_elements.find('/') != -1:
    l = list_elements.split('/')

s = set(l)
l = []
for i in s:
    l.append(i)
print(l)