from random import shuffle
#Adding elms from list_1 to List_2 withoout using append fn
l1=[1,2,3,4,5]
l2=[i for i in l1]
l2=[i for i in "ABCDE"]
print(l1,l2)


#As range(num) is the generator
list(range(20))


#Use of enumerate [to get index counter and its associted elm
for i in enumerate("ABCDEF"):
    print(i) #Give (0,A)(1,B)...(5,F)


#use of zip(lis1,list2,...list n)
l1=["1","2","3"]
l2=["one","two","three","four"]
for i in zip(l1,l2):
    print(i)


#unpacking using zip
print([a+b for a,b in zip(l1,l2)])


#object creation
print(i for i in zip(l1,l2))


#adding that obj list
print([i for i in zip(l1,l2)])

#checking value  is in ilist or not
print("Vlaue" in l2[1:2])


#checking  in dictionary
print("key_name" in {"key":3})
d={"key":"Value"}
print("value_Name" in d.values())

#using shuffle lib
print(l1)
#use of shuffle fn
shuffle(l1)
print(l1)
print(shuffle(l1))
print(l1)
#1.
#as its not a attribute of list obj  its a built in fn in package lib
# we cant use
#[ERROR]print(l1.shuffle())

#2.
#we cant store directly shuffle list as it dont return anydata Type
#store_list=shuffle(l1)
#[ERROR]print(type(store_list))

#input and randint()
