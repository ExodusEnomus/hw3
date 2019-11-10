#list popular methods
l = []
l.append('a')
print(l)
l.insert(0,'b')
l.insert(0,'c')
l.insert(0,'d')
print(l)
l.pop(1)
print(l)
c = l.count('a')
print(c)
l.reverse()
print(l)

#str popular methods
s = 'this is the string'
print(s.upper())
print(s[4:])
print(s[4:].strip())
print(len(s))
print(s.split(' '))

#set popular methods
l = [1,1,2,2,3,3,4,4]
a = set(l)
print(a)
print(1 in a)
b = a.copy()
b.remove(1)
print(b.issubset(a))
print(a.difference(b))
b.clear()

#dict popular methods
d = dict.fromkeys(l,10)
print(d)
print(d.get(1))
print(d.pop(1))
print(d.values())
