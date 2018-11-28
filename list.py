mylist = []
print('TYPE = {}'.format(type(mylist)))

#add
mylist += ['aaa','bbb','ccc']
print(mylist)
mylist.append('ddd')
print(mylist)
print(mylist[0])
mylist[0] = 'eee'
print(mylist)

#search index
print(mylist.index('ccc'))

#insert
mylist.insert(2,'fff')
print('Insert index 2 "fff" = {0}'.format(mylist))

if 'DDD' in mylist:
    print(mylist.index('DDD'))
print(len(mylist))

#loop range
for i in range(len(mylist)):
    print(mylist[i])
print('*'*30)

#loop mylist
for i in mylist:
    print(i)

print(mylist[1:3])
print(sorted(mylist))
print(sorted(mylist,reverse=True))
mylist.remove('eee')
if 'eee' in mylist:
    mylist.remove('eee')
    print('Remove "eee" success !!')
else:
    print("Don't have 'eee' in mylist")

print(mylist)

m = [(i*1.60934) for i in range(1 ,6)]
print(m)
print(type(m))



