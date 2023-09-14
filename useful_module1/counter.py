from  collections import Counter
#defaultdict, 



li = [1,2,3,4,5,6,7]
#print(Counter(li))

#output : {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}

#Counter create dictionary that keeps track of how many times an item occured in a iterable


li = [1,2,3,4,5,6,7,7]
#print(Counter(li))

#output : Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})


sentence = 'blah blah good morning'
#print(Counter(sentence))


#which letter occured the most
#Counter({' ': 3, 'o': 3, 'b': 2, 'l': 2, 'a': 2, 'h': 2, 'g': 2, 'n': 2, 'd': 1, 'm': 1, 'r': 1, 'i': 1})


#dictionary ={'a':1, 'b': 2}
#print(dictionary['a'])


'''d= OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['a']=1
d2['b']=2

print(d2 == d)

#output : True

#if change ordered output = False
d= OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['b']=1
d2['a']=2

print(d2 == d)'''

#regular dict

d= {'c': 100}
d['a']=1
d['b']=2

d2 = {'c': 100}
d2['a']=1
d2['b']=2

print(d2 == d)

#https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/
