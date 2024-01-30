#list:
'''
1.Are ordered so can use Indexing here also to access that data
2. are Mutable :so can change the dataType,edit the existing data,remove the data,add,clear all data
mutate:
    l1=[1,2,3]
    first we will access that thing using Indexing
    l1[0]
    then edit or mutate
    l1[0]="one"
add:
    using append fn
    no need to access the Index where we want to edit in append fn , it auto add in the last
    l1.append("someOther")
remove:
    using pop fn pop(Index), indiex sppecify to remove the required Item from indexing
    l1.pop()
    l1.pop(1)
3. concatenate two list together
    l1=[1,"!",1.2]
    l2=["one"]
    l2+l1 //will return a new lsit and can also be assigned tnti new varible
4. New thing to sort the List ,not return anything , it edits the existing list
using sort fn
    Note : Type is importsnt here
    l1.sort()
    when we print l1 , observe its actually sorted now
    we cant do
    new_l1=l1.sort()
    type(new_l1) give none type
    INSTEAD
    l1.sort()
    new_list=l1
    l=l[::-1]
    


'''

#Dictionary
'''
INSTEAD OF INDEXING WE SPECIFY THE ASSOCIATED KEY WITH THAT VALUE TO ACCES THAT VALUE , NOTE WE CAN ACCESS THE KEY BY SPECYFING THE ASSCOCIATED VALUE
use: get the data/value by assinging the correct variable/key name to that data/value
pros: access the value/data by specifying teh associated key with that value 
{key:value}
USE: ENGLISH_SUBJECT={"SOHAN":23,"RAHUL":22,"ISHAAN":
1. Unorderd mappings 
2. NESTED DICT SUPPORT;
3. [CHECK] USE String DATA  For KEY and any data for value 
4. Ex:
d={'':[1,2,"key In dict",2.3,[{'key_in_dict_in_List_in dict':"value"}]],'':1.2,}
5.Methods:
    d['k1']="nw value"
    d.keys() //return all keys as list 
    d.values() //return all values as list
    d,items() //return all key value pairs as list
'''
#SETS
'''
1.Are unordered collection of UNIQUE elements
{cant have more than one}

2.Init of set 
    my_set=set()
3.methods;
    add:
    my_set.add(2)
    try using adding 2 agian 
    my_str.add(2)
    
    effiecinet way of adding 
    l1=[1,2,1,23,3,3,2,1,1]
    my_set.add(l1)
    my-set ony conatins unique elm of above list and are unordered 
'''
#Boolean
'''used to make logic
true=True
false=True
'''
