import collections

print(list(set([1,2,3]+[1,2,3,4,5])))

di = {
    '1': 23123,
    '2':3141,
}

for key,val in di.items():
    print(key,val)

a = collections.Counter(x=3,y=4)
print(a)
b = collections.Counter(x=3,z=4)
print(b)
print(a+b)