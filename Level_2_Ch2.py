#more on list
#appending chars or iterable in new list
'''l1=[1,2,"223"]
l2=[]
for i in l1:
    l2.append(i)
    print(l2)
print(l2)'''

#One liner way
l1=[1,2,3,"89"]
l=[x for x in l1]
print(l)
l=[]
l=[x for x in range(0,11)]
l=[]
#expression in list comprehension
l=[i^2 for i in range(1,10)]
print(l)
l=[]
#use of if under list comprehension
l=[x^2 for x in range(1,10) if x%2==0]
print(l)
l=[]
#use of elset
l=[x if x%2==0 else 'odd' for x in range(10)]
print(l)
l=[]
#[controversial]
'''l=['expression in termm of x'  for x in 'iterables' ]
print(type(l))
print(l[-1])'''
#list unpaking in list comprehension
l=[x+y for x in [1,2,3] for y in [10,100.1000]]
print(l)
l=[]

#how to learn yourself
help(l.extend) #NOTE dont use parenthesis it will make it as a attribute
#use python docs


