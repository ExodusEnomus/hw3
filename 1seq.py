l = []
elem_count = int(input('Input list elements count'))
i = 0
while i < elem_count:
    curr_elem = input('Input {} element'.format(i))
    l.append(curr_elem)
    i+=1
l.sort()
print(l)