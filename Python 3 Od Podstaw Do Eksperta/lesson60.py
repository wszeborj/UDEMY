def evilfunction(toBeDestroyed):
    # toBeDestroyed.clear()
    print('tobedestroyed', id(toBeDestroyed))


mylist=[1,2,3,4,54,76]

print('mylist', id(mylist))

evilfunction(mylist.copy())

secondlist=mylist.copy()
print('secondlist', id(secondlist))

secondlist[0]=21
print('mylist po zmianie secondlist', mylist)
