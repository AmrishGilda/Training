print ('obj');
print ("one", "two", 'three');

stuff = ['aa', 'bb', 'cc']
stuff1 = ['d', 'e', 'f']
stuff2 = stuff + stuff1;
for item in stuff2[2:5]:
    print (item);
#   print (len(stuff));
#   print(len(stuff2));

a='abc'
print(a.upper())
a=4;
b=5;
print (type((a/b)));
print (type(stuff));
x=int("1");
print (x);
print (type(x));

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist.pop()
print(thislist)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)

a=0

def myfunc(n):
    return lambda a: a - n


mydoubler = myfunc(2)
print(mydoubler(11))